# secret code 2
def decrypt():
    ciphertext = input("Enter your coded text: ")
    shift = int(input("Enter the distance value: "))
    space = []

    # creat a list of encrypted words.
    ciphertext = ciphertext.split()

    # creat a list to hold decrypted words.
    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)

    sentence = ' '.join(sentence)
    
    print(str(sentence))
    
decrypt()