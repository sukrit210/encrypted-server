from encrypt import Encrpyt


def Decrypt(msg):
    key = 3
    decrypt_bytes = []
    for byte in msg:
        byte -= key
        decrypt_bytes.append(byte)

    msg_bytes = bytes(decrypt_bytes)
    decode_msg = msg_bytes.decode('utf-8')
    return decode_msg

# origin , final= Decrypt()
# print(final) 
# print(origin)
   