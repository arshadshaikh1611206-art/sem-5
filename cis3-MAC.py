import hmac
import hashlib

def create_mac(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()

def verify_mac(mac, key, message):
    new_mac = create_mac(key, message)
    valid = hmac.compare_digest(mac, new_mac)
    if valid:
        print("Message Is Valid")
    else:
        print("Message Is Modified")

key = input("Enter Secret Key : "). encode()
message = input("Enter Message : ").encode()

mac = create_mac(key, message)
modified_mac = create_mac(key, b"Modified Message")

verify_mac(mac, key, message)
verify_mac(modified_mac, key, message)
