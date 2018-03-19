#alphabet = "abcdefghijklmnopqrstuvwxyz !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`{|}~"
#key = "qwertyuioplkjhgfdsazxcvbn/m'].;[,?\"}>:{<\\|=_+-0 192837465)!(@*#&$^%`~PLQAOKWSIJEDUHRFYGTZMXNCBV"
alphabet = "`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
key = " !\"#$%&'()*+,-2./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"   
def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result = ""
    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result
'''
with open("/Users/ewilbe5944/project/snel/text_files/file_001597.txt", 'r') as f:
        unencrypted_message = f.read()
        f.close()
'''

encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)


print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)

