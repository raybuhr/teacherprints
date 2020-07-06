# Setting up your dev environment

1. SSH into the EC2 instance
1. The Miniconda3 installer is in `/home/software_assets/` - from your user's $HOME directory, run `$ bash ../software_assets/Miniconda`
1. Verify that the installation has added miniconda to your `PATH` by invoking `$ echo $PATH`
1. By default the installer will attempt to place it at `home/yourUsernameHere/miniconda3`
1. Accept the license agreement `$ >>> yes` and accept the offer for the installer to initialize Miniconda `$ >>> yes`.
1. Leave the terminal and return `$ exit` and then SSH back in.

```bash
$ conda config --add channels conda-forge
$ conda config --set channel_priority strict
$
$
$
$

```

```bash
$ sudo apt-get install sox
$ sudo apt-get install libsox-fmt-mp3
$ sox --version
```


[The Definitive Guide to Conda Environments](https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533)
+ [Install npm package with conda via environment.yml](https://stackoverflow.com/questions/57082949/install-npm-package-with-conda-via-environment-yml) - installing _svelte_ this way won't work
+ [How to update an existing conda environment with a yml file](https://stackoverflow.com/questions/42352841/how-to-update-an-existing-conda-environment-with-a-yml-file)

+ [Getting 'Warning:youtube-dl not found'](https://github.com/mps-youtube/pafy/issues/154)
+ [Registering an application with YouTube to get an API key...](https://developers.google.com/youtube/registering_an_application) not strictly necessary for pafy, but we'd be better netizens if we intended to download lots of YouTube videos for the audioset...
+ [PyPI: sox 1.3.7](https://pypi.org/project/sox/) - it indicates it's _a python wrapper around SoX_. Which means we _do_ need to have SoX installed already as a dependence or there's nothing to wrap.
+ [Installation of SoX on different platforms](https://at.projects.genivi.org/wiki/display/PROJ/Installation+of+SoX+on+different+Platforms)
    * Along the way, found this: [Using CMUSphinx and Training a Model to Enhance the Accuracy of Speech Recognition](https://at.projects.genivi.org/wiki/display/PROJ/Using+CMUSphinx+and+Training+a+Model+to+Enhance+the+Accuracy+of+Speech+Recognition)

You can create a base env using `$ conda env create -f YourEnvironmentDefinitionHere.yml` and then update it at a later point using `$ conda env update --name NameOfEnvToUpdate --file NewParametersHere.yml`


+ To save Librosa spectrograms, etc.: https://stackoverflow.com/questions/56719138/how-can-i-save-a-librosa-spectrogram-plot-as-a-specific-sized-image

+ [Pafy can't natively handle snippets of a video](https://stackoverflow.com/questions/28423501/download-part-of-the-youtube-video-using-python)
+ [](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl)
+ https://stackoverflow.com/questions/27473526/download-only-audio-from-youtube-video-using-youtube-dl-in-python-script
+ https://stackoverflow.com/questions/41240726/change-the-output-name-when-download-with-youtube-dl-using-python
+ https://github.com/kkroening/ffmpeg-python
+ https://askubuntu.com/questions/966488/how-do-i-fix-r-command-not-found-errors-running-bash-scripts-in-wsl