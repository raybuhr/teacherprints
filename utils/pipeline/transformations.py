import pandas as pd
import numpy as np
import copy
import datetime
import time


def DfFromRttm(rttm):
    """ Given an RTTM file, parses it into a Pandas DataFrame.
    """
    df = pd.read_csv(rttm,
                     sep=' ',
                     names=['task', 'inputFile', 'one', 'start', 'duration',
                            'NA_1', 'NA_2', 'class', 'NA_3', 'NA_4'])

    # Drop the columns we don't care about from a base RTTM
    vizframe = copy.deepcopy(df) \
        .drop(
        columns=[
            'task',
            'inputFile',
            'one',
            'NA_1',
            'NA_2',
            'NA_3',
            'NA_4'])

    return vizframe


def SpeechifyDihardDF(input_df,
                      new_label='SPEECH',
                      verbose=False):
    """ Given a DIHARD-generated dataframe
        with labels of type A-Z, AA-AZ, BA-BZ, etc.
        replace the class labels with a label of your
        choosing.
    """
    input_df['class'] = new_label

    if verbose:
        input_df.head(5)
    return input_df


def RttmToUtteranceIndexedSpeakerActivity(df, outfile=None):
    """ Given an RTTM input file, generate a dataframe structured
        to support a visualization of type 'Speaker Activity' and optionally
        export to a csv located at {outfile}

        df = Pandas DataFrame containing a standard .rttm file
        outfile = destination for exported CSV (path, filename, extension)
    """

    # Check whether an outfile has been defined
    if outfile is not None:
        export = True
    else:
        export = False

    # Drop the columns we don't care about from a base RTTM
    vizframe = copy.deepcopy(df)

    # Rename columns for our viz's purposes
    vizframe = vizframe \
        .rename(
            columns={
                'start': 'START',
                'duration': 'DUR',
                'class': 'LABEL'
            })

    # Remap the model classes for this viz's purposes
    vizframe['LABEL'] = vizframe['LABEL'] \
        .map({
            'KCHI': 'CHILD',
            'CHI': 'CHILD',
            'FEM': 'ADULT',
            'MAL': 'ADULT'
        })

    # Filter the dataframe to just the 'clean' (non-'SPEECH') classes
    vizframe = vizframe[vizframe['LABEL'].isin(['CHILD', 'ADULT'])]

    vizframe['LABEL_NUM'] = vizframe['LABEL'] \
        .apply(lambda x: 1 if x == 'CHILD' else (-1 if x == 'ADULT' else NaN))

    vizframe['DUR_TRANS'] = vizframe['LABEL_NUM'] * vizframe['DUR']
    vizframe['COUNT'] = 1

    if export:
        vizframe.to_csv(outfile)

    return vizframe


# Identify the latest timestamp we need.
def GetLatestTimestampNeeded(input_df, verbose=True):
    """ Given an RTTM-derived dataframe,
        extract the last timestamp we'll need
        as a scalar. It will be the maximum value of
        the `start` + `duration` columns.
    """
    input_df['end_time'] = input_df['start'] + input_df['duration']
    end_row = input_df['end_time'].idxmax()
    latest_timestamp = input_df.at[end_row, 'start'] \
        + input_df.at[end_row, 'duration']

    if verbose:
        print(f'''
        >> This DF has data that runs until {latest_timestamp}.
        >> That value was found at row {end_row} and is the sum of
           {input_df.at[end_row, "start"]} and
           {input_df.at[end_row, "duration"]}
           ''')
    return latest_timestamp


# Create millisecond index.
def MakeMillisecondIntegerIndexedDf(
        start,
        duration,
        colname='value',
        colvalue='',
        decimals=4,
        verbose=False):
    """ Create an integer-indexed dataframe covering a
            {duration} from
            {start} having a single column with the name
            {colname} that contains a default value of
            {colvalue} for that named column.
        By default it runs quietly rather than {verbose}.
    """

    if verbose:
        print(f' >>> From [{start}] for [{duration}] seconds'
              f' until [{start+duration}] the col [{colname}]'
              f' will contain the value [{colvalue}]')

    # Create a range between the start and stop
    rng = pd.RangeIndex(start=int(round(start, decimals) * 1000),
                        stop=int(round(start + duration, decimals) * 1000),
                        step=1)

    # Turn that series into a DataFrame and rename the index for clarity
    df = pd.Series(colvalue, index=rng).to_frame(name=colname)
    df.index.name = f'millisecond_ints'
    if verbose:
        print(df.head(3), df.tail(3))
    return df


