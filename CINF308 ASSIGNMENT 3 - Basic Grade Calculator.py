'''
Ask user to input five grades for processing
Assign user input to array(list)
Open file in write mode
Write each grade to the file
Close file
Reopen file in read mode
Read all grades into a list
Pull grades from list and assign to individual int/float variables
Perform operations to find grade average, highest and lowest grades
Print results and display to user
End program
'''

file = open ( 'grade_report.txt' , 'w' )

#Basic user input, adds input to a list and splits into individual items
uGrades = []
uInput = input("Please input 5 grades you would like to calculate the average for (WITH NO COMMAS): ")
uGrades = uInput.split()


#Write inputted grades to file, close and reopen, read file and write values to new list
with open('grade_report.txt', 'w') as f:
    for item in uGrades:
        f.write(f"{item}\n")
file.close


file = open ('grade_report.txt' , 'r')
with open ('grade_report.txt', 'r') as f:
    gradesF = f.read().splitlines()


#Find the average of the inputted grades
g1 = int(gradesF[0])
g2 = int(gradesF[1])
g3 = int(gradesF[2])
g4 = int(gradesF[3])
g5 = int(gradesF[4])

gSum = g1 + g2 + g3 + g4 + g5
gAvg = gSum/5

#Convert string list to int list, find max and min
gInt = list(map(int, gradesF))
gMax = max(gInt)
gMin = min(gInt)

#Convert the list of grades to a string for output
sep = ", "
gfStr = sep.join(gradesF)


print("Inputted Grades: " + gfStr + """\n
\n
""" + "Average GPA: " + str(gAvg) + "\n" + "Highest Grade: " + str(gMax) + "\n" + "Minimum Grade: " + str(gMin))



