#linux #server #prometheus #monitoring #systemd

`sudo useradd -rs /bin/false node_exporter`

Create a systemd service in `/etc/systemd/system/node_exporter.service`

```
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
ExecStart=/usr/local/bin/node_exporter --collector.textfile.directory=/var/lib/node_exporter
Restart=always

[Install]
WantedBy=multi-user.target
```

Create a job `node_exporter` in `prometheus.yml`

```yml
  - job_name: 'node_exporter'
    static_configs:
      - targets: ['localhost:9100']
```
