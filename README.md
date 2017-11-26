# Dan & Kelly's Flood Detector

## Installation & Usage

```
cd flood_detector
python setup.py develop
cp .env.example .env
```

Enter Twilio accounts information and phone numbers.

```
source .env
sudo -E flood_monitor
```

Tail logs

```
tail -f /var/log/flood_monitor.log
```

## Troubleshooting

If getting an ``IOError``, use ``i2cHelper.py`` from SunFounder to check for problems.
