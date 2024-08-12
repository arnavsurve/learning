
We can create a systemd service to poll for battery status and feed it to node exporter. This writes battery status information to `/var/lib/node_exporter/battery.prom` to be read by [node exporter][node-exporter].

#### `/usr/local/bin/battery_metrics.sh`

```bash
#!/bin/bash

METRICS_FILE="/var/lib/node_exporter/battery.prom"
battery_info=$(acpi -b)
battery_percent=$(echo $battery_info | grep -P -o '[0-9]+(?=%)')
charging_status=$(echo $battery_info | grep -P -o '(Charging|Discharging|Full)')

if [ "$charging_status" == "Charging" ]; then
    charging_status_value=1
elif [ "$charging_status" == "Discharging" ]; then
    charging_status_value=0
else
    charging_status_value=2
fi

echo "# HELP battery_percentage Battery percentage." > $METRICS_FILE
echo "# TYPE battery_percentage gauge" >> $METRICS_FILE
echo "battery_percentage $battery_percent" >> $METRICS_FILE

echo "# HELP battery_charging_status Battery charging status (1=Charging, 0=Discharging, 2=Full)." >> $METRICS_FILE
echo "# TYPE battery_charging_status gauge" >> $METRICS_FILE
echo "battery_charging_status $charging_status_value" >> $METRICS_FILE
```

# creating a systemd service for battery metrics

We need a timer as otherwise the service throws an error `start-limit-hit` indicating the service has attempted to restart too many times. This is because otherwise, the service would be configured to restart continuously but exits quickly each time it runs.

#### `/etc/systemd/system/battery_metrics.service`

```bash
[Unit]
Description=Battery Metrics

[Service]
Type=oneshot
ExecStart=/usr/local/bin/battery_metrics.sh

[Install]
WantedBy=multi-user.target
```

#### `/etc/systemd/system/battery_metrics.timer`

```bash
[Unit]
Description=Run battery_metrics.sh every 5 minutes

[Timer]
OnBootSec=5min
OnUnitActiveSec=5min
Unit=battery_metrics.service

[Install]
WantedBy=timers.target
```
