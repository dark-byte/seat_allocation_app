from models.classroom import Classroom
from utils.data_loader import load_student_data, group_students_by_department
from utils.seating_utils import generate_seating_pattern

def main():
    num_classrooms = int(input("Enter the number of classrooms: "))
    seats_per_bench = int(input("Enter seats per bench (2 or 3): "))
    max_students_per_classroom = 16 * seats_per_bench  # Each classroom can have up to 48 students for 3 seats per bench

    # Load student data and group by department
    students_df = load_student_data("data/students.csv")
    department_students = group_students_by_department(students_df)
    
    student_blocks = []
    
    # Divide students into blocks of up to 48 students
    for dept, students in department_students:
        student_list = students[['name', 'usn']].values.tolist()
        for i in range(0, len(student_list), max_students_per_classroom):
            student_blocks.append((dept, student_list[i:i + max_students_per_classroom]))

    classroom_count = 0
    while classroom_count < num_classrooms and student_blocks:
        classroom = Classroom(seats_per_bench=seats_per_bench)
        # Each classroom will get up to 48 students or what's left in student_blocks
        students_to_seat = []

        while len(students_to_seat) < max_students_per_classroom and student_blocks:
            dept, block = student_blocks.pop(0)
            students_to_seat.extend(block[:max_students_per_classroom - len(students_to_seat)])
            if len(block) > max_students_per_classroom - len(students_to_seat):
                remaining_block = block[max_students_per_classroom - len(students_to_seat):]
                student_blocks.insert(0, (dept, remaining_block))  # Put remaining students back to be processed

        # Group students by two departments for seating arrangement
        students_dict = {}
        for student in students_to_seat:
            dept = student[1][5:7]  # Extract department code from USN
            if dept not in students_dict:
                students_dict[dept] = []
            students_dict[dept].append(student)

        # Fill the classroom with the available students
        seating_arrangement = generate_seating_pattern(classroom, students_dict)
        classroom.add_seating(seating_arrangement)
        
        print(f"\nSeating Arrangement for Classroom {classroom_count + 1}:")
        for bench in classroom.seating_arrangement:
            print(bench)
        
        classroom_count += 1

if __name__ == "__main__":
    main()
