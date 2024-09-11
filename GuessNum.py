import random

#                       Start
print("""
    {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
    {}..................................................{}
    {}..................................................{}
    {}..._____......................._____._............{}
    {}..|..__.\.....................|_..._|.|...........{}
    {}..|.|..\/_..._..___..___.___....|.|.|.|__...___...{}
    {}..|.|.__|.|.|.|/._.\/.__/.__|...|.|.|.'_.\./._.\..{}
    {}..|.|_\.\.|_|.|..__/\__.\__.\...|.|.|.|.|.|..__/..{}
    {}...\____/\__,_|\___||___/___/...\_/.|_|.|_|\___|..{}
    {}..._..._................._........................{}
    {}..|.\.|.|...............|.|.......................{}
    {}..|..\|.|_..._._.__.___.|.|__...___._.__..........{}
    {}..|...`.|.|.|.|.'_.`._.\|.'_.\./._.\.'__|.........{}
    {}..|.|\..|.|_|.|.|.|.|.|.|.|_).|..__/.|............{}
    {}..\_|.\_/\__,_|_|.|_|.|_|_.__/.\___|_|............{}
    {}..................................................{}
    {}..................................................{}
    {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
      """)

start = True
while start:
    number = random.randint(1,101)
    print("I've chosen a number between 1 and 100.")
    while True:
        difficulty = input("Choose Difficulty (Easy/Medium/Hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            break
        print("Invalid input. Please choose Easy, Medium, or Hard.")
    
    life = {"easy": 10, "medium": 6, "hard": 2}.get(difficulty)
    
    while life > 0:
        print(f"\nLives left: {life}")
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess == number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess > number:
            print("Too high. Try a lower number.")
            if guess - number <= 5:
                print("You're very close!")
        else:
            print("Too low. Try a higher number.")
            if number - guess <= 5:
                print("You're very close!")
        life -= 1
    
    if life == 0:
        print(f"\nGame over! You've run out of lives. The number was {number}.")
    
    while True:
        choice = input("Do you want to play again? (Yes/No): ").lower()
        if choice in ["yes", "no"]:
            break
        print("Invalid input. Please answer Yes or No.")
    
    if choice == 'no':
        break
    print("\n")
    
print("Thanks for playing! THE END")