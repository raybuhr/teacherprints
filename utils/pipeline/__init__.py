# from pipeline import backup, postprocessing, preprocessing
# from .backup import backup_import
# from .postprocessing import postprocessing_import
# from .preprocessing import preprocessing_import

# from . import backup, postprocess, preprocess
from . import (backup, calculations, postprocessing, preprocessing,
               rttm_from_interval_set, rttm_to_speaker_activity,
               transformations)


def confirm_import(user='No-one'):
    print(f'Running for [{user}]')
    print('From preprocessing:')
    if preprocessing_import():
        print(preprocessing_import())
    print('From backup:')
    if backup_import():
        print('Success')
    print('From postprocessing:')
    if postprocessing_import():
        print('Success')

if __name__ == '__main__':
    confirm_import()
