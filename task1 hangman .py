import random
def hangman():
    list_of_words = ["artificial","intelligence","python","programmer","hangman"]
    word =random.choice(list_of_words)
    turns = 10
    guessmade = '  '
    valid_entry= set('abcdefghijklmnopqrstuvwxyz')
    print("\n Lets begin the Hangman game!")
    while len(word)>0:
        main_word = "  "
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word +letter
            else:
                main_word = main_word+"_"
            if main_word == word:
                print("\n Congeatulations you won the game! ")
                print(main_word)
                break
        print("guess a word",main_word)
        guess = input()
        if guess in valid_entry:
            guessmade = guessmade +guess
        else:
            print("enter valid character")
            guess=input()
        if guess not in word:
            turns = turns-1

            if turns==9:
                print("9 turns left!!!")
                print("----------")
            if turns==8:
                print("8 turns left!!!")
                print("----------")
                print("    o     ")
            if turns == 7:
                print("7 turns left!!!")
                print("----------")
                print("    o     ")
                print("    |    ")
            if turns == 6:
                print("6 turns left!!!")
                print("----------")
                print("    o     ")
                print("    |    ")
                print("    /    ")
            if turns == 5:
                print("5 turns left!!!")
                print("----------")
                print("    o     ")
                print("    |    ")
                print("   / \    ")
            if turns == 4:
                print("4 turns left!!!")
                print("----------")
                print("   \o     ")
                print("    |    ")
                print("   / \    ")
            if turns == 3:
                print("3 turns left!!!")
                print("----------")
                print("   \o/    ")
                print("    |    ")
                print("   / \    ")
            if turns == 2:
                print("2 turns left!!!")
                print("----------")
                print("   \o/ |  ")
                print("    |    ")
                print("   / \    ")
            if turns == 1:
                print("only 1 turns left!!!hangman on his last breadth!!!")
                print("----------")
                print("   \o/ _|  ")
                print("    |    ")
                print("   / \    ")
            if turns == 0:
                print("you loose!!!")
                print("you let a good man die")

name = input("enter your name -> ")
print("welcome", name,"!")
print("-------------------------------------")
print("Try to guess the word in less than 10 attempts")
hangman()
