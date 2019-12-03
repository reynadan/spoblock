# spoblock
Simple program muting audio while spotify is running ads
It's getting the current windows title and if it's not corresponding to music, sound is muted.

## Requirements

### Alsaaudio
For python3 you have to get alsaaudio manually for now.
You can install it by following the steps given below.

Make sure that gcc, python3-dev, libasound2-dev packages are installed in your machine (install them using synaptic if you are using Ubuntu).

Download and extract the following package http://sourceforge.net/projects/pyalsaaudio/files/pyalsaaudio-0.7.tar.gz/download

Go to the extracted folder and execute the following commands (Execute the commands as root or use sudo)

python3 setup.py build 
python3 setup.py install

sudo apt-get install gcc python3-dev
sudo pip3 install psutil
