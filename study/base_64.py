import base64

# Creating a string
message = "This is textum from Sovinion"
# Encoding the string into bytes
message_bytes = message.encode("UTF-8")
print(type(message_bytes))
print(message_bytes)
# Base64 Encode the bytes
base64_bytes = base64.b64encode(message_bytes)
print(type(base64_bytes))
# Decoding the Base64 bytes to string
base64_message = base64_bytes.decode("UTF-8")

print(base64_message)

print("and rollback")

print(base64.b64decode(base64_message).decode("UTF-8"))
