from shared_modules.system_modules import clear_terminal

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }

    student_grades = {}

    grade_value: str = ""

    # mainline statements

    # loop through the student_scores dictionary
    for student_name, student_score in student_scores.items():

        # set grade_value
        if student_score >= 91:
            grade_value = "Outstanding"
        elif student_score >= 81:
            grade_value = "Exceeds Expectations"
        elif student_score >= 71:
            grade_value = "Acceptable"
        else:
            grade_value = "Fail"

        # add record to student_grades dictionary
        student_grades[student_name] = grade_value

    # print the final student_grades dictionary
    print(student_grades)

    return None

if __name__ == '__main__':
    main()
