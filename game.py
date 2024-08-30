from data import movies, options_movies
from data import games, options_games
from data import user_questions, user_options


def user_input():
    # print("Would you like to add your own questions?")
    # user_decision = input("State Yes or No: ").upper()
    while True:
        print("Would you like to add your own questions?")
        user_decision = input("State Yes or No: ").upper()
        if user_decision == "YES":
            print("How many questions would you like to add?:")
            number_of_questions = int(input())
            n = 0
            nq=0
            if nq <= number_of_questions:
                nq+=1
                while n < number_of_questions:
                    print(f"Enter question {n+1} : ")
                    new_question_from_user = input()
                    print("Enter the questions in this format (A.answer B.answer C.answer D.answer)")
                    print("Enter the choices for your question (space-separated between the answers): ")
                    usr_choices = input()
                    user_options.append(usr_choices.split(" "))

                    print("Enter the correct answer for the question: ")
                    usr_answer = input().upper()
                    user_questions[new_question_from_user]=usr_answer
                    n+=1
            print("\nUpdated Questions and Answers! ")
            for question, answer in user_questions.items():
                print(f"Question: {question} | Answer: {answer}")       
            break      

        elif user_decision == "NO":
            print("Exiting the input section.")
            break
        else:
            print("Enter valid answer!")
            print("----------------------")

user_input()
def select_question():
    print("Choose type of questions!")
    print("1. Movies")
    print("2. Games")
    print("3. Your own questions")

    while True:
        choice = input("Enter a number to choose the questions: ")
        if choice == "1":
            return movies, options_movies
        elif choice == "2":
            return games, options_games
        elif choice == "3":
            return user_questions, user_options
        else:
            print("Invalid choice! Choose a valid number!")


def new_game():
    questions, options = select_question()
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("(------------------)")
        print(key)
        for i in options[question_num - 1]:

            print(i)
        guess = input("Enter (A,B,C or D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses, questions)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct answer!")
        return 1
    else:
        print("Wrong answer")
        return 0


def display_score(correct_guesses, guesses, questions):
    print("(------------------)")
    print("Results!")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int(correct_guesses / len(questions) * 100)
    print("Your score is: " + str(score) + "%")


def play_again():

    while True:
        response = input("Do you want to play again? (yes or no): ").upper()
        if response == "YES":
            return True
        elif response == "NO":
            return False
        else:
            print("Enter correct answer! (yes or no): ")


new_game()
while play_again():
    new_game()
print("Thank you for playing!")
