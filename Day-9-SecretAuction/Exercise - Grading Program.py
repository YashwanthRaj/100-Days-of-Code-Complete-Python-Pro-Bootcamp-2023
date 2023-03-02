'''
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. 
By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys 
and their grades for values. The final version of the student_grades dictionary will be checked.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key1 in student_scores:
    temp_score = student_scores[key1]
    if temp_score >= 91 and temp_score <= 100:
        student_grades[key1] = 'Outstanding'
    elif temp_score >= 81 and temp_score <= 90:
        student_grades[key1] = 'Exceeds Expectations'
    elif temp_score >= 71 and temp_score <= 80:
        student_grades[key1] = 'Acceptable'
    else:
        student_grades[key1] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)