# Subset by label
def SubsetDfByLabel(df, column_list, key_col, value):
    """ Given a dataframe {df}, return the subset
        of the dataframe defined by {column_list}
        containing {value} in the {key_col} column
    """
    return df[df[key_col] == value][[x for x in column_list]]


def BuildOneHotEncodedDf(input_df,
                         label_list=[],
                         verbose=True
                         ):
    """ Given an RTTM-generated DataFrame, generate a DF containing
        all of the labels of interest in one-hot encoded format
        against an integer-indexed DF representing milliseconds from
        the beginning of the recording
    """

    max_seconds_needed = GetLatestTimestampNeeded(input_df)

    if verbose:
        print(f'max_seconds_needed is equal to {max_seconds_needed}')

    outer_df = MakeMillisecondIntegerIndexedDf(
        start=0,
        duration=max_seconds_needed,
        colname='base_col',
        colvalue=np.nan,
        decimals=4,
        verbose=True)

    if verbose:
        print(f'The outer_df frame will contain {outer_df.shape[0]} records.')

    # Loop through labels, subsetting the original DF so
    # we can merge it back into the main outer DF
    for label in label_list:
        print(f'>>> Processing label: {label}\n')

        if label not in input_df['class'].unique():
            print(f'Label {label} not found in this dataset')
            label_base_df = pd.DataFrame(columns=[label])
            continue

        # Gotta avoid errors from accidentally manipulating original DFs
        temp_df = copy.deepcopy(input_df)

        # Replace the deep-copied DF with a subset of itself
        # that contains only records for the label of interest
        temp_df = SubsetDfByLabel(
            input_df,
            column_list=['start', 'duration', 'class'],
            key_col='class',
            value=label
        )

        if verbose:
            print(f'The temp_df subset for label {label}'
                  f' contains {temp_df.shape[0]} rows')
            print(temp_df.head(5),
                  temp_df.tail(5))

        # The subsetted DF retains the original index unless you reset it
        temp_df.reset_index(drop=True,
                            inplace=True)

        if verbose:
            print(f'The temp_df frame is as follows:\n{temp_df}')

        # Creating the base DF for this label:
        # ranges from 0 to the earliest record
        label_base_df = MakeMillisecondIntegerIndexedDf(
            start=0,
            duration=temp_df['start'].min(),
            colname=label,
            colvalue=np.nan,
            decimals=4,
            verbose=verbose)

        if verbose:
            # The head() will always be the same,
            # so we need to look at the tail() to verify
            print('\n>>> The last few rows of the label_base_df for label'
                  f' {label} are:\n{label_base_df.tail()}'
                  f'\n>>> Base DF size for label {label}: {len(temp_df)}\n')

        for i in temp_df.index:
            if verbose:
                print('*' * 10 + f'{label}: i = {i}' + '*' * 10)
            s, d, cn = temp_df.loc[i, ['start', 'duration', 'class']]
            label_base_df = label_base_df.append(
                MakeMillisecondIntegerIndexedDf(
                    start=s,
                    duration=d,
                    colname=cn,
                    colvalue=1,
                    decimals=4,
                    verbose=verbose
                ))
            
            if verbose:
                print(f'\n>>> Base DF size after {i}' \
                      ' rounds: {len(label_base_df)}')
                print(f'\n>>> The head:\n{label_base_df.head(10)}'\
                      f'\n>>> The tail:\n{label_base_df.tail(10)}')
                print('\n>>> A few of its contents:'\
                      f'\n{label_base_df[~label_base_df[label].isna()].head(5)}')

        # Creating a placeholder for the update call
        outer_df[label] = np.nan
        
        # When attempting the update method:
        print(f'Attempting update with DF from label {label}')
        outer_df.update(
            other     = label_base_df,
            overwrite = True)
        
        if verbose:
            try:
                print(outer_df[~outer_df[label].isna()].head())
            except:
                print(outer_df)

    # Applying Anna's clean-up steps
    # Step 1. Drop the base_col, which was just a placeholder anyway,
    # and replace NaNs with 0s
    outer_df.drop(columns=['base_col'], inplace = True)
    outer_df.fillna(0, inplace=True)
    outer_df = outer_df.astype('int32', copy = True)
    
    # Step 2. 'Combine MAL/FEM and KCHI/CHI'
    # Replaced by ConsolidateLabels() as a post-processing step
    # Step 3: 'Combine ADULT and CHILD columns' (...to make a new 'SPEECH' column)
    # ...is superseded by the DIHARD masking process, but in any case would be
    # accomplished using the ConsolideLabels() function
    
    return outer_df


