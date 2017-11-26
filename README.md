# Dan & Kelly's Flood Detector

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
tail -f /var/log/flood_monitor.log
```

## Troubleshooting

If getting an ``IOError``, use ``i2cHelper.py`` from SunFounder to check for problems.
