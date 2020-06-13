# lets use base64 encoding based encryption algorithm  for encryption and decryption here
import base64


def validate(n):
    name_list = list(n)
    digit_list = []
    alpha_list = []
    for i in name_list:
        if i.isdigit():
            digit_list.append(i)
        else:
            alpha_list.append(i)
    if len(alpha_list) != 0 and len(digit_list) != 0:
        return True
    else:
        return False


def enc_decrypt(n):
    masked_refid = n[::-1]  # for making decryption much harder
    # print(masked_refid)
    encrypt_str = base64.b64encode(masked_refid)
    print("NOTE: This is your encrypted string. Keep it safe.  " + str(encrypt_str))
    option = input("Whether you want the decrypted string back(yes/no) ?")
    if option.upper() == 'YES':
        decrypt_str = base64.b64decode(encrypt_str)
        decrypted = decrypt_str.decode()[::-1]
        print("Your decrypted String from encryption: " + decrypted)
    else:
        print("Exit. Done")


if __name__ == '__main__':

    name = input("Enter the Reference_ID:")
    if len(name) >= 12:
        if validate(name):
            enc_decrypt(name.encode())
        else:
            print("NOTE:Enter Reference id combining alphabets and numbers")
    else:
        print("NOTE:Enter the reference Id greater than 12 characters with num and alphabets")

# output
# checked in python3
# Enter the Reference_ID:hariharan@12345$#@1
# NOTE: This is your encrypted string. Keep it safe.  b'MUAjJDU0MzIxQG5hcmFoaXJhaA=='
# Whether you want the decrypted string back(yes/no) ?yes
# Your decrypted String from encryption: hariharan@12345$#@1
