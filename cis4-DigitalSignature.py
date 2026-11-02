from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes

private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public = private.public_key()

def create_signature(message) :
    return private.sign(message, padding.PKCS1v15(), hashes.SHA256())

def verify_signature(signature, message):
    try:
        public.verify(signature, message, padding.PKCS1v15(), hashes.SHA256())
        print("Message Is Valid")
    except InvalidSignature:
        print("Message Is Modified or Signature Is Incorrect")

message = input("Enter Message : ").encode ()
signature = create_signature (message)
invalid_signature = create_signature(b"Modified Message")

verify_signature(signature, message)
verify_signature(invalid_signature, message)
