grades = [85, 78, 92, 45, 33, 67, 88, 41]
# a_Categorize each student's grade
def categorize_grades(grades):
    categories = [ ]
    for score in grades:
        if score > 80:
            categories.append (f"Score: {score} - Grade: A")
        elif 60 <= score <= 80:
            categories.append (f"Score: {score} - Grade: B")
        elif 40 <= score < 60:
            categories.append (f"Score: {score} - Grade: C")
        else:
            categories.append (f"Score: {score} - Grade: F")
    return categories

#b_Function to boost grades by 5%
def boost_grades(grades):
    return list(map(lambda x: x * 1.05, grades))

# c_ Find boosted grades above 90
def boosted_grades_above_90(boosted_grades):
    return list(filter(lambda x: x > 90, boosted_grades))

# Categorize grades
grade_categories = categorize_grades(grades)
print("Grade Categories:")
for category in grade_categories:
    print(category)

# Boost grades
boosted_grades = boost_grades(grades)
print("\nBoosted Grades:")
print(boosted_grades)

# Find boosted grades above 90
grades_above_90 = boosted_grades_above_90(boosted_grades)
print("\nBoosted Grades Above 90:")
print(grades_above_90)
