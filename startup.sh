#!/bin/bash

python neopixel_driver.py &
python buzz_server.py &
/usr/local/bin/node server.js &

