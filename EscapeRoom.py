# Rita Zhou huan zhou
# 3_escape Room Assignment
# 02/23/2024


print("You are in a room with a door and stairs. Which way will you go?")
user_response = input()

if user_response == "door":
    print("There are 2 buttons on the door. Which do you press?")
    door = int(input())
    if door == 1:
        print("A trap door opens underneath your feet and you fall. GAME OVER")
    elif door == 2:
        print("The door opens. You're free. YOU WIN!")
    else:
        print("You hurt your finger pressing a button that doesn't exist. GAME OVER")
elif user_response == "stairs":
    print("There are 10 cookies on a plate. How many do you eat?")
    cookies = int(input())
    if cookies < 2:
        print("Your friends eat all the rest. You get too hungry and have to quit. GAME OVER")
    elif cookies > 5:
        print("You get a stomach ache and can't search any more. GAME OVER")
    elif 5 >= cookies >= 2:
        print("You notice a secret keypad under the cookie plate. Enter the weight of the remaining cookies in "
              "ounces, if each one weighs 1.5")
        weight = float(input())
        remaining_weight = (10 -cookies) * 1.5
        if weight == remaining_weight:
            print("A secret door opens for you to exit. YOU WIN!")
        else:
            print("Incorrect. GAME OVER")
else:
    print("That's not a valid direction. You trip and fall. GAME OVER")