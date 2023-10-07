def rot13(message):
#   ROT13
#   ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
#   ||||||||||||||||||||||||||||||||||||||||||||||||||||
#   NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm

    ROT13 = {
        'A': 'N','B': 'O','C': 'P','D': 'Q','E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 
        'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 
        'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'
            }

    decoded = ''
    for i in message:
        if i.isupper() == True and i in ROT13.keys():
            decoded = decoded + ROT13[i]
        elif i.isupper() != True and i.upper() in ROT13.keys():
            decoded = decoded + (ROT13[i.upper()]).lower()
        else:
            decoded = decoded + i

    print(decoded)

rot13('EBG13 rknzcyr.')


