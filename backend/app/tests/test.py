import requests

# Define the base URL of your API
base_url = "http://localhost:8000/api/v1/counter"

# Test the GET route
def test_get_counter():
    response = requests.get(base_url)
    if response.status_code == 200:
        print(f"GET /api/v1/counter: {response.json()}")
    else:
        print(f"Failed to GET /api/v1/counter: {response.status_code}")

# Test the POST route
def test_increment_counter():
    response = requests.post(base_url)
    if response.status_code == 200:
        print(f"POST /api/v1/counter: {response.json()}")
    else:
        print(f"Failed to POST /api/v1/counter: {response.status_code}")

test_get_counter()
test_increment_counter()