#!/bin/bash
echo "Updating repositories"
sudo apt-get update 
echo "Installing depedencies"
sudo apt install -y netcat-traditional python3 pip
sudo pip3 install RPi.GPIO
echo " "
echo "Edit the config.py file with the details of the companion server then run __main__.py"