def start(nice=0, mean=0, name=""):
    name = describe_game(name)
    nice_mean(nice, mean, name)

def describe_game(name):
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people.")
                    print("You can choose to be nice or mean, but at the end of the game your fate")
                    print("will be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a conversation. Will you be nice or mean? (N/M) ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice += 1
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly and storms off...")
            mean += 1
            stop = False
    score(nice, mean, name)

def show_score(nice, mean, name):
    print("\n{}, your current total: ({}, Nice) and ({}, Mean)".format(name, nice, mean))

def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
    elif mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    print("\nNice job {}, you win! Everyone loves you and you've made lots of friends along the way!".format(name))
    again(nice, mean, name)

def lose(nice, mean, name):
    print("\nAhhh too bad, game over! {}, you live in a dirty beat-up van by the river...wretched and alone!".format(name))
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N): ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        elif choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO': ")

def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)

# Start the game
start()
