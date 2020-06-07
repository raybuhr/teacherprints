#! /usr/bin/bash
# Run this from within the home folder of the root (ubuntu) user
# $# - number of arguments passed to the script
# $1 to $n - argument position. Note for >1 digit n need to enclose in {} as ${10}
# $@ - all arguments as a 0-indexed array

# Let's add a password to the default -ubuntu- user
# echo ">> This creates a password for the root user on first run:"
# sudo passwd # make new password -ubuntu-

for newuser in $@
do
    # Create the new user; don't require a password at that stage
    sudo useradd --disabled-password --gecos "" $newuser

    # Change the password for that user
    echo "\n>> Make a password for the user we just created:"
    sudo passwd $newuser

    # Add that user to the sudo-ers group
    echo "\n>> Adding the new user to the sudo-ers group"
    sudo usermod -aG sudo $newuser
    sudo usermod -aG group_tt $newuser

    # Change to that user
    echo "\n>> Verifying the new user exists and we can see their files"
    sudo -i -u $newuser echo "++ Executing as $USER"
    sudo -i -u $newuser ls -lah

    # Go back over to the ubuntu user
    echo "\n>> All done...now executing as $USER"
    # exit

    # Copy over the authentication public key so they can SSH in
    echo "\n>> Copying over the necessary public keys so the new user can SSH in"
    sudo mkdir -p /home/$newuser/.ssh
    sudo cp ~/.ssh/authorized_keys /home/$newuser/.ssh/authorized_keys
    sudo chmod 700 /home/$newuser/.ssh
    sudo chmod 644 /home/$newuser/.ssh/authorized_keys
    # Wrap up
    echo "\n>> All done! Try switching over to the new user via 'su - $newuser'"
done

# References:
# https://tecadmin.net/tutorial/bash-scripting/bash-command-arguments/
# https://tecadmin.net/tutorial/bash-scripting/bash-command-arguments/
# https://stackoverflow.com/questions/5474732/how-can-i-add-a-help-method-to-a-shell-script/5476278