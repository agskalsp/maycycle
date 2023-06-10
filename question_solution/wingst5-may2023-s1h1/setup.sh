#!/bin/sh
sudo apt update 
sudo apt install python3-pip --fix-missing -y
pip3 install -r requirements.txt
sudo apt install docker-compose -y
sudo apt install docker.io -y
 
