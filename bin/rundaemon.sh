#! /bin/bash
start-stop-daemon --start --background --exec "python /home/pi/discordbot/weaponbot.py" --make-pidfile --pidfile=/tmp/weaponbot.pid
start-stop-daemon --start --background --exec "python /home/pi/discordbot/teambot.py" --make-pidfile --pidfile=/tmp/teambot.pid
