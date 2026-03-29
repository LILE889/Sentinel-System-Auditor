import subprocess
import datetime
import getpass

def cpu_usage():
    # safley run this command
    top_process = subprocess.Popen(["top", "-bn1"], stdout=subprocess.PIPE)
    
    #use grep to sudosusu
    output, error = top_process.communicate()
    for line in output.decode().split('\n'):
        if "Cpu(s)" in line:
            # Manually parse the string logic
            parts = line.split()
            usage = float(parts[1]) + float(parts[3])
            return f"{usage}%"
    return "Error"
def ram_info():
    # Using 'free -m' to get memory in Megabytes
    try:
        output = subprocess.check_output(["free", "-m"]).decode()
        lines = output.split('\n')
        # Line 1 is the 'Mem:' line. Index 1=total, 2=used, 3=free
        mem_data = lines[1].split()
        total = mem_data[1]
        used = mem_data[2]
        free = mem_data[3]
        return f"Total: {total}MB | Used: {used}MB | Free: {free}MB"
    except:
        return "Error"

def get_disk_space():
    # Using 'df -h' specifically for the root partition
    try:
        output = subprocess.check_output(["df", "-h", "/"]).decode()
        lines = output.split('\n')
        # Line 1 is the data line. Index 3 is 'Available'
        disk_data = lines[1].split()
        return f"Available: {disk_data[3]}"
    except:
        return "Error"

def log_event():
    # Grabs the current system user and exact timestamp
    user = getpass.getuser()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Grab the last login info for this user via subprocess
    try:
        last_login = subprocess.check_output(["last", "-n", "1", user]).decode().split('\n')[0]
    except:
        last_login = "No login history found"

    log_entry = (f"--- SECURITY AUDIT ---\n"
                 f"Request Time: {timestamp}\n"
                 f"Accessed By: {user}\n"
                 f"Last Session Info: {last_login}\n"
                 f"----------------------\n")
    
    with open("sentinel_security.log", "a") as f:
        f.write(log_entry)
    
    return f"Event logged for user: {user}"