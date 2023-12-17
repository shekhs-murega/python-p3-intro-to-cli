#!/usr/bin/env python3

import os

def create_grade_report(student_grades):
    os.makedirs('reports', exist_ok=True)  # Ensure 'reports' directory exists
    file_path = os.path.join('reports', 'grade_report.txt')  # Proper file path

    with open(file_path, 'w') as gr:
        for grade in student_grades:
            gr.write(grade + '\n')

if __name__ == '__main__':
    student_grades = []

    grade = input("Student name, grade: ")
    while grade:
        student_grades.append(grade)
        grade = input("Student name, grade: ")

    create_grade_report(student_grades)
