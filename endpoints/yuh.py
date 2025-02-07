import requests

response = requests.get("http://127.0.0.1:5000/")
print(response.status_code)  # Should be 200
print(response.json())  # Should print {'message': 'Hello, World!'}
