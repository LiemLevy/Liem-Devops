def get_vm_input():
    name = input("Enter VM name: ")
    os = input("Enter OS (Linux Ubuntu / Windows 10):  ")
    cpu = int(input("Enter number of CPUs: "))
    ram = int(input("Enter amount of RAM (GB): "))
    return {"name": name, "os": os, "cpu": cpu, "ram": ram}

ןif os == "Linux Ubuntu": 
get_vm_input()