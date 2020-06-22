conda update -n base -c defaults conda
conda env create -f /home/projects/teacherprints/base-env.yml
conda env update -f /home/projects/teacherprints/viz-env.yml -n teacherprints
conda env update -f /home/projects/teacherprints/modeling-env.yml -n teacherprints
