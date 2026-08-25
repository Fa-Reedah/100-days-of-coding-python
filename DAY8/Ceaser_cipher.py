# Encryption game

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

directions_ = input("Type 'encode' to encrypt and 'decode' to decrypt:\n ").lower()
text_ = input("Type your message:\n").lower()
shift_ = int(input("Type shift number:\n"))


def question():
    question_ = input("Do you want to go again (Yes/No):\n").lower()
    if question_ == "yes":
        directions_ = input("Type 'encode' to encrypt and 'decode' to decrypt:\n ").lower()
        text_ = input("Type your message:\n").lower()
        shift_ = int(input("Type shift number:\n"))
        ceaser(text_, shift_, directions_)
        question()
    else:
        print("END")


def ceaser(text, shift, directions):
    result = ""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)

            if directions == "encode":
                code = alphabet[(position + shift) % 26]
                result += code

            elif directions == "decode":
                code = alphabet[(position - shift) % 26]
                result += code
        else:
            result += i

    print(f"Your message is:\n {result}")


ceaser(text_, shift_, directions_)

question()

'''   
def encrypt(text, shift):
    encode = ""
    for i in text:
       # position = 0
       # for a in alphabet:
       #     position += 1
        position = alphabet.index(i)
       #     if a == i:
       #     code = alphabet[((position + shift)-1)%26]
        code = alphabet[(position + shift)%26]
        encode += code
       #        break            replace with line 16
    print(54356789 0-=
09 654321`2378=9|+

def decrypt(text, shift):
    decode = ""
    for i in text:
       # position = 0
       # for a in alphabet:
       #     position += 1
        position = alphabet.index(i)
       #     if a == i:
       #     code = alphabet[((position + shift)-1)%26]
        code = alphabet[(position - shift)%26]
        decode += code
       #        break            replace with line 16
    print(decode)

if directions == "encode":
    encrypt(text_, shift_)
elif directions == "decode":
    decrypt(text_, shift_)
'''
