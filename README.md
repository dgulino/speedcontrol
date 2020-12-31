# speedcontrol
Web interface to control Speedify connection on Linux.

### Instructions for Raspberry Pi OS (raspian)

## Install OS dependencies
	sudo apt install python3
	sudo apt install uwsgi-plugin-python3

## Create user and directories
	sudo useradd speedcontrol
	sudo mkdir /home/speedcontrol
	sudo mkdir /var/log/speedcontrol
	sudo mkdir /var/run/speedcontrol
	sudo mkdir /opt/speedcontrol
	sudo chown speedcontrol: /var/log/speedcontrol /var/run/speedcontrol /opt/speedcontrol /home/speedcontrol

## Get code
	sudo su - speedcontrol
	cd /opt
	git clone $git_url

## Install python dependencies
        cd /opt/speedcontrol
	python3 -m venv speedcontrol_venv
	source /opt/speedcontrol/speedcontrol_venv/bin/activate
	pip3 install pipenv
	pipenv install

## Enable and start process
	sudo cp speedcontrol.service /lib/systemd/system/
	sudo systemctl enable speedcontrol
	sudo systemctl start speedcontrol

## Use
	http://$address:5000

## Crontab
	#To auto reconnect in the morning:
        sudo su -
	crontab -e
        #Add line:
        0 4 * * * /usr/share/speedify/speedify_cli connect
	
