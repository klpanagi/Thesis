#!/bin/bash

## Helper functions to get the shell used for this login user
_get_shell () {
  local shell_path=$(getent passwd $LOGNAME | cut -d: -f7)
  local shell=""
  if [[ "$shell_path" =~ "zsh" ]]; then
    shell="ZSH"
  elif [[ "$shell_path" =~ "bash" ]]; then
    shell="BASH"
  else
    echo -e "Not recognized shell"
    exit 1
  fi
  echo "$shell"
}

_get_shell_rcfile () {
  local _shell=$(_get_shell)
  local _shell_rc_file=""
  if [[ "$_shell" == "ZSH" ]]; then
    _shell_rcfile="${HOME}/.zshrc"
  elif [[ "$_shell" == "BASH" ]]; then
    _shell_rcfile="${HOME}/.bashrc"
  fi
  echo "$_shell_rcfile"
}

## -------------------------------------------------------------

URL="http://developer.download.nvidia.com/embedded/L4T/r21_Release_v3.0/cuda-repo-l4t-r21.3-6-5-prod_6.5-42_armhf.deb"

cd /tmp
wget ${URL}

sudo dpkg -i cuda-repo-l4t-r21.3-6-5-prod_6.5-42_armhf.deb
sudo apt-get -y update
sudo apt-get -y install cuda-toolkit-6-5

SHELL_RC_FILE=$(_get_shell_rcfile)
echo $SHELL_RC_FILE

if [ -n "$ZSH_VERSION" ]; then
  SHELL_RC_FILE="~/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
  SHELL_RC_FILE="~/.bashrc"
else
  echo -e "Not supported SHELL for this installation"
  exit 1
fi


echo "# Add CUDA bin & library paths:" >> $SHELL_RC_FILE
grep -q "export PATH=.*/usr/local/cuda-6.5/bin" $SHELL_RC_FILE || echo "export PATH=/usr/local/cuda-6.5/bin:$PATH" >> $SHELL_RC_FILE

grep -q "export LD_LIBRARY_PATH=/usr/local/cuda-6.5/lib" $SHELL_RC_FILE || echo "export LD_LIBRARY_PATH=/usr/local/cuda-6.5/lib:$LD_LIBRARY_PATH" >> $SHELL_RC_FILE

source $SHELL_RC_FILE


