# Change the permissions on the ts_github_key
sudo chmod 600 ~/.ssh/ts_github_key

# Add the GitHub credentials to the ssh-agent
eval `ssh-agent -s`
ssh-add ~/.ssh/ts_github_key

# Change the permissions on the ts_github_key
# sudo chmod 600 ~/.ssh/ts_github_key

# Create the space where the GitHub repo will live
sudo mkdir /home/projects
sudo ln -s /home/projects ~/projects

# Ensure it is executable by everyone, otherwise the git commands won't work
sudo chmod 777 /home/projects
cd projects
git clone git@github.com:TSSlade/teacherprints.git
chmod -R 777 /home/projects/teacherprints
cd ~

# Create the spaces where the Miniconda installation and assets will go
sudo mkdir -m 777 /opt/miniconda3
sudo mkdir -m 777 /home/software-assets/

# Go get Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
mv Miniconda3-latest-Linux-x86_64.sh /home/software-assets/

# Install it in the /opt/ folder
bash /home/software-assets/Miniconda3-latest-Linux-x86_64.sh -p /opt/miniconda3 -f

source /opt/miniconda3/bin/activate
conda update -n base -c defaults conda

###### For each user ######
printf "\n>> Would you like to add a new user? [y] or [n] "
read -r answer
typeset -l ${answer} # Forcing the answer to lowercase
while [[ "$answer" = y ]]
do
   printf "\n>> Name of the new user: "
   read -r USERN
   UARRAY+=( $USERN )

   # Start adding users
   sudo adduser --disabled-password --gecos "" ${USERN}
   printf "\n>> Please provide a password: "
   read -s PW
   sudo echo ${USERN}:${PW} | sudo chpasswd

   # Go back home and make a symlink
   cd ~
   sudo ln -s /home/projects /home/${USERN}/projects

   # Verify the template files have been populated and that .bashrc is not bare
   sudo ls -lah /home/${USERN}
   # At this point these files^ have permissions 755, ${USERN}:${USERN}

   # Add a -conda activate- command to the end of the bash file
   sudo chmod 777 /home/${USERN}/.bashrc
   echo "source /opt/miniconda3/bin/activate" >> /home/${USERN}/.bashrc
   cat /home/${USERN}/.bashrc
   sudo chmod 644 /home/${USERN}/.bashrc

   # Add the user to the sudo-ers group
   sudo usermod -aG sudo ${USERN}

   # Make sure there's an .ssh directory that the user owns in which the authorized_keys can
   # live so they can .ssh in. NB the ts_github_key is not automatically pulled over.
   sudo mkdir /home/${USERN}/.ssh
   sudo touch /home/${USERN}/.ssh/authorized_keys
   # At this point these files^ have permissions 755, root:root

   sudo chown ubuntu:ubuntu /home/${USERN}/.ssh
   sudo chown ubuntu:ubuntu /home/${USERN}/.ssh/authorized_keys
   # At this point these files^ have permissions 755 and 644 respectively, ubuntu:ubuntu

   sudo chmod 777 /home/${USERN}/.ssh/authorized_keys
   sudo cat /home/ubuntu/.ssh/authorized_keys >> /home/${USERN}/.ssh/authorized_keys
   sudo chown -R ${USERN}:${USERN} /home/${USERN}
   sudo chmod 700 /home/${USERN}/.ssh
   sudo chmod 600 /home/${USERN}/.ssh/authorized_keys
   sudo mkdir -m 777 /home/${USERN}/.conda
   sudo chown -R ${USERN}:${USERN} /home/${USERN}/.conda
   sudo chmod -R 755 /home/${USERN}
   printf "\n>> Would you like to add another user? [y] or [n] "
   read -r answer
done

UNUM=0
while [[ ${UNUM} -lt ${#UARRAY[@]} ]]
do
   printf "\n>> User: ${UARRAY[${UNUM}]}"
   printf "\n>> Configuring [${UARRAY[${UNUM}]}]'s -base- env"
   conda env create -p /home/${UARRAY[${UNUM}]}/.conda/envs/teacherprints -f /home/projects/teacherprints/base-env.yml
   printf "\n>> Updating [${UARRAY[${UNUM}]}]'s env with -viz- tools"
   conda env update -p /home/${UARRAY[${UNUM}]}/.conda/envs/teacherprints -f /home/projects/teacherprints/viz-env.yml
   printf "\n>> Updating [${UARRAY[${UNUM}]}]'s env with -modeling- tools"
   conda env update -p /home/${UARRAY[${UNUM}]}/.conda/envs/teacherprints -f /home/projects/teacherprints/modeling-env.yml
   sudo chown 777 ${UARRAY[${UNUM}]}:${UARRAY[${UNUM}]} /home/${UARRAY[${UNUM}]}/.conda
   (( UNUM+=1 ))
done

# https://stackoverflow.com/questions/46607012/bash-script-while-loop-with-read-input-from-user
# https://stackoverflow.com/questions/2150882/how-to-automatically-add-user-account-and-password-with-a-bash-script
# https://unix.stackexchange.com/questions/242251/count-number-of-elements-in-bash-array-where-the-name-of-the-array-is-dynamic
# https://github.com/conda/conda/issues/8850
# 
# https://unix.stackexchange.com/questions/70859/why-doesnt-sudo-su-in-a-shell-script-run-the-rest-of-the-script-as-root