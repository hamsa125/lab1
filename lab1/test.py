import random

def main():
    print("Welcome to the random number game.\n")
    print("To start off pleas enter the game's ranges \n ")
    answer = random.randint(0, 20)
    print(answer)
    guess = 0
    while True:
        guess = guess + 1
        print(answer)
        print(guess)
        cs = int(input())
        print(cs)
        if cs < answer: print("Too Low")
        elif cs > answer: print("Too High")

        break
    print("you got it ", guess)
    print(" Do you want to play agin")

if __name__ == '__main__':
        main()