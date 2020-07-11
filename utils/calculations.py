import pandas as pd
import numpy as np
import copy
import datetime
import time


def CountOverlapsOrPauses(input_df,
                  cols_to_check = ['ADULT', 'CHILD'],
                  target_col    = 'OVERLAPS',
                  full          = True,
                  pauses        = False,
                  verbose       = False):
    """ Given a dataframe and a list of Truthy {cols_to_check},
        generate a new boolean {target_col}.
        If {full}==True all of the {cols_to_check} must be
        switched on to activate the boolean.
        If {pause}==True, identifies observations where none of
        the {cols_to_check} are Truthy.
    """

    if pauses:
        input_df[target_col] = np \
            .where(
                input_df[cols_to_check] \
                .sum(axis = 1) == 0,
                True, False)
        
    else:
        threshold = 1 if (full==False) else len(cols_to_check)
        if verbose:
            print(f'Threshold of activation is {threshold}')

        input_df[target_col] = np \
            .where(
                input_df[cols_to_check] \
                .sum(axis = 1) >= threshold,
                True, False)
    
    return input_df


def FlagUtteranceBoundaries(input_df,
                            label_dict = {'ADULT' :'UTT_A',
                                          'CHILD' :'UTT_C',
                                          'SPEECH': 'UTT_S'},
                            verbose    = False):
    """ Given an input DF and a {label_dict} mapping
        the columns whose boundaries need to be identified to
        the columns where those boundaries will be recorded,
        flag the observations where a segment toggles on or off
    """
    
    for col in label_dict:
        input_df[label_dict[col]] = input_df[col].astype('int32').diff()
    
    return input_df