# Getting your machine set up to work with our files in AWS

## [Getting your GitHub repo set up locally with your credentials](#credentials-in-secrets)

1. You'll want to clone the GitHub repo to your local machine. For our code to work equally well on everyone's machines, you'll want to have the same kind of folder structure in place. That includes
    + having credentials stored in a `.secrets` folder...
    + that is ignored by version control and ...
    + have the same key names for the relevant credentials.
Those are not hard-and-fast requirements, but once your setup deviates from this structure the commands are not guaranteed to work out of the box.

```bash
$ git clone git@github.com:TSSlade/teacherprints.git

$ mkdir teacherprints/.secrets

$ echo ".secrets/*" >> .gitignore

$ touch teacherprints/.secrets/aws_credentials.csv; cd teacherprints/.secrets

$ echo "nonAdmin-AccessKeyId=YourOtherKeyIDHereNoQuotes" >> aws_credentials.csv

$ echo "nonAdmin-SecretKey=YourOtherSecretKeyHereNoQuotes" >> aws_credentials.csv

$ touch .secrets/teacherprints-ec2.pem

$ vim .secrets/teacherprints-ec2.pem
```

### [Create your PEM file](#create-pem-file)

These instructions assume you have not already gotten your .pem file set up on your own. If you've already gotten it squared away and appropriately saved in the `.secrets` folder, you can skip this section.

**NB:** This is to be done on the physical computer you are working with. You do not need to do this in the cloud unless you're planning to SSH from one cloud machine to another cloud machine.

1. Outside of vim, copy the contents of the PEM file (that I shared in Slack) into your buffer.
1. Back in vim, paste the contents of your buffer into the file.
    1. Via text insert mode:
        1. Type `i`
        1. Type `command+v` on a Mac or `control+v` on Windows to paste your buffer into vim
    1. Via normal mode:
        1. Type `command+shift+v` on a Mac or `TBD` on Windows to paste your buffer into vim
1. Write the file to disc: type `:w!`
1. Quit vim: type `:q` (`:q!` to quit without saving)

