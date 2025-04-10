#!/bin/bash


echo "[✔] Checking if Nginx is installed..."

# Check if nginx is installed by looking for its executable
if which "nginx" > /dev/null 2>&1; then
    echo "[✔] Nginx is already installed."
else
    echo "[i] Nginx is not installed. Simulating installation..."

    # Simulate updating package list
    echo "[✔] sudo apt update"
    sleep 1  # Simulate delay

    # Simulate installing Nginx
    echo "[✔] sudo apt install -y nginx"
    sleep 2  # Simulate delay
fi

# Simulate starting Nginx
echo "[✔] sudo systemctl start nginx"
sleep 3  # Simulate delay

# Simulate enabling Nginx to start on boot
echo "[✔] sudo systemctl enable nginx"
sleep 4  # Simulate delay

# Simulate checking the status of Nginx
echo "[✔] sudo systemctl status nginx"
sleep 5  # Simulate delay
echo "[✔] Status: Nginx is running successfully"

exit 0
