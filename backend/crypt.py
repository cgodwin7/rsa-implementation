from backend.keygen import KeyCreator
import time
print("Generating 1024 bit keys...")

ephemeral_keys = KeyCreator()

print("Done!")
time.sleep(.5)
print("Encrypting...")
time.sleep(1)
def encrypt(mess):
    e, n = ephemeral_keys.fetchPubKey()
    return (pow(mess,e,n))

def decrypt(mess):
    d, n = ephemeral_keys.fetchPrivKey()
    return (pow(mess,d,n))


