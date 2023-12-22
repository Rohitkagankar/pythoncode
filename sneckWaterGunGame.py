import random
while True:
    play=input("enter 1 for play and any key for exit: ")
    if play=="1":
        you = input("choose sneck, water, gun (s,w,g): ")
        choice=['s','w','g']
        if( you not in choice):
            print("you enter wrong choice,choose(s,w,g).")
            continue
        ranChoice = random.choice(choice)
        print("computer choice =", ranChoice)
        if you == ranChoice:
            print("Game Draw...")
        elif (you=="s" and ranChoice=="w") or (you=="g" and ranChoice=="s") or (you=="w" and ranChoice=="g"):
            print("congratulations.you win...")
        elif (you=="w" and ranChoice=="s") or (you=="s" and ranChoice=="g") or (you=="g" and ranChoice=="w"):
            print("you lose...")
    else:
        print("thenk you...")
        break

