import requests
from datetime import datetime

def get_current_date_time():
    current_date_time = datetime.now()
    return current_date_time.strftime("%Y-%m-%d %H:%M:%S")

def check_website_status():
    url = 'https://digitalcareerinstitute.org/'

    try:
        response = requests.get(url)
        current_date_time = get_current_date_time()
        status_code = response.status_code

        print(f"Current Date and Time: {current_date_time}")
        print(f"Status Code for {url}: {status_code}")

    except requests.RequestException as e:
        print(f"Error: {e}")

check_website_status()
