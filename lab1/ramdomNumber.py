import random
#Guessing Game between 0-20

def intVerification():
    #creat a loop and only break if user enters a  integer
    while True:
        # use try to verify input
        try:
           # Get uses input
            number  =int( input())
        except ValueError:
            print("Sorry, I don't understand can you enter as a decimal \n")
            continue

        break
    return number

def main():

    print("Welcome to the random number guess game.\n")
    print("Guess a number between 0-20")

    #gentrate answer
    answer = random.randint(0, 20)
    #keep usere gesing till they get it right
    while True:
        #get valid uers input
        usersGuess = int (intVerification())
        #compare
        if usersGuess < answer:
            print("Too Low")
        elif usersGuess > answer:
            print("Too High")
        elif usersGuess == answer:
            break

    print("you got it !!")
    print("The answer was ", answer)

if __name__ == '__main__':
        main()
