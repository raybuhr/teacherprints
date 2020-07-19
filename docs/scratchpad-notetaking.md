
https://medium.com/@limichelle21/connecting-google-domains-to-amazon-s3-d0d9da467650 <-- almost worked, except the "www."-prefixed version gives 404.

https://stackoverflow.com/questions/10115799/set-up-dns-based-url-forwarding-in-amazon-route53

https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo

https://www.codementor.io/@jqn/deploy-a-flask-app-on-aws-ec2-13hp1ilqy2


## Ensuring we can install / update conda packages...

sudo chmod -R 777 ~/.conda
sudo chown -R tslade:tslade /opt
# Then changed it back to root:root - might work as-is now?
conda install -c mvdbeek multiprocessing-logging
conda install -c conda-forge sk-video
conda install -c conda-forge youtube-dl
conda install -c conda-forge sox


## Path arguments we need to share with the -download_audioset.py- invocation...
conda activate audioset-env
python download_audioset.py -v -f /home/tslade/.conda/envs/audioset-env/bin/ffmpeg ../data


ffmpeg path: /home/tslade/.conda/envs/audioset-env/bin/ffmpeg
ffprobe path: /home/tslade/.conda/envs/audioset-env/bin/ffprobe
audio_codec:
audio_sample_rate:
audio_format:


https://github.com/marl/audiosetdl/issues/17:
--audio-format wav --audio-codec pcm_s16le

audio_dl_args = [ffmpeg_path, '-n',
'-ss', str(ts_start), # The beginning of the trim window
'-i', best_audio_url, # Specify the input video URL
'-t', str(duration), # Specify the duration of the output
'-vn', # Suppress the video stream
'-ac', '1', # Set the number of channels
'-sample_fmt', 's16', # Specify the bit depth
'-f', 'wav', # Specify output format
'-acodec', audio_codec, # Specify the output encoding
'-ar', '44100', # Specify the audio sample rate
audio_filepath]

Various errors:

sox.core.SoxiError: SoXI failed with exit code 1
This install of SoX cannot process .flac files.
2020-06-11 03:07:30,675 - audiosetdl - ERROR - Error while processing video -2xiZDEuHd8: [Errno 2] No such file or directory: './bin/ffmpeg/ffprobe';
UserWarning: ffmpeg/ffprobe not found in path: ./bin/ffmpeg
subprocess.CalledProcessError: Command '['sox', '--i', '-c', '../data/data/eval_segments/audio/-1UWSisR2zo_30000_40000.flac']' returned non-zero exit status 1




(base) tslade@ip-172-31-29-82:~/projects/pyclan-repo/pyclan-master$ conda info

     active environment : base
    active env location : /opt/miniconda3
            shell level : 1
       user config file : /home/tslade/.condarc
 populated config files :
          conda version : 4.8.3
    conda-build version : not installed
         python version : 3.7.6.final.0
       virtual packages : __glibc=2.27
       base environment : /opt/miniconda3  (read only)
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /opt/miniconda3/pkgs
                          /home/tslade/.conda/pkgs
       envs directories : /home/tslade/.conda/envs
                          /opt/miniconda3/envs
               platform : linux-64
             user-agent : conda/4.8.3 requests/2.23.0 CPython/3.7.6 Linux/4.15.0-1065-aws ubuntu/18.04.4 glibc/2.27
                UID:GID : 1001:1001
             netrc file : None
           offline mode : False


cat eval_segments.csv.bak | head -6903 | tail -1000 >> eval_segments_big-cow06.csv



# big-cow02
gtcode w210_capstone/teacherprints
ssh big-cow02
exit
scp -i .secrets/teacherprints-ec2.pem eval_segments_big-cow02.csv tslade@ec2-3-19-227-218.us-east-2.compute.amazonaws.com:projects/data/eval_segments_big-cow_02.csv; ssh big-cow02;
## To execute within the instance
tmux; cd ~/projects/audiosetdl; conda activate audioset-env; mkdir ~/projects/data/big_cow02; python download_audioset.py -f /home/tslade/.conda/envs/audioset-env/bin/ffmpeg -fp /home/tslade/.conda/envs/audioset-env/bin/ffprobe -ac pcm_s16le -af wav -e ../data/eval_segments_big-cow_02.csv -lp ./audioset-dl_big-cow_02.log ../data/big_cow02

# Finds the name of the first 429-error-generating file
`$ cat ~/projects/audiosetdl/audioset-dl_big-cow_02.log | grep 'HTTP Error 429:' | head -1 | cut -d ":" -f 3 | cut -d " " -f 11`

