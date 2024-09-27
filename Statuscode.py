import requests

# Configuration
url = 'https://github.com/nikirai48/qa-test' 

def check_uptime():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Application is UP! Status code: {response.status_code}")
        else:
            print(f"Application is DOWN! Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN! Error: {e}")

if __name__ == "__main__":
    check_uptime()
