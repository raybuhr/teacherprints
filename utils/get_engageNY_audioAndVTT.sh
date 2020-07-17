for URL in $(cat /home/projects/data/engageNY/engageNY_vimeoURLs.txt)
do
    youtube-dl -f bestaudio $URL --audio-format wav -o '%(id)s.%(format-id)s' --write-sub --sub-format vtt
done