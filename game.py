def new_game():
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
    display_score(correct_guesses,guesses)
def check_answer(answer, guess):
    if answer == guess:
        print("Correct answer!")
        return 1
    else:
        print("Wrong answer")
        return 0


def display_score(correct_guesses,guesses):
    print("(------------------)")
    print("Results!")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    score = int(correct_guesses/len(questions)*100)
    print("Your score is: "+str(score)+"%")

def play_again():
    
    while True:
        response=input("Do you want to play again? (yes or no): ").upper()
        if response=="YES":
            return True
        elif response=="NO":
            return False
        else:
            print("Enter correct answer!")

questions = {
    "What is the name of the main villan in Star Wars?": "A",
    "What is the name of the second planet in the Solar system?": "B",
    "Who is the writer of the LOTR?": "D",
    "Is Earth round?": "B",
}
options = [
    ["A. Darth Vader", "B. Han Solo", "C. Luke Skywalker", "D. Obi Wan Kenobi"],
    ["A. Earth", "B. Venus", "C. Jupiter", "D. Pluto"],
    ["A. J.K.Rowling", "B. Ivan Vazov", "C. Hristo Stoichkov", "D. Tolkin"],
    ["A. No", "B. Yes", "C. Sometimes", "D. What is Earth?"],
]
new_game()
while play_again():
    new_game()
print("Thank you for playing!")
