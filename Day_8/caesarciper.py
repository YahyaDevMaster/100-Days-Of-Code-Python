alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

def caesar_cipher(enorde):
    shift_number=int(input("Please enter the number? "))#The user Did Enter Number 4 For Example
    Message=input("please enter your massage that will trans to the Cipher ").lower()#The user did enter the "Yahya" FOR EXAMPLE
    CaesarCipher="Here is your result: "
    if enorde ==False:
        shift_number*=-1
    for i in Message:
        if i in alphabet:
            mod=(alphabet.index(i)+shift_number)%26
            CaesarCipher+=alphabet[mod]
        else:
            CaesarCipher+=i
    print(CaesarCipher)

print("""                                                                  
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          
""")
should_continue = True
while should_continue:
    enorde=input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    
    if enorde=="encode":
        caesar_cipher(True)
    elif enorde=="decode":
        caesar_cipher(False)
    else:
        print("Your type has not included")
    
    restart = input("Do you want to replay? Yes or no: \n").lower()
    if restart == "no":
        should_continue = False 
        print("Goodbye! 👋")