A little bit about vim for reference [here](https://irian.to/blogs/introduction-to-vim-modes/).

For SSH to use your .pem file we'll need to make sure that it not only isn't _publicly_ viewable, even your own user can only read it (but not write or execute). So next execute the command

```bash
$ chmod 400 .secrets/teacherprints-ec2.pem
```

## [Accessing the AWS workspace from your machine](#ssh-to-aws)

For the moment, we'll have a shared AWS EC2 instance that we SSH into for the purposes of working on a more powerful machine than our own laptops.

If you have followed the instructions above about structuring your `.secrets` folder to contain the necessary credentials, the code below _should_ work as-is with only the indicated modifications. If it doesn't, please let me know.

1. Verify the EC2 instance you're targeting is, indeed, up and running. You can do this via the `Instance Console` in AWS.
    1. You'll need to have signed in to the [AWS Console](https://aws.amazon.com/). Remember: you're signing in using your _IAM_ credentials for our shared workspace, _not_ your 'root' credentials (i.e., the ones you use to do AWS things unrelated to this project.)
1. If you run into some trouble, AWS documentation on connecting your instance via the command line [is here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html).

```bash
# From within the teacherprints root folder
$ ssh -i ".secrets/teacherprints-ec2.pem" YourUserNameHere@ec2-3-23-90-91.us-east-2.compute.amazonaws.com`
```

### [To create a new user within the cloud instance](#new-cloud-user)

By default, the `YourUserNameHere` value for an EC2 Ubuntu instance is `ubuntu`. It's best practice to have individual usernames for different users, though, so that's what we'll do. If the instructions below (cribbed from the [AWS documentation here](https://aws.amazon.com/premiumsupport/knowledge-center/new-user-accounts-linux-instance/)) are confusing, please reach out.

**N.B.**: Usernames have already been created for the `teacherprints` core team members. The below is only necessary if you want to create another one.

```bash
# From any user within the superusers group (sudo-enabled)
# Create a new user; if no password desired append `--disabled-password`
# Not recommended to disable password for future sudo-enabled users
$ sudo adduser NewUserName

# Add the user to the sudo usergroup
$ sudo usermod -aG sudo NewUserName

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

## [Setting up your SSH config to make it easier to connect to the remote machine](#ssh-config-file)

If you intend to be SSHing into multiple remote machines, it may make sense to set up a `config` file within your `~/.ssh` folder that allows you to initiate an SSH session with a full suite of configurations without needing to type them in yourself.

**NB:** These are steps to be executed on the physical device you are interacting with. You do not need to do this on the cloud machine unless you are planning to SSH from there into other machines.

Our references for this section are posts from
+ Linuxize ([_Using the SSH Config File_](https://linuxize.com/post/using-the-ssh-config-file/))
+ CiberCiti.biz ([_OpenSSH Config File Examples_](https://www.cyberciti.biz/faq/create-ssh-config-file-on-linux-unix/))
+ [_SSH Can Do That? Productivity Tips for Working with Remote Servers_](http://blogs.perl.org/users/smylers/2011/08/ssh-productivity-tips.html)
+ Ubuntu's official documentation ([_SSH/OpenSSH/PortForwarding_](https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding))

1. If it does not already exist, create a `config` file within your `.ssh` folder.
    1. The `.ssh` folder will exist within your `HOME` if you have ever previously initiated an SSH session.
    1. If it's not there, create it first (`$ mkdir ~/.ssh`).
    ```bash
    $ touch ~/.ssh/config

    # update permissions so only the user can read, can write, can't execute
    $ chmod 600 ~/.ssh/config
    ```
1. Your config file will be laid out with keys (e.g., `Host`) separated from the values they take (e.g., `dev`) by a space: `Host dev`.
1. All the configurations that go together are grouped in what is called a _stanza_. It is good practice to indent all lines of the stanza save the first to make it clearer how everything fits together.
1. The file is read/interpreted from top to bottom. The first stanza matching the command you are issuing is the one that will take precedence.
1. The relevant portion of mine looks like this:
    ```ssh-config
    # The name of the host you'll invoke with $ ssh <whatever>
    Host teacherprints
        # The Elastic IP that AWS will keep pointing at our EC2 instance
        Hostname 3.23.90.91
        # The username you're logging in with
        User tslade
        # The port to connect on
        Port 22
        IdentityFile path/to/my/pemfile/MyPemFile.pem
        GatewayPorts yes
        # Mapping ports for Jupyter, etc.
        LocalForward 8888 127.0.0.1:8888
        LocalForward 8889 127.0.0.1:8889
        LocalForward 8890 127.0.0.1:8890
        LocalForward 8891 127.0.0.1:8891
        LocalForward 8896 127.0.0.1:8896
        # Keeps the remote server alive for a while - helps if your connectivity is spotty
        ControlPersist 4h
        # Local portion of a config setting to allow GUIs to run off the remote server
        ForwardX11 yes
    ```
As a result of the above, now instead of typing in
```bash
$ ssh -i ".secrets/teacherprints-ec2.pem" tslade@ec2-3-23-90-91.us-east-2.compute.amazonaws.com
```
I can simply invoke
```bash
$ ssh teacherprints
```
...and I'm off to the races!

While defining my own `.ssh/config` file, I found these resources helpful:
+ [_Can tmux pane remote ssh-connection_](https://stackoverflow.com/questions/10537206/can-tmux-pane-remote-ssh-connection)
+ [_Run tmux on ssh login_](https://unix.stackexchange.com/questions/552614/run-tmux-on-ssh-login)

## [Working with shared folders from within our own HOME directories](#shared-folders-home)

The EC2 instance has a structure as follows:

```bash
$ cd /
$ tree -L 1
    .
    ├── bin
    ├── boot
    ├── dev
    ├── etc
    ├── home # <-- This is where the magic happens
    ├── lib
    ├── lib64
    ├── media
    ├── meta
    ├── mnt
    ├── opt
    ├── proc
    ├── root
    ├── run
    ├── sbin
    ├── snap
    ├── srv
    ├── sys
    ├── tmp
    ├── usr
    ├── var
    └── writable

$ tree -L 1 home
    home
    ├── ajacobson
    ├── kdarnell
    ├── lmoore
    ├── projects # <-- This is where the GitHub repo and shared files will live
    ├── tslade
    └── ubuntu

$ tree -L 1 home/projects
    home/projects
    └── teacherprints
```

It would be a bit of a pain to always need to back up out your user's `HOME` directory to get to the relevant folders. If you create a symlink to the folder within your own `HOME`, it can be a bit easier to work with.

```bash
~$ pwd
# /home/tslade

# Make a symbolic link to the common folder and name it something helpful
~$ ln -s /home/projects projects
~$ ls -l
# total 4
# drwxr-xr-x 3 tslade tslade 4096 May 31 04:12 snap
# lrwxrwxrwx 1 tslade tslade   14 May 31 04:45 projects -> /home/projects

~$ cd projects

# Let's verify it contains what we expect it to
~/projects$ ls -l
# total 4
# drwxrwxr-x 5 tslade tslade 4096 May 31 04:31 teacherprints

# If all worked as planned, the output of the next command should match the above
~/projects$ ls -l /home/projects
# total 4
# drwxrwxr-x 5 tslade tslade 4096 May 31 04:31 teacherprints

# It does! Success.
```

## [Other notes](#other-notes)

In the event you use SSH for communication with GitHub and you're not able to make commits to the repo or clone it, the instructions at [_How to use SSH keys for authentication_](https://upcloud.com/community/tutorials/use-ssh-keys-authentication/) can help sort you out.

## [Standing up a new instance via CLI](#new-instance-cli)

If we need to tear down an instance and start it back up again, we don't want to have to reconfigure everything by hand in the console. That's for a couple of reasons.

1. It's not super straightforward to do in the first place, so odds are good you'll have to re-teach yourself how to do it each time. (Unless it's part of your day to day, in which case...you do you.)
2. It takes time and concerted attention, both of which you might prefer to be spending on something else.
3. It's not reproducible. (You might have done something _sliiiiiightly_ differently somewhere along the way, and if you didn't document that...you won't be able to get back to the configuration you needed for everything to work just right.)

So we'll go ahead and try to get our AWS config squared away using the _AWS CLI_ tool. That way we can keep our config files under version control and just execute them when we need to stand up a new server instance.

### [Gather your tools](#gather-cli-tools)

1. You'll need to download and install the [AWS CLI tool (v2)](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html). There are different versions for Windows, Mac, Linux, and Docker.
2. If you have not (or your admin has not) already configured your [IAM](https://console.aws.amazon.com/iam/) (_identity access management_) user profile for the group in question, you'll need to do that.
3. Follow [the instructions above](#credentials-in-secrets) about making sure your credentials aren't exposed in version control.

We're going to be following [AWS' instructions](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) for configuring the command line. Here's where you'll use the _access key id_ and _secret access key_ you saved in your `.secrets/aws_credentials.csv` [earlier](#credentials-in-secrets).

```bash
$ aws configure
AWS Access Key ID [None]: PasteYourAccessKeyIdHere
AWS Secret Access Key [None]: PasteYourSecretHere
Default region name [None]: us-west-2
Default output format [None]: json
```

When you execute the commands above, you'll be making changes to the files stored at
```bash
### credentials
~/.aws/credentials                 # linux
C:\Users\USERNAME\.aws\credentials # windows
### configuration
~/.aws/config                      # linux
C:\Users\USERNAME\.aws\config      # windows
```
Per the instructions:
> CLI credentials file – This is one of the files that is updated when you run the command aws configure. The file is located at ~/.aws/credentials on Linux or macOS, or at C:\Users\USERNAME\.aws\credentials on Windows. This file can contain the credential details for the default profile and any named profiles.

> CLI configuration file – This is another file that is updated when you run the command aws configure. The file is located at ~/.aws/config on Linux or macOS, or at C:\Users\USERNAME\.aws\config on Windows. This file contains the configuration settings for the default profile and any named profiles.

In the event you use SSH for communication with GitHub and you're not able to make commits to the repo or clone it, the instructions at [_How to use SSH keys for authentication_](https://upcloud.com/community/tutorials/use-ssh-keys-authentication/) can help sort you out.

At some later point we may need to enable multifactor authentication (MFA) to ensure the security settings are appropriately tight. The AWS instructions [discuss configuring MFA for CLI work](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html).

Generally speaking, we're going to want to read in our configurations from a file rather than passing them to the CLI in realtime. For those purposes the `$ aws [service-name] [command-name] --generate-cli-skeleton yaml-input` command will be useful. (It is also possible to use the [json-input option](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-skeleton.html), but I think yaml will be more readable.) The discussion of the `DryRun` configuration flag is especially relevant for us.

A few important troubleshooting points:

+ Never forget that the region you're in matters. If you're getting unexpected errors on a simple command that _should_ be working, verify that the region your profile is using matches the profile in which the resource you're consulting or acting upon is residing. e.g., [_Create security group at CLI, getting `InvalidVpcID.NotFound The vpc ID does not exist`_](https://stackoverflow.com/questions/58359924/create-security-group-at-cli-getting-invalidvpcid-notfound-the-vpc-id-does-not)

```bash
$ aws ec2 describe-security-groups --group-ids [id here] --region [region here] > vpc-security-group.yml
```

In the event you use SSH for communication with GitHub and you're not able to make commits to the repo or clone it, the instructions at [_How to use SSH keys for authentication_](https://upcloud.com/community/tutorials/use-ssh-keys-authentication/) can help sort you out.