def ConsolidateLabels(input_df,
                      label_dict = {'ADULT': ['MAL','FEM'],
                                    'CHILD': ['CHI','KCHI']},
                      verbose    = True):
    """ Given a DF containing one-hot encoded columns and
        a dictionary with the desired consolidation labels as keys
        and the source columns as values in lists, consolidate
        the labels
    """

    for target in label_dict:
        sources = [src for src in label_dict[target]]
        input_df[target] = np \
            .where(input_df[sources].sum(axis=1) > 0, True, False)

    return input_df


def DropColumns(input_df,
                to_drop = ['MAL', 'FEM', 'CHI', 'KCHI'],
                verbose = False):
    """ Given a dataframe, drop the listed columns
    """
    return input_df.drop(columns=to_drop, inplace = True, axis = 1)


# Smooth data by eliminating pauses less than back_window + forward_window 
# milliseconds between consecutive statements.
def ApplySmoothing(input_df,
                   back       = 500,
                   forward    = 500,
                   label_dict = {'ADULT': 'SMOOTH_A',
                                 'CHILD': 'SMOOTH_C'},
                   verbose    = False):
    """ Given an input df and window durations of
        {back} and {forward}, apply a smoothing across
        the windows defined by their span to the columns
        listed as keys in {label_dict}, generating the
        columns listed as their values. This eliminates pauses
        that are shorter in duration than the span created by
        {back} and {forward}.
    """

    for src in label_dict:
        back_window    = input_df[src].rolling(back).sum()
        forward_window = input_df[src].iloc[::-1].rolling(forward).sum()
        input_df[label_dict[src]] = np.where((back_window >= 1) & (forward_window >= 1), 1, 0)

    return input_df


def convert(n): 
    return time.strftime("%M min %S sec", time.gmtime(n))


def ApplyDihardMask(dihard_df,
                    marvin_df,
                    write_outer=None,
                    verbose=False):
    """ Given a millisecond-indexed {dihard_df} and
        a millisecond-indexed {marvin_df}, conducts an outer merge
        and then drop any records not present in the {dihard_df}
        dataframe. If {write_outer} is a valid file destination,
        generates a CSV of the full outer join to troubleshoot
        unexpected results.
    """

    outer = pd.merge(left       = marvin,
                    left_index  = True,
                    right       = dihard,
                    right_index = True,
                    how         = 'outer',
                    suffixes    = ('_mar', '_dih')
                   )
    outer.index.rename('millisecond_ints', inplace=True)
    
    if write_outer is not None:
        try:
            outer.to_csv(write_outer)
        except:
            print(f'-write_outer- parameter of {writer_outer}' \
                   'is not a valid destination. Nothing written.')
            
    result = outer.loc[outer['SPEECH_dih'].notna()]
    result.drop(columns=['SPEECH_mar'], inplace=True)
    result.rename(columns={'SPEECH_dih':'SPEECH'}, inplace=True)
    
    if verbose:
        print('Masking MARVIN with DIHARD resulted in the following changes:')
        print('\t\tMarvin\t\tDIHARD\t\tMasked')
        all_cols = [m for m in marvin.columns] \
                 + [d for d in dihard.columns] \
                 + [r for r in result.columns]
        for col in set(all_cols):
            mar_ct = int(marvin[col].sum()) if col in marvin.columns else np.nan
            dih_ct = int(dihard[col].sum()) if col in dihard.columns else np.nan
            res_ct = int(result[col].sum()) if col in result.columns else np.nan
            print(f'{col}\t\t{mar_ct}\t\t{dih_ct}\t\t{res_ct}')

    return result