# Gets the count of videos retrieved:
`$ ls -lah ~/projects/data/big_cow04/data/eval_segments_big-cow_04/audio | wc -l`

# Look at the last five videos DLed to cross-reference last one with source csv:
`$ ls -lah ~/projects/data/big_cow03/data/eval_segments_big-cow_03/audio | tail -5`

# Finds the YTID of the last video DLed
`$ vim ~/projects/data/eval_segments_big-cow_04.csv`
`: set number`
`/ {YTID-of-first-429-generating-file}`
`# copy the id of the subsequent file`

# Download and back up the audiosetdl logs
scp -i .secrets/teacherprints-ec2.pem tslade@ec2-3-19-227-218.us-east-2.compute.amazonaws.com:~/projects/audiosetdl/audioset-dl_big-cow_02.log .


# Back these records up to S3

By default, your instance may not have the aws cli tool installed. So step 1 is getting that in place.

```bash
$ sudo apt install awscli
```

If you try to leap directly ahead to moving objects from place to place, you'll run into errors as a result of having failed to properly configure your access credentials. So the next step is to get those set. Have your `AWS Access Key ID` and `AWS Secret Key ID` handy - these are the ones I issued you when I first configured the IAM users.

```bash
# https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
$ aws configure
# paste in your AWS Access Key ID
# paste in your AWS Secret Key ID
# set your default region to be us-east-2
# set your default output format to json
```

Our S3 bucket is at `s3://teacherprints.org`. Note that passing the destination as `https://s3-us-east-2.amazonaws.com/teacherprints.org` will result in an `Access Denied` error.

S3 is smart enough to create any intermediate paths necessary for the endpoint to be valid, so we don't need to attempt a `$ mkdir` of some sort before copying over our stuff.

```bash
$ aws s3 cp ~/projects/data/eval_segments_big-cow_02.csv s3://teacherprints.org/data/allocations/
$ aws s3 cp ~/projects/data/big_cow02/data/eval_segments_big-cow_02/audio/ s3://teacherprints.org/data/audiofiles --recursive
```

You might think you need to feed the bucket the `s3://` prefix, but in this call you do not. In fact, doing so will cause the call to fail.

`$ aws s3api list-objects --bucket teacherprints.org --query 'Contents[].{Key: Key, Size: Size}'`



# Big-Cow03
gtcode w210_capstone/teacherprints
ssh big-cow03
exit
scp -i .secrets/teacherprints-ec2.pem eval_segments_big-cow03.csv tslade@ec2-3-128-76-226.us-east-2.compute.amazonaws.com:projects/data/eval_segments_big-cow_03.csv; ssh big-cow03;
## To execute within the instance
tmux; cd ~/projects/audiosetdl; conda activate audioset-env; mkdir ~/projects/data/big_cow03; python download_audioset.py -f /home/tslade/.conda/envs/audioset-env/bin/ffmpeg -fp /home/tslade/.conda/envs/audioset-env/bin/ffprobe -ac pcm_s16le -af wav -e ../data/eval_segments_big-cow_03.csv -lp ./audioset-dl_big-cow_03.log ../data/big_cow03

# big-cow04
gtcode w210_capstone/teacherprints; ssh big-cow04
exit
scp -i .secrets/teacherprints-ec2.pem eval_segments_big-cow04.csv tslade@ec2-18-221-139-67.us-east-2.compute.amazonaws.com:projects/data/eval_segments_big-cow_04.csv; ssh big-cow04;
## To execute within the instance
tmux; cd ~/projects/audiosetdl; conda activate audioset-env; mkdir ~/projects/data/big_cow04; python download_audioset.py -f /home/tslade/.conda/envs/audioset-env/bin/ffmpeg -fp /home/tslade/.conda/envs/audioset-env/bin/ffprobe -ac pcm_s16le -af wav -e ../data/eval_segments_big-cow_04.csv -lp ./audioset-dl_big-cow_04.log ../data/big_cow04

# big-cow05
gtcode w210_capstone/teacherprints; ssh big-cow05
exit
scp -i .secrets/teacherprints-ec2.pem eval_segments_big-cow05.csv tslade@ec2-52-14-56-222.us-east-2.compute.amazonaws.com:projects/data/eval_segments_big-cow_05.csv; ssh big-cow05;
## To execute within the instance
tmux; cd ~/projects/audiosetdl; conda activate audioset-env; mkdir ~/projects/data/big_cow05; python download_audioset.py -f /home/tslade/.conda/envs/audioset-env/bin/ffmpeg -fp /home/tslade/.conda/envs/audioset-env/bin/ffprobe -ac pcm_s16le -af wav -e ../data/eval_segments_big-cow_05.csv -lp ./audioset-dl_big-cow_05.log ../data/big_cow05

