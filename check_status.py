import requests

def check_website():
    url = "https://github.com"
    print(f"Sending a GET request to {url}...")
    
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    print(f"API Server Headers: {response.headers.get('server')}")

if __name__ == "__main__":
    check_website()
