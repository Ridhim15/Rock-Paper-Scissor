import random
import replit
from colors import *
import os


def gameloop():

    rock = '''  
      _______
  ---'   ____)  
        (_____)  
        (_____)  
        (____)
  ---.__(___)  
  '''

    paper = '''  
      _______
  ---'   ____)____  
            ______)  
            _______)  
           _______)
  ---.__________)  
  '''

    scissors = '''  
      _______
  ---'   ____)____  
            ______)  
         __________)  
        (____)
  ---.__(___)  
  '''
    Rsp = '''
  ██████╗░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░███████╗██████╗░
  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
  ██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝
  ██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
  ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
  
  ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
  ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
  ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
  ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
  ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
  ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░'''

    def greetings():
        width = os.get_terminal_size().columns
        print(f"{Rsp}".center(width) + "\n\n")
        print(
            green + "\^o^/ Greetings fellow traveller" + reset +
            " what brings you here today? \n\nWell since you're already here ( ﾉ ﾟｰﾟ)ﾉ , might I interest you in an"
            + Red + " 'INTENSE'" + Blue + " Game of RSP " + reset +
            "\n\nOh how rude of me , My name is " + Blue +
            "Ruijerd the Great Machine Master" + reset +
            " here in this town , you might haave heard of me!\n\n")
        name = input(
            "Well enough about me lets hear from you , What is your name ?\n")
        print(
            f"\nSo you are {name} yes? Well it dosen't matter anyway im just gonna call you traveller for now...(too much hassel to use name again and again (^///^)) \n "
        )

    def rounds():

        num = (input(
            "༼ つ ◕_◕ ༽つ Go ahead traveller choose what this game of RSP is best of \n(Please choose the number of rounds in digits) Note:  Max rounds = 10\n"
        ))
        is_num = False
        while is_num != True:
            if num.isdigit() == False or int(num) > 10:
                num = (input(
                    "\nTraveller please choose a number less than 10 and in digits\n Please don't enter a negative number\n"
                ))
            else:
                num = int(num)
                is_num = True

        print(
            "Well then as you wish traveller ^_^ \nThis shall be an intense game of ROCK PAPER SCISSOR of between you and my greatest  machine"
            + Blue + " 'Computer'" + reset +
            f" U_U it self \n\nIt shall be best of {num} rounds\n")
        return num

    def rsp():
        greetings()
        num = rounds()
        wrong_choice = 0
        nrounds = 0
        trav_score = 0
        comp_score = 0
        while num > 0:
            nrounds += 1
            print(Red + f"Round {nrounds}" + reset)
            user_choice = int(
                input("What do you choose ---> \n Type " + Blue + " 0" +
                      reset + " for Rock \n Type " + Blue + " 1" + reset +
                      " for Paper  \n Type " + Blue + " 2" + reset +
                      " for Scissors \n"))
            while user_choice > 2:
                wrong_choice += 1
                if wrong_choice == 1:
                    print(
                        Red + "Traveller!" + reset +
                        ", uhh i'll let this one" + green + " slide" + reset +
                        " but next time You " + Red + "Must" + reset +
                        " not chose the option out of bounds \nNow then Try again \n"
                    )
                    user_choice = int(
                        input("What do you choose ---> \n Type " + Blue +
                              " 0" + reset + " for Rock \n Type " + Blue +
                              " 1" + reset + " for Paper  \n Type " + Blue +
                              " 2" + reset + " for Scissors \n"))
                    continue
                else:
                    print(Red + "I warned you there , You lose this round \n" +
                          reset)
                    num -= 1
                    break

            else:
                arr = [rock, paper, scissors]
                comp_choice = random.choice(arr)
                user_choice = arr[user_choice]

                if (user_choice == paper and comp_choice == rock):
                    print(
                        f"You chose {user_choice} \n Computer chose {comp_choice} \n Paper beats Rock "
                        + green + "You Win" + reset + "\n")
                    trav_score += 1
                    print(
                        f"Score Board : Traveller's Score : Computer's Score \n\t\t\t\t\t\t{trav_score} \t\t: \t\t\t{comp_score}\n "
                    )
                if (user_choice == scissors and comp_choice == paper):
                    print(
                        f"You chose {user_choice} \n Computer chose {comp_choice} \n Scissor cuts Paper "
                        + green + "You Win" + reset + "\n")
                    trav_score += 1
                    print(
                        f"Score Board : Traveller's Score : Computer's Score \n\t\t\t\t\t\t{trav_score} \t\t: \t\t\t{comp_score} \n"
                    )
                if (user_choice == rock and comp_choice == scissors):
                    print(
                        f"You chose {user_choice} \n Computer chose {comp_choice} \n Rock beats Scissors "
                        + green + "You Win" + reset + "\n")
                    trav_score += 1
                    print(
                        f"Score Board : Traveller's Score : Computer's Score \n\t\t\t\t\t\t{trav_score} \t\t: \t\t\t{comp_score}\n "
                    )
                if (user_choice == rock and comp_choice == paper):
                    print(
                        f"You chose {user_choice} \n Computer chose {comp_choice} \n Paper beats Rock "
                        + Red + "You Lose" + reset + "\n")
                    comp_score += 1
                    print(
                        f"Score Board : Traveller's Score : Computer's Score \n\t\t\t\t\t\t{trav_score} \t\t: \t\t\t{comp_score}\n "
                    )
                if (user_choice == scissors and comp_choice == rock):
                    print(
                        f"You chose {user_choice} \n Computer chose {comp_choice} \n Rock beats Scissors "
                        + Red + "You Lose" + reset + "\n")
                    comp_score += 1
                    print(
                        f"Score Board : Traveller's Score : Computer's Score \n\t\t\t\t\t\t{trav_score} \t\t: \t\t\t{comp_score}\n "
                    )
                if (user_choice == paper and comp_choice == scissors):
                    print(
                        f"You chose {user_choice} \n Computer chose {comp_choice} \n Scissors cuts Paper "
                        + Red + "You Lose" + reset + "\n")
                    comp_score += 1
                    print(
                        f"Score Board : Traveller's Score : Computer's Score \n\t\t\t\t\t\t{trav_score} \t\t: \t\t\t{comp_score}\n "
                    )
                if (user_choice == comp_choice):
                    print(
                        f"You chose {user_choice} \n Computer chose {comp_choice} \n "
                        + magenta + "It's a draw" + reset + "\n")
                    print(
                        f"Score Board : Traveller's Score : Computer's Score \n\t\t\t\t\t\t{trav_score} \t\t: \t\t\t{comp_score} \n"
                    )
                num -= 1
        if trav_score > comp_score:
            print(
                Green + "Well Done Traveller \(￣︶￣*\))" + reset +
                " You have insane luck or your truly skilled \n\nWell thats about it for now see you next time. \n"
            )
        elif trav_score == comp_score:
            print(
                "To think you could compare to my greatest machine , interesting \nI think i'll do some changes , we shall meet again traveller , next time I will not fault in perfecting my machine"
            )
        else:
            print(
                "HA! As expected a mere passerby can't beat my years of work on this machine,"
                + magenta +
                "\n(Emotional Damage : Max \nDepression : 10^infinity)" +
                reset +
                "\nEven though its moves are random it still makes a calculated choice \n "
                + red + "(I wish ヾ(￣▽￣))" + reset +
                " \nCome back when you've honed your skills traveller\n" +
                red +
                "(Traveller loses faith in his abilities after losing miserably to Ruijerd's machine) \n "
                + reset)

    while True:
        rsp()
        play_again = input(
            "Do you want to Play again press Y for Yes and N for No \n")
        if play_again.lower() == 'n':
            break
        replit.clear()


gameloop()
