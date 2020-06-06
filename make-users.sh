#! /usr/bin/bash
# Run this from within the home folder of the root (ubuntu) user

# Let's add a password to the default -ubuntu- user
echo ">> This creates a password for the root user on first run:"
sudo passwd # make new password -ubuntu-

# Create the new user; don't require a password at that stage
sudo adduser --disabled-password --gecos "" lmoore

# Change the password for that user
echo "\n>> Make a password for the user we just created:"
sudo passwd lmoore

# Add that user to the sudo-ers group
echo "\n>> Adding the new user to the sudo-ers group"
sudo usermod -aG sudo lmoore

# Change to that user
echo "\n>> Verifying the new user exists and we can see their files"
sudo -i -u lmoore echo "++ Executing as $USER"
sudo -i -u lmoore ls -lah

# Go back over to the ubuntu user
echo "\n>> All done...now executing as $USER"
# exit

# Copy over the authentication public key so they can SSH in
echo "\n>> Copying over the necessary public keys so the new user can SSH in"
sudo mkdir -p /home/lmoore/.ssh
sudo cp ~/.ssh/authorized_keys /home/lmoore/.ssh/authorized_keys

# Wrap up
echo "\n>> All done! Try switching over to the new user via 'su - lmoore'"


