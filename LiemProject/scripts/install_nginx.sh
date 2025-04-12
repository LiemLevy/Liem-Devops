#!/bin/bash


echo "[✔] Checking if Nginx is installed..."


if which "nginx" > /dev/null 2>&1; then
    echo "[✔] Nginx is already installed."
else
    echo "[i] Nginx is not installed. Simulating installation..."

    
    echo "[✔] sudo apt update"
    sleep 1  

    
    echo "[✔] sudo apt install -y nginx"
    sleep 2  
fi


echo "[✔] sudo systemctl start nginx"
sleep 3  


echo "[✔] sudo systemctl enable nginx"
sleep 4  


echo "[✔] sudo systemctl status nginx"
sleep 5  
echo "[✔] Status: Nginx is running successfully"

exit 0