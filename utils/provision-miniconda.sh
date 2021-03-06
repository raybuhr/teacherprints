#! /usr/bin/bash
# Run this from within the home folder of the root (ubuntu) user

u_flag=''
l_flag=''
a_flag=''
files=''
user="$USER"

verbose='false'
loc='/home/software-assets'

print_usage() {
  printf "Usage: ..."
}

while getopts 'u:l:va' flag; do
  case "${flag}" in
    u) u_flag='true';
            user="${OPTARG}"; echo ">> User [$user]" ;;
    l) l_flag='true';
            loc="${OPTARG}"; echo ">> Dir [$loc]" ;;
    a) a_flag='true' ;;
    # f) files="${OPTARG}" ;;
    # v) verbose='true' ;;
    *) print_usage
       exit 1 ;;
  esac
done

# Confirming the parameters we've passed
echo ">> User [$user] will install Miniconda from [$loc]"

# This silently installs the Miniconda application to the user's $HOME
# sudo -i -u $user $loc/Miniconda3-latest-Linux-x86_64.sh -b -f

# This shortcuts the need for the user to run `$ conda init` and then logout/back in
# the first time they login as user
# echo ">> Linking root's profile.d to [$user]'s profile.d"
# sudo ln -s /etc/profile.d/conda.sh /home/$user/miniconda3/etc/profile.d/conda.sh
# sudo ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh

if a_flag=='true'; then
    echo "\n>> Adding to -activate conda- to user's .bashrc..."
    # su - $user source /opt/miniconda3/bin/activate
    sudo chmod 777 /home/$user/.bashrc
    # sudo printf "\nconda activate" >> /home/$user/.bashrc
    echo "source /opt/miniconda3/bin/activate" >> /home/$user/.bashrc
    sudo chmod 644 /home/$user/.bashrc
fi

# References:
# https://askubuntu.com/questions/849470/how-do-i-activate-a-conda-environment-in-my-bashrc
# https://stackoverflow.com/questions/7069682/how-to-get-arguments-with-flags-in-bash/21128172
# https://tecadmin.net/tutorial/bash-scripting/bash-command-arguments/
# https://docs.anaconda.com/anaconda/install/silent-mode/
