newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(newEngland):
    count = 0
    for i in newEngland:
        for j in i:
            count = count + 1
        print(i + " has " + str(count) + " letters.")
        count = 0
    

#x = problem2_3(newEngland)