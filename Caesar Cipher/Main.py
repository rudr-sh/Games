import sketch
print(sketch.art)

def encrypt(original_text,shift_amount,mode):
    if mode == 'decode':
        shift_amount = - shift_amount
    encoded = ""
    for letter in original_text:
        if letter in alphabets:
            shift_posn = alphabets.index(letter) + shift_amount
            shift_posn %= len(alphabets)
            encoded+=alphabets[shift_posn]
        else:
            encoded+=letter
    print(f"Here's the encoded result: {encoded}")
again = True

while again:
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text,shift,direction)

    rerun=input("Do you want to use the program again? Yes or No: ").lower()
    if rerun == 'no':
        again = False
        print("GoodBye")
    else:
        again = True
    

        
