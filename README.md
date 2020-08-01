# speedcontrol
Web interface to control Speedify connection on Linux.

### Instructions for Raspberry Pi OS (raspian)

## Install OS dependencies
sudo apt install python3
sudo apt install uwsgi-plugin-python3

## Create user and directories
sudo useradd speedcontrol -D
sudo mkdir /home/speedcontrol
sudo mkdir /var/log/speedcontrol
sudo mkdir /var/run/speedcontrol
sudo mkdir /opt/speedcontrol
sudo chown speedcontrol: /var/log/speedcontrol /var/run/speedcontrol /opt/speedcontrol

## Get code
git clone speedcontrol

## Install python dependencies
python3 -m venv speedcontrol_venv
source /opt/speedcontrol/speedcontrol_venv/bin/activate
pip3 install pipenv
pipenv install

## Enable and start process
sudo cp speedcontrol.init /etc/init.d/speedcontrol
sudo systemctl enable speedcontrol
sudo systemctl start speedcontrol

## Use
http://$address:5000
