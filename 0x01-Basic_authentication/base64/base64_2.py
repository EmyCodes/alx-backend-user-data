#!/usr/bin/python3

import requests
import base64


# Replace with your actual credentials
username = 'your_username'
password = 'your_password'

url = 'https://example.com/protected_resource'

# Combine the username and password with a colon and encode in Base64
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode('ascii')).decode('ascii')

# Construct the Authorization header
headers = {'Authorization': f'Basic {encoded_credentials}'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Access granted:", response.text)
else:
    print("Access denied. Status code:", response.status_code)

