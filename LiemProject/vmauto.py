def get_vm_input():
    name = input("Enter VM name: ")
    if not name.strip():
        print("❌ VM name cannot be empty.")
        return False

    os = input("Enter OS (Linux Ubuntu / Windows 10):  ")
    if os not in ["Linux Ubuntu", "Windows 10", "Linux", "Windows","windows","linux"]:
        print("❌ The operating system must be 'Linux Ubuntu' or 'Windows 10'.")
        return False

    try:
        cpu = int(input("Enter number of CPUs: "))
        if cpu <= 0:
            print("❌ The number of cores (CPU) must be positive.")
            return False
    except ValueError:
        print("❌ CPU must be an integer.")
        return False

    try:
        ram = int(input("Enter amount of RAM (GB): "))
        if ram <= 0:
            print("❌ The memory (RAM) must be positive.")
            return False
    except ValueError:
        print("❌ RAM must be an integer.")
        return False

    return {"name": name, "os": os, "cpu": cpu, "ram": ram}

vm_data = get_vm_input()
if vm_data:
    print("✅ Good input")
    print(vm_data)
else:
    print("⛔️ Bad input")