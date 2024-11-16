# Student Average Score Calculation

import numpy as np

def calculate_highest_average(scores):
    # Calculate the average score for each student
    averages = np.mean(scores, axis=1)
    
    # Identify the student with the highest average score
    highest_average_index = np.argmax(averages)
    highest_average_score = averages[highest_average_index]
    
    print(f"Student {highest_average_index + 1} has the highest average score: {highest_average_score}")

# Example dataset of students' scores
student_scores = np.array([[85, 90, 78],
                            [88, 92, 95],
                            [70, 75, 80]])

calculate_highest_average(student_scores)
