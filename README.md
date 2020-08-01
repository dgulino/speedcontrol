sudo apt install python3
sudo apt install uwsgi-plugin-python3

sudo useradd speedcontrol -D
sudo mkdir /home/speedcontrol
sudo mkdir /var/log/speedcontrol
sudo mkdir /var/run/speedcontrol
sudo mkdir /opt/speedcontrol
sudo chown speedcontrol: /var/log/speedcontrol /var/run/speedcontrol /opt/speedcontrol

git clone speedcontrol

python3 -m venv speedcontrol_venv
source /opt/speedcontrol/speedcontrol_venv/bin/activate
pip3 install pipenv
pipenv install

sudo cp speedcontrol.init /etc/init.d/speedcontrol
sudo systemctl enable speedcontrol
sudo systemctl start speedcontrol
