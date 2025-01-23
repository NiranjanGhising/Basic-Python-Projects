import random

def get_word():
    words_to_be_gusses = ['apple', 'stock', 'money','enjoy', 'focus', 'force','green']
    
    #generate ramdom words from list
    Ramdom_word = random.choice(words_to_be_gusses).upper()

    return Ramdom_word

def hidden_word(random_word):
    
    #hide the letters 
    return '_' *len(random_word)

def guessing_letter(random_word,hide_words):
    gusses_letter = []
    total_attempt = 5
    hide_word_list = list(hide_words)

    #run while the game over or user win game
    while total_attempt>0:

        
        gusses= input("enter A letter that can be in the word: ").upper()

        if gusses in  gusses_letter:
            print("You have already Enter this letter")
        #if gussed correct word
        elif gusses in random_word:
            print("Good !! you have gusses right letter")
            gusses_letter.append(gusses)
            #checks the index of correct letter
            for i in range(len(random_word)):
                if random_word[i] == gusses:
                    hide_word_list[i]= gusses
        else:
            print("Incorrect gusses")
            gusses_letter.append(gusses)
            total_attempt-=1
        # joins the elements of hide_word_display into one. converts lists into string.
        hide_word_display = ''.join(hide_word_list)
        print(hide_word_display)
        print(f"you have {total_attempt} attempt left")
        
        if '_' not in hide_word_list:
        
            print("You have gussed all the words Correctly.")
            break
    else:
        print(f"Game over... The Word was {random_word}")

    

def main():
    
    random_word = get_word()
    hide_words = hidden_word(random_word)
    print(hide_words)

    main_game = guessing_letter(random_word, hide_words)
    print(main_game)

    
    



result = main()
print(result)


