import json
import jsonschema
import subprocess
import logging

from src.machine import Machine


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

logging.basicConfig(
    filename="LiemProject/logs/provisioning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_nginx_installation_script():
    try:
        # הפעלת הסקריפט עם Popen
        process = subprocess.Popen(
            ["bash", "LiemProject/scripts/install_nginx.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # קבלת פלט שורה אחרי שורה בזמן אמת (כמו tail)
        for line in process.stdout:
            print(line, end="")  # הדפס את כל שורה מהפלט
            logging.info(line)   # שמור בלוג את כל הפלט

        # בדוק אם יש שגיאות ב- stderr (אם יש)
        stderr = process.stderr.read()
        if stderr:
            print(stderr)
            logging.error(stderr)

        process.wait()  # המתן לסיום התהליך
        if process.returncode == 0:
            logging.info("✅ Simulated Nginx installation completed successfully.")
        else:
            logging.error("❌ Simulated Nginx installation failed.")

    except FileNotFoundError:
        logging.error("❌ Script file not found.")
        print("Script file not found or path is incorrect.")
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Error running the script: {e}")
        print(f"Error occurred while running the script: {e}")
    except Exception as e:
        logging.error(f"❌ Unexpected error: {str(e)}")
        print(f"An unexpected error occurred: {str(e)}")


run_nginx_installation_script()
