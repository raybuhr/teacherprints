#! /usr/bin/bash
###############################################################################
### This script MUST be run as SUDO!!!
#
### Before you run this script, ensure you've uploaded the private key
### you will use to authenticate with our GitHub repo. In this
### script it's called -ts_github_key-
# 1. Copy/paste the instance's IP address (or the Elastic IP) and insert it
#    into the appropriate slot below (<ip-address-here>). This uploads
#    the private key necessary to interact with the GitHub repo
# $ scp -i .secrets/teacherprints-ec2.pem ~/.ssh/id_rsa \
#           ubuntu@<ip-address-here>:~/.ssh/ts_github_key
# $ scp -i .secrets/teacherprints-ec2.pem ~/.ssh/id_rsa \
#           ubuntu@ec2-18-217-32-65.us-east-2.compute.amazonaws.com:~/.ssh/ts_github_key
###
# 2. Do the same here: this uploads this file so you can execute it within
#    the instance. The lines below assumes you're working from within the top-
#    level teacherprints folder in your local GitHub repo.
#
# $ scp -i .secrets/teacherprints-ec2.pem workspace-setup.sh \
#           ubuntu@ec2-18-217-32-65.us-east-2.compute.amazonaws.com:~/workspace-setup.sh
#
# Remember to run this script as SUDO!
# $ sudo sh workspace-setup.sh
#### scp -i .secrets/teacherprints-ec2.pem .secrets/teacherprints-ec2.pem ubuntu@ec2-18-217-25-162.us-east-2.compute.amazonaws.com:ts_github_key

# Activate the ssh-agent application and add the key for GitHub
eval `ssh-agent -s`
ssh-add ~/.ssh/ts_github_key

# Create a group for the Team TeacherPrint users
sudo groupadd group_tt

# Add the current user to it
sudo usermod -aG group_tt ubuntu

### Create a new user with the following characteristics
# '-m'      : invoke the 'create home' option
# '-U'      : create a group with the user's name
# '-g'      : create with specified primary group (has to already exist)
# '-s'      : define the default shell
# '-G'      : assign the user to additional secondary groups (no spaces in options!)
# '-c'      : skip the rest of the user contact info. stuff (a.k.a. 'gecos')

sudo useradd -m -U -k -s '/bin/bash' -G sudo,group_tt -c "Tim Slade" tslade

# Verify that the user-creation worked as expected
cut -d : -f 1 /etc/passwd | sort

sudo mkdir -p /home/tslade/.ssh
sudo chown -R tslade /home/tslade
sudo cp ~/.ssh/authorized_keys /home/tslade/.ssh/authorized_keys
sudo chmod 700 /home/tslade/.ssh
sudo chmod 644 /home/tslade/.ssh/authorized_keys

# Set up the git config
git config --global user.name tt-ubuntu
git config --global user.email tim@teacherprints.org

## We're going to create all the folders we're expecting to need to
## get our users properly set up. If we're going to install miniconda
## as a multi-user application we want to put it someplace accessible
## to the whole team instead of in the default location

# sudo mkdir -m 775 /home/projects           # teacherprints repo
# sudo mkdir -m 775 /home/software-assets    # miniconda installer
# sudo mkdir -m 775 /opt/miniconda3          # shared miniconda executable

sudo mkdir /home/projects           # teacherprints repo
sudo mkdir /home/software-assets    # miniconda installer
sudo mkdir /opt/miniconda3          # shared miniconda executable

# Assign ownership of the projects folder to group_TT
sudo chgrp -R group_tt /home
sudo chgrp -R group_tt /opt
sudo chmod 770 /home
sudo chmod 770 /opt

# Create a symbolic link to the place we want to clone the
# GitHub repo to and go to it
sudo ln -s /home/projects projects
cd projects

# Clone the GitHub repo
# git clone https://github.com/TSSlade/teacherprints.git
git clone git@github.com:TSSlade/teacherprints.git

# Go back to root user's $HOME
cd ~

# Download the Miniconda file
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Move it to the folder we want to stash it in
mv Miniconda3-latest-Linux-x86_64.sh /home/software-assets

# Install miniconda
sudo sh /home/software-assets/Miniconda3-latest-Linux-x86_64.sh -p /opt/miniconda3 -f
source /opt/miniconda3/bin/activate
# conda init

# Create new users for our teammates
# sh projects/teacherprints/make-users.sh tslade kdarnell lmoore ajacobson
sh projects/teacherprints/make-users.sh cora naomi

# Make the provisioning script executable
chmod +x projects/teacherprints/provision-conda-envs.sh

# Provision each user with our conda set up
# for usern in tslade kdarnell lmoore ajacobson; do
for usern in cora naomi; do
    sh projects/teacherprints/provision-miniconda.sh -u $usern -a
    sudo -u $usern projects/teacherprints/provision-conda-envs.sh
done

# https://docs.anaconda.com/anaconda/install/multi-user/
# https://www.cyberciti.biz/tips/understanding-linux-unix-umask-value-usage.html#:~:text=The%20user%20file%2Dcreation%20mode,Symbolic%20values
# https://stackoverflow.com/questions/18599711/how-can-i-split-a-shell-command-over-multiple-lines-when-using-an-if-statement
# https://www.tecmint.com/add-users-in-linux/