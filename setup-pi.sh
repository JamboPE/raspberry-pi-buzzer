#!/bin/bash
echo "Updating repositories"
sudo apt-get update 
echo "Installing depedencies"
sudo apt-get install -y python-rpi.gpio python3-rpi.gpio netcat
echo " "
echo "Edit the config.py file with the details of the companion server then run __main__.py"