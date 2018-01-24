#! /bin/bash
start-stop-daemon --start --background --exec /home/pi/discordbot/weaponbot.py --make-pidfile --pidfile=/tmp/weaponbot.pid
start-stop-daemon --start --background --exec /home/pi/discordbot/teambot.py --make-pidfile --pidfile=/tmp/teambot.pid
start-stop-daemon --start --background --exec /home/pi/slackbot/run.py --make-pidfile --pidfile=/tmp/googlehomebot.pid
start-stop-daemon --start --background --exec /home/pi/tweetsync/post_discord.py --make-pidfile --pidfile=/tmp/tweetsync.pid
