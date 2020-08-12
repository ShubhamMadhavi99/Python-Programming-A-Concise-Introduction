
def problem3_1(fileName):

    file_n = open(fileName, "r")
    count = 0

    for line in file_n:
        count += len(line)
        print(line, end='')
    for line in file_n:
        count += len(line)
    print("")
    print('\nThere are '+str(count)+ ' letters in the file.')
    
    
#def problem3_1(txtfilename):
#    file = open(txtfilename)
#    line = file.read()
#    count = 0
#    for lines in line:
#        count = count + 1
#    print("There are " +str(count) + " letters in the file.")
    
        
#txtfilename = "humptydumpty.txt"
#x = problem3_1(txtfilename)
        