#linux #server #monitoring #prometheus #systemd

https://prometheus.io

# running promethus with systemd

https://janakiev.com/blog/prometheus-setup-systemd/

Create a dedicated `prometheus` user with: 
	`sudo useradd -M -U prometheus`

Download and move installed folder to `/opt/prometheus`
	ex. `sudo mv prometheus-2.40.0-rc.0.linux-amd64 /opt/prometheus`

Create a systemd service in `/etc/systemd/system/prometheus.service`

```
[Unit]
Description=Prometheus Server
Documentation=https://prometheus.io/docs/introduction/overview/
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Restart=on-failure
ExecStart=/opt/prometheus/prometheus \
  --config.file=/opt/prometheus/prometheus.yml \
  --storage.tsdb.path=/opt/prometheus/data \
  --storage.tsdb.retention.time=30d

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl start prometheus.service
sudo systemctl enable prometheus.service
```

Prometheus configuration is done in `/opt/prometheus/prometheus.yml`. A sample prometheus.yml file looks like this:

```yml
global:
  scrape_interval:     15s # By default, scrape targets every 15 seconds.

  # Attach these labels to any time series or alerts when communicating with
  # external systems (federation, remote storage, Alertmanager).
  external_labels:
    monitor: 'codelab-monitor'

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:

  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'
    # Override the global default and scrape targets from this job every 5 seconds.
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9090']
```

Refer to [[node-exporter]] for an example on adding another job.