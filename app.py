
from models.classroom import Classroom
from utils.data_loader import load_student_data, filter_students_by_department
from utils.seating_utils import generate_seating_pattern

def main():
    # Gather user input
    num_classrooms = int(input("Enter the number of classrooms: "))
    benches = int(input("Enter the number of benches per classroom: "))
    seats_per_bench = int(input("Enter seats per bench (2 or 3): "))
    
    departments = []
    for i in range(2):
        departments.append(input(f"Enter department {i + 1}: "))

    # Load and filter student data
    students_df = load_student_data("data/students.csv")
    filtered_students = filter_students_by_department(students_df, departments)

    # Process each classroom
    for _ in range(num_classrooms):
        classroom = Classroom(benches, seats_per_bench, departments)
        seating_arrangement = generate_seating_pattern(classroom, filtered_students)
        print("\nSeating Arrangement:")
        for bench in seating_arrangement:
            print(bench)

if __name__ == "__main__":
    main()
