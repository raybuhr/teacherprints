# AudioSet Research Notes

## Papers
+ [Weakly Labelled Audio Tagging with Attention Neural Networks](https://arxiv.org/pdf/1903.00765.pdf)
    + _Weakly labeled audio_ refers to when you have a label about the presence or absence of a feature, but you don't have the onset or offset time. That's the case for the AudioSet data more broadly, but may also be the case for some of the HomeBank stuff. This paper proposes a solution for dealing with that issue.


## Code

+ Information on the [Google AudioSet](http://research.google.com/audioset/download.html) dataset, including links to the labels alone ([balanced training set](http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/balanced_train_segments.csv), [unbalanced training set](http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/unbalanced_train_segments.csv), [evaluation set](http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/eval_segments.csv)) or to the features dataset.
+ Link to VGGish in Google's [pre-trained tensorflow models](https://github.com/tensorflow/models/tree/master/research/audioset/vggish) repo
+ [VGGish demo notebook in Colab](https://colab.research.google.com/drive/1TbX92UL9sYWbdwdGE0rJ9owmezB-Rl1C?usp=sharing)
    * I can't quite get it to work - it's not passing the smoke test, largely because it can't seem to FIND the smoke test module - but it's an interesting overview of how working with the VGGish pretrained model actually proceeds.