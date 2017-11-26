# Dan & Kelly's Flood Detector

## Purpose

When a sensor gets wet, send an SMS text message to a list of numbers. Record
wetness readings regularly and log them to a (rotating) log file.

## Hardware

Follow the
[rain detection module instructions](https://www.sunfounder.com/learn/sensor-kit-v2-0-for-raspberry-pi-b-plus/lesson-14-rain-detection-module-sensor-kit-v2-0-for-b-plus.html)
from the SunFounder Sensor Kit v2.0.

## SMS Capability

Sign up for an account with [Twilio](https://www.twilio.com).

## Installation & Usage

First install a Python dependency that is apparently not distributed through
PyPI (and therefore not pip-installable).

```
sudo apt-get install python-smbus
```

Clone this reposity and install the Python package.

```
https://github.com/danielballan/flood-detector
cd flood_detector
python setup.py develop
```

Customize using environment variables. Start with the example file included in
the repo.

```
cp .env.example .env
```

Enter Twilio accounts information and phone numbers into ``.env``. Then:

```
source .env
sudo -E flood_monitor
```

To check that it is running successfully, tail the log file:

```
tail -f /var/log/flood_monitor/flood_monitor.log
```

## Troubleshooting

If getting an ``IOError``, use ``i2cHelper.py`` from SunFounder to check for
problems. Find it, for example,
[here](https://github.com/sunfounder/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/blob/master/i2cHelper.py).
