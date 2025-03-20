def get_vm_input():
    name = input("Enter VM name: ")
    os = input("Enter OS: ")
    cpu = int(input("Enter number of CPUs: "))
    ram = int(input("Enter amount of RAM (GB): "))
    return {"name": name, "os": os, "cpu": cpu, "ram": ram}

get_vm_input()