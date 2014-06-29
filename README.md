Uses requests to monitor HTTP-servers for availability. Uses pushbullet or e-Mail for notification if host unreachable.

## usage

* install python (e.g.`sudo apt-get install python python-setuptools`)
* install pip (e.g. `sudo easy_install pip`)
* install dependencies (e.g. `pip install -r requirements.txt`)

* Configure (`cp config_example.json config.json`)
* Configure Pushbullet https://www.pushbullet.com/account
* Test the script `python pyhttpmon.py`
* Install conjob (e.g. `crontab -e`)
* `@daily python ~/pyhttpmon/pyhttpmon.py`

### uberspace
* clone repository `git clone https://github.com/dalcacer/pyhttpmon.git`
* `pip-3.2 install -r requirements.txt`
* Configure (`cp config_example.json config.json`)
* Configure Pushbullet https://www.pushbullet.com/account
* Test the script `python3.2 pyhttpmon.py `
* Install conjob (e.g. `crontab -e`)
* `@hourly /usr/local/bin/python3.2 ~/pyhttpmon/pyhttpmon.py`

## development

## used libs

## license
Not idea, yet.