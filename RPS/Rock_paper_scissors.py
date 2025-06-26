
def rock_paper_scissors(you):
    import random
    options = ["r","p","s"]
    cpu = random.choice(options)
    cpu_score = 0
    user_score = 0
    
    print(f"the computer choose {cpu} \n")
    # you = input("enter your preferred choice")

    if you == cpu:

        return f"tie \n score is you({user_score}) -- computer({cpu_score})"
    
    if (you == "p" and cpu == "r") or (you == "r" and cpu == "s") or ( you == "s" and cpu == "p"):
        user_score += 1
        return f"You beat the computer\n score is you({user_score}) -- computer({cpu_score})"

    cpu_score += 1
    return f"You got whopped by the computer! Score!  you({user_score}) -- computer({cpu_score})"

for i in range(5):
    test1 = input("Pls enter your preferred choice now  ")
    print(rock_paper_scissors(test1))
    






