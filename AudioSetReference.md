# AudioSet Reference

The project leverages the [Google Research AudioSet](https://research.google.com/audioset/). This readme file summarizes key features and considerations for the purposes of our project. Reading through the entirety of Google's documentation for the AudioSet is highly recommended.

## The AudioSet in Brief

The _AudioSet_ is a dataset of labeled 10-second segments of YouTube videos.
+ You can download CSVs containing information that will provide you the labels and also point you to the relevant video segments.
+ You can download TensorFlow tensors.

We will prefer to go the first way, as we want to build out our dataset from scratch.
+ As described [here](https://research.google.com/audioset/dataset/index.html), there are a large number of videos (over 2 million at this writing) whose segments have been labeled with over 500 labels (527 at this writing).
+ The CSV version of the AudioSet can be downloaded [here](https://research.google.com/audioset/download.html). The structure of the CSV is as follows:
```bash
# YTID, start_seconds, end_seconds, positive_labels
-0RWZT-miFs, 420.000, 430.000, "/m/03v3yw,/m/0k4j"
```
+ _YTID_ refers to the YouTube Video ID: the characters to be appended to the base URL (e.g., `https://www.youtube.com/watch?v=YTID-GOES-HERE`) to access the video
+ _positive\_labels_ refers to the auditory phenomena which have been identified as taking place in the span demarcated by the _start\_seconds_ | _end\_seconds_ segment

As the example in the documentation states, that example row
> means that for the YouTube video -0RWZT-miFs, for the 10 second chunk from t=420 sec to t=430 sec, annotators confirmed the presence of sound classes /m/03v3yw ("Keys jangling") and /m/0k4j ("Car").

To make heads or tails of the labels, you need to make reference to the [AudioSet Ontology](https://research.google.com/audioset/ontology/index.html). The `get-audioset.sh` shell script in this project generates a very basic (and flattened) mapping of the ontology's unique codes to a human-readable label.

## Our Code

The _AudioSet_ section of our project has a few utility scripts to make working with this dataset more straightforward.
+ `get-audioset.sh`: a shell script that
    - downloads
        + the three AudioSet CSV files (**evaluation**, **balanced_train_segments**, **unbalanced_train_segments**)
        + the QA ("Quality Assessment and Rerating") CSV file indicating the degree of quality Google believes the labels reflect
        + the list of videos that were rerated during the QA exercise
        + the AudioSet Ontology in JSON format
        + 