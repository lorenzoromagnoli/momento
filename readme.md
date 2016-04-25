
install guteprint
'sudo apt-get install printer-driver-gutenprint'

# for neopixels
# as per https://learn.adafruit.com/neopixels-on-raspberry-pi/software
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install

install graphicsmagick
sudo apt-get install graphicsmagick

install canvas dependencies
sudo apt-get install libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev build-essential g++
