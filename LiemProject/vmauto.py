import json
import jsonschema
from src.machine import Machine  # אנחנו מייבאים את המחלקה Machine

vm_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "os": {"type": "string", "enum": ["Linux Ubuntu", "Windows 10", "Linux", "Windows", "windows", "linux"]},
        "cpu": {"type": "integer", "minimum": 1},
        "ram": {"type": "integer", "minimum": 1}
    },
    "required": ["name", "os", "cpu", "ram"]
}

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


def save_vm_data_to_json(vm_data):
    
    try:
        jsonschema.validate(instance=vm_data, schema=vm_schema)
        print("✅ JSON schema validation passed.")
        with open('LiemProject/instances.json', 'w') as f:
            json.dump(vm_data, f, indent=4)
    except Exception as e:
        print("❌ JSON schema validation failed")


vm_data = get_vm_input()
if vm_data:
    machine = Machine(vm_data['name'], vm_data['os'], vm_data['cpu'], vm_data['ram'])
    print("✅ Good input")
    print(vm_data)
else:
    print("⛔️ Bad input")

save_vm_data_to_json(vm_data)
