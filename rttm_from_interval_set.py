def rttm_from_interval_set(interval_set, fname='filename', rttm=True):
    """ Given an interval_set from the -unsilence-
        package, generate an .rttm file with the format

        Type -- segment type; should always be SPEAKER
        File ID -- file name; basename of the recording minus extension (e.g., rec1_a)
        Channel ID -- channel (1-indexed) that turn is on; should always be 1
        Turn Onset -- onset of turn in seconds from beginning of recording
        Turn Duration -- duration of turn in seconds
        Orthography Field -- should always be <NA>
        Speaker Type -- should always be <NA>
        Speaker Name -- name of speaker of turn; should be unique within scope of each file
        Confidence Score -- system confidence (probability) that information is correct; should always be <NA>
        Signal Lookahead Time -- should always be <NA>

        SPEAKER pooppants 1 0.010 1.363 <NA> <NA> KCHI <NA> <NA>
    """
    result_set = [[
                  'interval',
                  'start',
                  'end',
                  'duration',
                  'is_silent'
                 ]]
    rttm_set = []
    i = 1
    for interval in interval_set:
        str_int = str(interval) \
                    .strip('[<>]') \
                    .replace("Interval start=", f"{i},") \
                    .replace(" end=", ",") \
                    .replace(" duration=", ",") \
                    .replace(" is_silent=", ",")
        new_int = str_int.split(',')
        result_set.append(new_int)
        rttm_set.append(f'SPEAKER ' +
                        f'{fname} 1 ' +
                        f'{new_int[1]} '+
                        f'{new_int[3]} <NA> <NA> ' +
                        f'{"SIL" if new_int[4]=="True" else "SND"} '+
                        '<NA> <NA>')
        i += 1

    if rttm:
        return rttm_set
    else:
        return result_set
