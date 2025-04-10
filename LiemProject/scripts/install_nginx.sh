#!/bin/bash

LOGFILE="LiemProject/logs/provisioning.log"

echo "$(date) - INFO - Starting Nginx installation..." >> $LOGFILE

# בדוק אם Nginx כבר מותקן
if command -v nginx > /dev/null; then
    echo "$(date) - INFO - Nginx is already installed." >> $LOGFILE
    exit 0
fi

# רק מדפיס את הפקודות מבלי להריץ אותן
echo "$(date) - INFO - Running: sudo apt update && sudo apt install -y nginx" >> $LOGFILE

# הדמיית התקנה (ללא הריצה בפועל)
echo "$(date) - INFO - Nginx simulated installation." >> $LOGFILE
