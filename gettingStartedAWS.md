# Getting your machine set up to work with our files in AWS

1. Download and install the [AWS CLI tool (v2)](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html). There are different versions for Windows, Mac, Linux, and Docker.
    1. You may need to configure your [IAM](https://console.aws.amazon.com/iam/) (_identity access management_) for AWS if you haven't already done so...
    2. Once you have a rootkey or keyfile of some kind, _if the folder you're keeping it in is within this Git repo_, please remember to add that folder to your `.gitignore`.

## Getting your GitHub repo set up locally with your credentials
2. You'll want to clone the GitHub repo to your local machine. For our code to work equally well on everyone's machines, you'll want to have the same kind of folder structure in place. That includes
    + having credentials stored in a `.secrets` folder...
    + that is ignored by version control and ...
    + have the same key names for the relevant credentials.
Those are not hard-and-fast requirements, but once your setup deviates from this structure the commands are not guaranteed to work out of the box.

```bash
$ git clone git@github.com:TSSlade/teacherprints.git
$ mkdir teacherprints/.secrets
$ echo ".secrets/*" >> .gitignore
$ touch teacherprints/.secrets/aws_credentials.csv; cd teacherprints/.secrets
$ echo "AWSAccessKeyId=YourKeyIDHereNoQuotes" >> aws_credentials.csv
$ echo "AWSSecretKey=YourSecretKeyHere" >> aws_credentials.csv
$ echo "nonAdmin-AccessKeyId=YourKeyIDHereNoQuotes" >> aws_credentials.csv
$ echo "nonAdmin-SecretKey=YourSecretKeyHere" >> aws_credentials.csv
$ touch .secrets/teacherprints-ec2.pem
$ vim .secrets/teacherprints-ec2.pem
```

#### Create your PEM file
1. Outside of vim, copy the contents of the PEM file into your buffer.
1. Back in vim, paste the contents of your buffer into the file.
    1. Via text insert mode:
        1. Type `i`
        1. Type `command+v` on a Mac or `control+v` on Windows to paste your buffer into vim
    1. Via normal mode:
        1. Type `command+shift+v` on a Mac or `TBD` on Windows to paste your buffer into vim
1. Write the file to disc: type `:w!`
1. Quit vim: type `:q` (`:q!` to quit without saving)

A little bit about vim for reference [here](https://irian.to/blogs/introduction-to-vim-modes/).

You'll need to make sure that your .pem file isn't publicly viewable for SSH to work. So next execute

```bash
$ chmod 400 .secrets/teacherprints-ec2.pem
```

## Accessing the AWS workspace from your machine
For the moment, we'll have a shared AWS EC2 instance that we SSH into for the purposes of working on a more powerful machine than our own laptops.

If you have followed the instructions above about structuring your `.secrets` folder to contain the necessary credentials, the code below _should_ work as-is with only the indicated modifications. If it doesn't, please let me know.

1. Verify the EC2 instance you're targeting is, indeed, up and running. You can do this via the `Instance Console` in AWS.
    1. You'll need to have signed in to the [AWS Console](https://aws.amazon.com/). Remember:
1. If you run into some trouble, AWS documentation on connecting your instance via the command line [is here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html).

```bash
# From within the teacherprints root folder
$ ssh -i ".secrets/teacherprints-ec2.pem" YourUserNameHere@ec2-18-222-196-16.us-east-2.compute.amazonaws.com
```

### To create a new user

By default, the `YourUserNameHere` value for an EC2 Ubuntu instance is `ubuntu`. It's best practice to have individual usernames for different users, though, so that's what we'll do. If the instructions below (cribbed from the [AWS documentation here](https://aws.amazon.com/premiumsupport/knowledge-center/new-user-accounts-linux-instance/)) is confusing, please reach out.

**N.B.**: Usernames have already been created for the `teacherprints` core team members. The below is only necessary if you want to create another one.

```bash
# From any user within the superusers group (sudo-enabled)
# Create a new user; if no password desired append `--disabled-password`
# Not recommended to disable password for future sudo-enabled users
$ sudo adduser NewUserName
# Add the user to the sudo usergroup
$ sudo usermod -aG NewUserName
# Change to the NewUserName
$ sudo su - NewUserName
# Create a space for the authorized keys to live and add the public key
$ mkdir .ssh
$ chmod 700 .ssh
$ touch .ssh/authorized_keys
$ chmod 600 .ssh/authorized_keys
$ cat >> .ssh/authorized_keys
# `cat` is now ready to accept input from your buffer.
# Copy the public key into your buffer and `command+v` or `ctrl+v` to paste
# Input the `enter` key to terminate the line
# Input `ctrl+d` to tell cat you're done making inputs
```

Once the user has logged in as themselves, they should change their sudo pw

```bash
# While logged in as yourself
$ passwd
# Enter your old password to verify
# Enter your new password twice
```
