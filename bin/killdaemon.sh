#! /bin/bash
start-stop-daemon --stop --pidfile /tmp/weaponbot.pid
start-stop-daemon --stop --pidfile /tmp/teambot.pid
start-stop-daemon --stop --pidfile /tmp/googlehomebot.pid
start-stop-daemon --stop --pidfile /tmp/tweetsync.pid
