conda update -n base -c defaults conda
conda env create -f base-env.yml
conda env update -f viz-env.yml -n teacherprints
conda env update -f modeling-env.yml -n teacherprints
