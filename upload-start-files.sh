#!/bin/bash
# Run this from within the home folder of the root (ubuntu) user

ipAdd=''
verbose=ßfalse
pem_loc=.secrets/teacherprints-ec2.pem
pro_loc=provisioning.sh
gh_loc=~/.ssh/id_rsa
targName=ts_github_key

print_usage() {
  printf "Usage: ..."
}

while getopts 'i:p:g:t:r:' flag; do
  case "${flag}" in
    i) i_flag='true';
            ipAdd="${OPTARG}"; echo ">> Instance: [${ipAdd}]" ;;
    p) p_flag='true';
            pem_loc="${OPTARG}"; echo ">> Pem file: [${pem_loc}]" ;;
    r) r_flag='true';
            pro_loc="${OPTARG}"; echo ">> Provisioning file: [${pro_loc}]";;
    g) g_flag='true';
            gh_loc="${OPTARG}"; echo ">> GitHub key: [${gh_loc}]" ;;
    t) t_flag="${OPTARG}"; echo ">> New name for GHK: [${targName}]" ;;
    v) verbose='true' ;;
    *) print_usage
       exit 1 ;;
  esac
done

echo ">> Uploading the GitHub key via: "
echo "\tscp -i ${pem_loc} ${gh_loc} ubuntu@${ipAdd}:~/.ssh/${targName}"
scp -i ${pem_loc} ${gh_loc} ubuntu@${ipAdd}:~/.ssh/${targName}
echo ">> Uploading the provisioning script via: "
echo "\tscp -i ${pem_loc} ${pro_loc} ubuntu@${ipAdd}:provisioning.sh"
scp -i ${pem_loc} ${pro_loc} ubuntu@${ipAdd}:provisioning.sh

# Logging in
ssh -i ${pem_loc} ubuntu@${ipAdd}

# https://unix.stackexchange.com/questions/536794/how-to-use-variable-in-scp-command-for-multiple-files