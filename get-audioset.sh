#! /usr/bin/bash
# Make the data/audioset folder if it's not previously there
mkdir -p ../data/audioset
mkdir reference

# Go get the CSVs
curl http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/eval_segments.csv > ../data/audioset/eval_segments.csv
curl http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/balanced_train_segments.csv > ../data/audioset/balanced_train_segments.csv
curl http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/unbalanced_train_segments.csv > ../data/audioset/unbalanced_train_segments.csv

# Verify the line counts of each
seq  -f "+" -s '' 20
echo '\nLine counts:'
echo '\t eval_segments contained' $(cat ../data/audioset/eval_segments.csv | wc -l) 'records'
echo '\t balanced_segments contained' $(cat ../data/audioset/balanced_train_segments.csv | wc -l) 'records'
echo '\t unbalanced_segments contained' $(cat ../data/audioset/unbalanced_train_segments.csv | wc -l) 'records'
seq  -f "+" -s '' 20; echo '\n'

# Go get the QA data
curl http://storage.googleapis.com/us_audioset/youtube_corpus/v1/qa/qa_true_counts.csv > ../data/audioset/qa_true_counts.csv
curl http://storage.googleapis.com/us_audioset/youtube_corpus/v1/qa/rerated_video_ids.txt > ../data/audioset/rerated_video_ids.txt

# Inspect a portion of the files
seq  -f "+" -s '' 20
echo '\n-QA true counts- Line count:' $(cat ../data/audioset/qa_true_counts.csv | wc -l) 'records'
echo 'A sample:'
head -5 ../data/audioset/qa_true_counts.csv
seq  -f "-" -s '' 20
echo '\n-Rerated video ID- line count:' $(cat ../data/audioset/rerated_video_ids.txt | wc -l) 'records'
echo 'A sample:'
head -5 ../data/audioset/rerated_video_ids.txt
seq  -f "+" -s '' 20; echo '\n'

# Go get the ontology so we can map the codes to human-readable labels
curl https://raw.githubusercontent.com/audioset/ontology/master/ontology.json > ../data/audioset/audioset-ontology.json
cat  ../data/audioset/audioset-ontology.json | jq -r '.[] | [.id, .name] | @csv' > reference/audioset-human-readable-id-mapping.csv

# Inpect a portion of the ontology
seq  -f "+" -s '' 20; echo '\n'
echo 'The raw ontology:'
jq '[.[0], .[1]]' ../data/audioset/audioset-ontology.json
seq  -f "-" -s '' 20; echo '\n'
echo 'The simplified mapping of IDs to human-readable labels:'
cat reference/audioset-human-readable-id-mapping.csv | head -5
seq  -f "+" -s '' 20; echo '\n'