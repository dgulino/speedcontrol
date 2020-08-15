#!/bin/bash
/bin/kill -INT $(cat /opt/speedcontrol/speedcontrol.pid)
rm /opt/speedcontrol/speedcontrol.pid
