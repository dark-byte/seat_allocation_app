
import random

def generate_seating_pattern(classroom, students):
    seating_arrangement = []
    benches = classroom.benches
    seats_per_bench = classroom.seats_per_bench
    dep1, dep2 = classroom.departments

    dep1_students = students[students['department'] == dep1].values.tolist()
    dep2_students = students[students['department'] == dep2].values.tolist()
    
    if seats_per_bench == 2:
        for bench in range(benches):
            seating_arrangement.append([dep1_students.pop(0), dep2_students.pop(0)])
    elif seats_per_bench == 3:
        for bench in range(benches):
            seating_arrangement.append([
                dep1_students.pop(0),
                dep2_students.pop(0),
                dep1_students.pop(0) if bench % 2 == 0 else dep2_students.pop(0)
            ])
    return seating_arrangement
