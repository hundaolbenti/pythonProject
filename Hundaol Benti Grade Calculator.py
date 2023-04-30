Hundaol
from tabulate import tabulate
name = str(input("Enter your name :"))#this takes input of name from the user
section = int(input("Enter your section :"))
ID_no = str(input("Enter your ID :"))
Year = int(input("Enter the year :"))
print("--------------------------------")
print("|","name |","Section |","ID :")
print(name,"   ",section," ",ID_no)
print("--------------------------------")
def Grade_calculator():

    score = int(input("Enter your score :"))
    table_data = [['Name', 'Section', 'ID No.', 'Year', 'Score', ],
                  [name, section, ID_no, Year, score]]
    if score>=90 and score<100:
        print("A+")
    elif score>=85 and score<90:
        print("A")
    elif score>=80 and score<85:
        print("A-")
    elif score>=75 and score<80:
        print("B+")
    elif score>=70 and score<75:
        print("B")
    elif score>=65 and score<70:
        print("B-")
    elif score>=60 and score<65:
        print("C+")
    elif score>=55 and score<60:
        print("C")
    elif score>=50 and score<55:
        print("C-")
    elif score>=45 and score<50:
        print("D")
    elif score>=40 and score<45:
        print("F")
    else:
        print("invalid score")
    repeat = input("Would you like to run again yes/ no :")
    if repeat == "yes":
        Grade_calculator()
    else:
        print(tabulate(table_data, headers="firstrow",tablefmt="fancy_grid"))
        print("Thanks for using ---Hundaol")
        exit()
Grade_calculator()





