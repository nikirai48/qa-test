# Table of Contents
1. [System Health Monitoring Script]
2. [Application Health Checker]
  
## System Health Monitoring Script

### Description
This script monitors the health of a Linux system by checking:
- **CPU usage**
- **Memory usage**
- **Disk space**
- **Running processes**

If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script will send an alert to the console.

### Requirements
- Python 3.x
- `psutil` library

### Installation
To install the required library, run the following command:
```bash
pip install psutil

## Application health checker

### Description
This script checks the uptime of a specified application by assessing its HTTP status codes. It determines if the application is:
- **Up: Functioning correctly**
- **Down: Unavailable or not responding**

### Requirements
- Python 3.x
- requests library

### Installation
To install the required library, run the following command:
```bash
pip install requests
  
