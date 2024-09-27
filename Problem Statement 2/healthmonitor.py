import psutil
import time

cpu_threshold = 80  
memory_threshold = 80  
disk_threshold = 80  

def Cpu_usage():
    check_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {check_usage}%")
    
    if check_usage > cpu_threshold:
        print(f"Alert! CPU usage is above {cpu_threshold}%!")
    else:
        print("CPU usage is within normal limits.")

def memory_usage():
    memory = psutil.virtual_memory()  
    memory_usage = memory.percent  
    print(f"Memory Usage: {memory_usage}%")
    
    if memory_usage > memory_threshold:
        print(f"Alert! Memory usage is above {memory_threshold}%!")
    else:
        print("Memory usage is within normal limits.")

def disk_usage():
    disk = psutil.disk_usage('/')  
    disk_usage = disk.percent  
    print(f"Disk Usage: {disk_usage}%")
    
    if disk_usage > disk_threshold:
        print(f"Alert! Disk usage is above {disk_threshold}%!")
    else:
        print("Disk usage is within normal limits.")

if __name__ == "__main__":
    while True:
        Cpu_usage()         
        memory_usage()      
        disk_usage()        
        time.sleep(5)            
