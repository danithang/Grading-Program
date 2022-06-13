student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#taking the key(each student)
for student in student_scores:
    #score is calculating the value of out of the dictionary using the key
    score = student_scores[student]
    #if, elif, else statements to determine the what the scores represent
    if score > 90:
        #taking the empty dictionary of student_grades and giving it a value of the key(student) and it will print which statement pertains to each student's grade
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)





