#!/usr/bin/python3

import base64


# String to be encoded
input_string = "Hello, Base64 encoding!"

# Convert the string to bytes (ASCII)
input_bytes = input_string.encode('ascii')

# Perform Base64 encoding
encoded_bytes = base64.b64encode(input_bytes)

# Convert the encoded bytes back to a string
encoded_string = encoded_bytes.decode('ascii')

print(encoded_string)

