#linux #server #monitoring #cockpit

You can use [cockpit](https://cockpit-project.org/) to monitor servers.

```bash
sudo apt install cockpit

sudo systemctl start cockpit.socket cockpit.server
```

Go to `https://<server ip>:9090` to access the dashboard.
