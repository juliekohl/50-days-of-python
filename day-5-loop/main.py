# For Loop with Lists
# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     # print(fruit)
#     print(fruit + " Pie")
#     # print(fruits)
# print(fruits)

# Average Height
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_scores)):
#       student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# total_height = 0
# for height in student_heights:
#     total_height += int(height)
# print(f"total height = {total_height}")
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f"number of students = {number_of_students}")
#
# average_height = round(total_height / number_of_students)
# print(average_height)

# High Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
        # print(highest_score)

print(f"The highest score in the class is: {highest_score}")
