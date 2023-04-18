#!/bin/bash
# written by Anant Shukla
sudo yum update -y
sudo yum install git -y
git clone https://github.com/anantshukla93/Fake-Apache-Log-Generator.git
mkdir /tmp/logs
sudo yum install pip -y
sudo pip install -r ./Fake-Apache-Log-Generator/requirements.txt
sudo pip3 install boto3
chmod u+x ~/Fake-Apache-Log-Generator/apache-fake-log-gen.py
