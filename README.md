# spoblock
Simple program muting audio while spotify is running ads for linux.

It's getting the current windows title and if it's not corresponding to music, spotify app is closed and automatically plays music once reopened

Tips : create an alias like this one so you just have to use the command spotify and enjoy ```alias spotify="spotify & python3 /PATH_TO_SCRIPT/spotify.py;"```

## Requirements

Linux, created on Debian 9, works on Debian 10

apt install :
- libasound2-dev

pip3 install :
- psutil
- termcolor
- pynput
- pyalsaaudio
