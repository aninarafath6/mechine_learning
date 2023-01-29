import random as random


def rpsValidator(uc, cc):
    if (uc == cc):
        print("Tie...!")
    elif (uc == "Paper" and cc == "Rock" or uc == "Scissor" and cc == "Paper" or uc == "Rock" and cc == "Scissor"):
        print("User Wins..")
    else:
        print("Computer wins")
    print("Computer choice : {} and User choice: {}\n\n".format(cc, uc))


while True:
    # Items list
    rps_list = ["Rock", "Paper", "Scissor"]

    # computer choice
    cc = random.choice(rps_list)
    # user choice
    uc = rps_list[int(
        input("Select you option \n1:Rock\n2:Paper\n3:Scissor\n\n"))-1]
    rpsValidator(uc, cc)
