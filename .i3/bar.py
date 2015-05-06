# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Shows Date and Time
status.register(
	"clock",
	format="%H:%M %a %b %d" #Format: 23:00 | Mon Jan 1
)

# Show CPU Usage
status.register("cpu_usage",format=" {usage:02}%")

# Show Memory Usage
status.register(
	"mem",
	format=" {used_mem:00}G/{avail_mem:00}G"
)

# Shows CPU temperature
status.register("temp", format=" {temp:.0f}°C")

# Shows Battery Status
status.register(
	"battery",
	format="{status} {remaining:%E%hh:%Mm}",
	alert=True,
	alert_percentage=5,
	status={
		"DIS":  "",
		"CHR":  "",
		"FULL": "",
	}
)

# Displays whether a DHCP client is running
status.register("runwatch", name="", path="/var/run/dhclient*.pid")

# Shows status of Wireed Interface
status.register(
	"network",
	interface="lan0",
	format_up="{v4cidr}"
)

# Shows the status of Wireless Interface
status.register(
	"wireless",
	interface="wifi0",
	format_up=" {essid}:{v4cidr} {quality:02.0f}%",
	format_down=""
)

# Shows disk usage of /
#status.register(
#	"disk",
#	path="/home",
#	format=" {used}/{total}G [{avail}G]"
#)

# Shows pulseaudio default sink volume
status.register("pulseaudio", format=" {volume}%")

# Shows MPD status
'''status.register(
	"mpd",
	format="{status} {title}/{album}",
	status={
		"pause": "",
		"play": "",
		"stop": "",
	}
)'''

status.run()
