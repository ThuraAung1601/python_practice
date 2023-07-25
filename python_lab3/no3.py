import random
player = int(input("scissor(0), rock(1), paper(2): "))
computer = random.randint(0,2)

if player != 0 or player != 1 or player != 2:
    if computer == 0 and player == 2:
        print("The computer is scissor. You are paper. You lose.")
    elif computer == 2 and player == 0:
        print("The computer is paper. You are scissor. You won.")

    elif computer == 0 and player == 1:
        print("The computer is scissor. You are rock.  You won.")
    elif computer == 1 and player == 0:
        print("The computer is rock. You are scissor. You lose.")

    elif computer == 1 and player == 2:
        print("The computer is rock. You are paper. You won.")
    elif computer == 2 and player == 1:
        print("The computer is paper. You are rock. You lose.")

    elif computer == player:
        if computer == 0 or player == 0:
            print("The computer is scissor. You are scissor. It is a draw.")
        elif computer == 1 or player == 1:
            print("The computer is rock. You are rock. It is a draw.")
        elif computer == 2 or player == 2:
            print("The computer is paper. You are paper. It is a draw.")
else:
    print("Please input within range 0-2!")
