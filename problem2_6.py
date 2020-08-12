import random 

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.

    random.seed(431)  # don't remove when you submit for grading
    for r1 in range(0,100):
        L1 = (random.randint(1,6))
        L2 = (random.randint(1,6))

        print(L1+L2)