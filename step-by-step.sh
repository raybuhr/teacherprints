# Add the GitHub credentials to the ssh-agent
eval `ssh-agent -s`
ssh-add ~/.ssh/ts_github_key

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
echo "Would you like to add a new user? [y] or [n]"
read -r answer
typeset -l ${answer} # Forcing the answer to lowercase
while [[ "$answer" = y ]]
do
   echo "Name of the new user: "
   read -r USERN
   UARRAY+=( $USERN )
   # Start adding users
   sudo adduser --disabled-password --gecos "" ${USERN}
   echo "Please provide a password: "
   read -s PW
   sudo echo ${USERN}:${PW} | sudo chpasswd
   # Go back home and make a symlink
   cd ~
   ln -s /home/projects /home/${USERN}/projects
   # Verify the template files have been populated and that .bashrc is not bare
   ls -lah /home/${USERN}
   # Add a -conda activate- command to the end of the bash file
   sudo chmod -R 777 /home/${USERN}
   echo "source /opt/miniconda3/bin/activate" >> /home/${USERN}/.bashrc
   cat /home/${USERN}/.bashrc
   sudo usermod -aG sudo ${USERN}
   echo "Would you like to add another user? [y] or [n]"
   read -r answer
done

UNUM=0
while [[ ${UNUM} -lt ${#UARRAY[@]} ]]
do
   echo ">> User: ${UARRAY[${UNUM}]}"
   echo: ">> Configuring [${UARRAY[${UNUM}]}]'s -base- env"
   conda env create -p /home/${UARRAY[${UNUM}]}/.conda/envs/teacherprints -f /home/projects/teacherprints/base-env.yml
   echo: ">> Updating [${UARRAY[${UNUM}]}]'s env with -viz- tools"
   conda env update -p /home/${UARRAY[${UNUM}]}/.conda/envs/teacherprints -f /home/projects/teacherprints/viz-env.yml
   echo: ">> Updating [${UARRAY[${UNUM}]}]'s env with -modeling- tools"
   conda env update -p /home/${UARRAY[${UNUM}]}/.conda/envs/teacherprints -f /home/projects/teacherprints/modeling-env.yml
   (( UNUM+=1 ))
done

# https://stackoverflow.com/questions/46607012/bash-script-while-loop-with-read-input-from-user
# https://stackoverflow.com/questions/2150882/how-to-automatically-add-user-account-and-password-with-a-bash-script
# https://unix.stackexchange.com/questions/242251/count-number-of-elements-in-bash-array-where-the-name-of-the-array-is-dynamic