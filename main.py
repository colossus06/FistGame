''''
-this is a triple quotation mark-
Today is 04.05.22
Ada is eating pasta and meat wathing Cleo and Cuquin
Dancing with the solution theme every time.
'''
# And this is a single line comment
# x = 5 x stores an int
# read the code left to rigt top to bottom

print("Welcome to my first game!")
name = input("What's your name? ")
age = int(input("What's your age? "))

print("Hello " + name + ", you're", age, "years old! ")
health = 10

if age >= 18:
    print("You're old enough to play the game. ")
    want_to_play = input("\nDo you want to play (yes/no)? ").lower()
    if want_to_play == "yes":
        print("\nYou're starting with", health, "health. ")
        print("Let's play! ")
        left_or_right = input("First choice... Left of right (left/right)? ")
        if left_or_right == "left":
            ans = input(
                "Nice, you follow the path and reach a lake... \nDo you swim across or go around (across/around)? "
            )
            if ans == "around":
                print(
                    "You went around and reached the other side of the lake. ")

            elif ans == "across":
                print(
                    "You managed to get across but bit by a baloon fish and lost 5 health. "
                )
                health -= 5
            ans = input(
                "You notice a house and a river. Which do you go to (river/house)? "
            )
            if ans == "house":
                print("You go to the house and greeted by the owner... He doesn't like you. You lose 5 health. ")
                health -= 5
                if health <= 0:
                    print("You now have 0 health, you lose the game! ")
                else:
                    print("You survived... You win the game! ")
            else:
                print("You fell in the river and you lost! ")
                  

        else:
            print("You fell down and lost! ")
    else:
        print("\nSorry to see you go... ")
else:
    print("\nYou're not old enough to play the game... ")
