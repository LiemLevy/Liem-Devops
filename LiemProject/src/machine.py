import logging


logging.basicConfig(filename="LiemProject/logs/provisioning.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
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
