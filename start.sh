#!/bin/bash
cd /opt/speedcontrol
source /opt/speedcontrol/speedcontrol_venv/bin/activate
uwsgi -i uwsgi-service.ini