# big-cow06
gtcode w210_capstone/teacherprints; ssh big-cow06
exit
scp -i .secrets/teacherprints-ec2.pem eval_segments_big-cow06.csv tslade@ec2-18-188-106-243.us-east-2.compute.amazonaws.com:projects/data/eval_segments_big-cow_06.csv; ssh big-cow06;
## To execute within the instance
tmux; cd ~/projects/audiosetdl; conda activate audioset-env; mkdir ~/projects/data/big_cow06; python download_audioset.py -f /home/tslade/.conda/envs/audioset-env/bin/ffmpeg -fp /home/tslade/.conda/envs/audioset-env/bin/ffprobe -ac pcm_s16le -af wav -e ../data/eval_segments_big-cow_06.csv -lp ./audioset-dl_big-cow_06.log ../data/big_cow06











usage: download_audioset.py [-h] [-f FFMPEG_PATH]
                            [-fp FFPROBE_PATH]
                            [-e EVAL_SEGMENTS_PATH]
                            [-b BALANCED_TRAIN_SEGMENTS_PATH]
                            [-u UNBALANCED_TRAIN_SEGMENTS_PATH]
                            [-ac AUDIO_CODEC]
                            [-asr AUDIO_SAMPLE_RATE]
                            [-abd AUDIO_BIT_DEPTH]
                            [-vc VIDEO_CODEC]
                            [-af AUDIO_FORMAT]
                            [-vf VIDEO_FORMAT]
                            [-vm VIDEO_MODE]
                            [-vfr VIDEO_FRAME_RATE]
                            [-nr NUM_RETRIES]
                            [-n NUM_WORKERS]
                            [-nl]
                            [-lp LOG_PATH]
                            [-v]
                            data_dir

Download AudioSet data locally

positional arguments:
  data_dir              Path to directory where AudioSet data will be stored

optional arguments:
  -h, --help            show this help message and exit
  -f FFMPEG_PATH, --ffmpeg FFMPEG_PATH
                        Path to ffmpeg executable
  -fp FFPROBE_PATH, --ffprobe FFPROBE_PATH
                        Path to ffprobe executable
  -e EVAL_SEGMENTS_PATH, --eval EVAL_SEGMENTS_PATH
                        Path to evaluation segments file
  -b BALANCED_TRAIN_SEGMENTS_PATH, --balanced-train BALANCED_TRAIN_SEGMENTS_PATH
                        Path to balanced train segments file
  -u UNBALANCED_TRAIN_SEGMENTS_PATH, --unbalanced-train UNBALANCED_TRAIN_SEGMENTS_PATH
                        Path to unbalanced train segments file
  -ac AUDIO_CODEC, --audio-codec AUDIO_CODEC
                        Name of audio codec used by ffmpeg to encode output audio
  -asr AUDIO_SAMPLE_RATE, --audio-sample-rate AUDIO_SAMPLE_RATE
                        Target audio sample rate (in Hz)
  -abd AUDIO_BIT_DEPTH, --audio-bit-depth AUDIO_BIT_DEPTH
                        Target audio sample bit depth
  -vc VIDEO_CODEC, --video-codec VIDEO_CODEC
                        Name of video codec used by ffmpeg to encode output audio
  -af AUDIO_FORMAT, --audio-format AUDIO_FORMAT
                        Name of audio format used by ffmpeg for output audio
  -vf VIDEO_FORMAT, --video-format VIDEO_FORMAT
                        Name of video format used by ffmpeg for output video
  -vm VIDEO_MODE, --video-mode VIDEO_MODE
                        Name of the method in which video is downloaded. 'bestvideo' obtains the best quality video that does not contain an audio
                        stream. 'bestvideoaudio' obtains the best quality video that contains an audio stream. 'bestvideowithaudio' obtains the best
                        quality video without an audio stream and merges it with audio stream
  -vfr VIDEO_FRAME_RATE, --video-frame-rate VIDEO_FRAME_RATE
                        Target video frame rate (in fps)
  -nr NUM_RETRIES, --num-retries NUM_RETRIES
                        Number of retries when ffmpeg encounters an HTTPissue, which could be to unpredictable network behavior
  -n NUM_WORKERS, --num-workers NUM_WORKERS
                        Number of multiprocessing workers used to download videos
  -nl, --no-logging     Disables logging if flag enabled
  -lp LOG_PATH, --log-path LOG_PATH
                        Path to log file generated by this script. By default, the path is "./audiosetdl.log".
  -v, --verbose         Prints verbose info to stdout

https://havecamerawilltravel.com/photographer/how-allow-public-access-amazon-bucket/