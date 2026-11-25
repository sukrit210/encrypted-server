from key import Key




def Encrpyt():
    message = input("enter your message: ")
    key_agreed = 3
    bytes_msg = message.encode('utf-8')
    encrypt_msg = []
    for byte in bytes_msg:
        byte += key_agreed
        encrypt_msg.append(byte)

    return bytes(encrypt_msg)
    

# name = Encrpyt(message)
# print(name)



