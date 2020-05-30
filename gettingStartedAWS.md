# Getting your machine set up to work with our files in AWS

1. Download and install the [AWS CLI tool (v2)](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html). There are different versions for Windows, Mac, Linux, and Docker.
    1. You may need to configure your [IAM](https://console.aws.amazon.com/iam/) (_identity access management_) for AWS if you haven't already done so...
    2. Once you have a rootkey or keyfile of some kind, _if the folder you're keeping it in is within this Git repo_, please remember to add that folder to your `.gitignore`.


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
