npm install -g node-gyp
npm install printer --msvs_version=2013

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
