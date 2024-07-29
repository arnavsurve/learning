#linux #ubuntu #server

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
