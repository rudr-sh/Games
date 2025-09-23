import random
import hangman_art
import hangman_wordlist
################################################
print(hangman_art.art)
choosen_word = random.choice(hangman_wordlist.word_list)

dash = ""

for blank in range(len(choosen_word)):
    dash+="_"
print(dash)
##################################################
lives = 0
game_over = False
correct_letters =[]
previous_try =[]
while game_over == False and lives < 7:

    guess = input("Enter letter choosen by you: ").lower() 

    letter_match = ""
    if guess in correct_letters:
        print("You've already guesssed this letter")
    for match in choosen_word:
        if match == guess:
            letter_match+= match
            correct_letters.append(match)
        elif match in correct_letters:
            letter_match += match
        else:
            letter_match+="_"
    print(letter_match)
    if letter_match in previous_try:
        print(hangman_art.HANGMANPICS[lives])
        lives+=1
        print("This letter is not in this word.")
    previous_try.append(letter_match)
    if "_" not in letter_match:
        game_over = True
if lives >= 7:
    print(f"*************************** YOU LOST *************************************\n The word was {choosen_word}")
elif game_over == True:
    print("*************************** YOU WON ************************************* ")
