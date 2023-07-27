import random
from list_of_500_words import easy_list
from list_of_next_1500_words import hard_list

print("Welcome to Almost Wordle, the highly un-copyrighted word-guessing game!")

difficulty = str(input("Please choose your level of difficulty - easy or hard: "))

if difficulty == "easy":
    word = random.choice(easy_list)
else:
    word = random.choice(hard_list)

answer = str(word)

guess = str(input("OK! Here we go. Please enter your first guess: "))

while len(guess) != 5:
    print("Only five-letter-words are allowed.")
    guess = str(input("Please enter another word:"))
else:
    pass

#while guess not in list_of_all_five_letter_words:
    #print("Guess is not a word")
    #guess = str(input("Please enter another word:"))
#else:
    #pass

word_as_a_list = list(guess)

#print(word_as_a_list)

answer_as_a_list = list(answer)

#print(answer_as_a_list)

if guess == answer:
    print("Congratulations, you won!")
else:
    for x in word_as_a_list:
        if x in answer_as_a_list:
            if word_as_a_list.index(x) == answer_as_a_list.index(x):
                print("The letter", x, "is present at the same place in the answer")
            else:
                print("The letter", x, "is present but at a different position.")

    print("Four guesses left!")

    second_guess = str(input("Enter your next guess: "))

    if second_guess == answer:
        print("Congratulations, you won!")
    else:
        second_guess_as_a_list = list(second_guess)
        for x in second_guess_as_a_list:
            if x in answer_as_a_list:
                if second_guess_as_a_list.index(x) == answer_as_a_list.index(x):
                    print("The letter", x, "is present at the same place in the answer")
                else:
                    print("The letter", x, "is present but at a different position.")

        print("Three guesses left!")

        third_guess = str(input("Enter your next guess: "))

        if third_guess == answer:
            print("Congratulations, you won!")
        else:
            third_guess_as_a_list = list(third_guess)
            for x in third_guess_as_a_list:
                if x in answer_as_a_list:
                    if third_guess_as_a_list.index(x) == answer_as_a_list.index(x):
                        print("The letter", x, "is present at the same place in the answer")
                    else:
                        print("The letter", x, "is present but at a different position.")

            print("Two guesses left!")

            fourth_guess = str(input("Enter your next guess: "))

            if fourth_guess == answer:
                print("Congratulations, you won!")

            else:
                fourth_guess_as_a_list = list(fourth_guess)
                for x in fourth_guess_as_a_list:
                    if x in answer_as_a_list:
                        if fourth_guess_as_a_list.index(x) == answer_as_a_list.index(x):
                            print("The letter", x, "is present at the same place in the answer")
                        else:
                            print("The letter", x, "is present but at a different position.")

                print("Last guess!")

                fifth_guess = str(input("Enter your next guess: "))

                if fifth_guess == answer:
                    print("Congratulations, you won!")
                else:
                    print("Sorry, the answer was", answer)
                    print("Better luck next time!")
