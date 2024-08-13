#!/bin/bash
echo "please remember to change (dollar sign)HOMEDIRECTORY with your real home directory" 
echo gaining ownership
chown -R $USER:$USER ~/bin/lnknk/
echo install zsh,xonsh,py-venv,pip
sudo apt install -y zsh
sudo apt install -y xonsh
sudo apt install -y python3-venv
sudo apt install -y python3-pip
cd ~/bin/lnknk
echo creating venv and installing required packages
python -m venv ~/venv/
sudo apt install -y tk
