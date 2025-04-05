import logging

# הגדרת הגדרות הלוגים
logging.basicConfig(filename="LiemProject/logs/provisioning.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name  # שם ה-VM
        self.os = os      # מערכת הפעלה של ה-VM
        self.cpu = cpu    # מספר ה-CPUs
        self.ram = ram    # זיכרון RAM ב-GB
        logging.info(f"Created machine: {self.name} ({self.os}, {self.cpu} CPUs, {self.ram} GB RAM)")

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }

    def log_creation(self):
        logging.info(f"Machine {self.name} created with OS: {self.os}, CPU: {self.cpu}, RAM: {self.ram}")
