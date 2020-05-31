#! /usr/bin/bash
mkdir -p ../data/audioset
curl http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/eval_segments.csv > ../data/audioset/eval_segments.csv
curl http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/balanced_train_segments.csv > ../data/audioset/balanced_train_segments.csv
curl http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/unbalanced_train_segments.csv > ../data/audioset/unbalanced_train_segments.csv

# Verifying the line counts of each
seq  -f "+" -s '' 20
echo '\nTo verify:'
echo '\t eval_segments contained' $(cat ../data/audioset/eval_segments.csv | wc -l) 'records'
echo '\t balanced_segments contained' $(cat ../data/audioset/balanced_train_segments.csv | wc -l) 'records'
echo '\t unbalanced_segments contained' $(cat ../data/audioset/unbalanced_train_segments.csv | wc -l) 'records'
seq  -f "+" -s '' 20