"""
percentages for reference -
    A+	97%+	
    A	93%-96%	
    A-	90%-92%	
    B+	87%-89%	
    B	83%-86%	
    B-	80%-82%	
    C+	77%-79%	
    C	73%-76%	
    C-	70%-72%	
    D+	67%-69%	
    D	63%-66%	
    D-	60%-62%	

"""

classes = []
grades = []

#collects class name + grade
def collect():
    n = 0
    classNum = int(input("Input the number of classes you have: "))
    classNum = classNum - 1
    while (n <= classNum):
        className = input("Enter class name: ")
        classes.append(className)
        n = n + 1

    print(classes)
    g = 0

    while (g <= classNum):
        grade = input("Enter letter grade: ")
        grade = grade.upper()
        grades.append(grade)
        g = g + 1
    calculate()

#calculates gpa value
def calculate():
    total = 0
    for element in grades:
        if element == "A+":
            total = total + 4.0
        elif element == "A":
            total = total + 4.0
        elif element == "A-":
            total = total + 3.7
        elif element == "B+":
            total = total + 3.3
        elif element == "B":
            total = total + 3.0
        elif element == "B-":
            total = total + 2.7
        elif element == "C+":
            total = total + 2.3
        elif element == "C":
            total = total + 2.0
        elif element == "C-":
            total = total + 1.7
        elif element == "D+":
            total = total + 1.3
        elif element == "D":
            total = total + 1.0
    gpa = total / len(classes)
    print(gpa)

collect()

