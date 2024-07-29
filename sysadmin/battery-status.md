#linux #ubuntu #server #scripts #cron

## using `upower`

```bash
asurve@lilac:~$ upower --enumerate
/org/freedesktop/UPower/devices/battery_BAT0
/org/freedesktop/UPower/devices/line_power_ADP1
/org/freedesktop/UPower/devices/DisplayDevice
```

```bash
asurve@lilac:~$ upower -i /org/freedesktop/UPower/devices/battery_BAT0
  native-path:          BAT0
  vendor:               SMP
  model:                bq20z451
  power supply:         yes
  updated:              Mon 29 Jul 2024 01:09:48 PM PDT (19 seconds ago)
  has history:          yes
  has statistics:       yes
  battery
    present:             yes
    rechargeable:        yes
    state:               discharging
    warning-level:       none
    energy:              45.3488 Wh
    energy-empty:        0 Wh
    energy-full:         48.9347 Wh
    energy-full-design:  54.7018 Wh
    energy-rate:         8.87334 W
    voltage:             12.184 V
    charge-cycles:       467
    time to empty:       5.1 hours
    percentage:          92.6721%
    temperature:         28.9 degrees C
    capacity:            89.4572%
    technology:          lithium-ion
    icon-name:          'battery-full-symbolic'
  History (charge):
    1722283788  92.672  discharging
    1722283788  0.000   unknown
  History (rate):
    1722283788  8.873   discharging
    1722283788  0.000   unknown
```

## using `acpi`

```bash
asurve@lilac:~$ acpi -b
Battery 0: Discharging, 92%, 05:05:43 remaining
```

## automating battery logs with `apci`

### `monitor_battery.md`
```bash
#!/bin/bash

# Set log directory
LOG_DIR="/home/asurve/logs/battery_status"

# Create log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Get current date
CURRENT_DATE=$(date +"%Y-%m-%d")

# Set log file name for today
LOG_FILE="$LOG_DIR/battery_log_$CURRENT_DATE.txt"

# Get battery info
battery_info=$(acpi -b)

# Extract battery info
battery_percent=$(echo $battery_info | grep -P -o '[0-9]+(?=%)')

# Extract charging status
charging_status=$(echo $battery_info | grep -P -o '(Charging|Discharging|Full)')

# Log the information
# echo "$(date): Battery at $battery_percent% - $charging_status" >> "$LOG_FILE"
echo "$(date): $battery_info" >> "$LOG_FILE"

# TODO: Send an alert if battery is under a threshold

# Purge logs older than 30 days
find "$LOG_DIR" -name "log_*.txt" -type f -mtime +30 -delete
```

### set up a cron job to run regularly

```bash
crontab -e
```

```bash
# added this line to the end of the file to run every 10 minutes
*/10 * * * * /home/asurve/scripts/monitor_battery.sh
```

- `*/10`: run at every 10th minute
- `*`: every hour
- `*`: every every day of the month
- `*`: every month
- `*`: every every day of the week
