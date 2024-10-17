def generate_seating_pattern(classroom, department_students):
    seating_arrangement = []
    benches = classroom.benches
    seats_per_bench = classroom.seats_per_bench
    
    # Extract department names directly from the dictionary keys
    dept_keys = list(department_students.keys())
    
    if len(dept_keys) > 2:
        raise ValueError("Only up to two departments are supported per classroom.")
    
    dept1, dept2 = dept_keys[0], (dept_keys[1] if len(dept_keys) > 1 else None)
    students1 = department_students[dept1]
    students2 = department_students[dept2] if dept2 else []

    for bench in range(benches):
        if seats_per_bench == 3:
            if dept2 and students1 and students2:
                # Alternate: Dept1 - Dept2 - Dept1
                left = students1.pop(0) if students1 else None
                middle = students2.pop(0) if students2 else None
                right = students1.pop(0) if students1 else None
                seating_arrangement.append([left, middle, right])
            elif students1:  # Handle single department case
                left = students1.pop(0) if students1 else None
                middle = students1.pop(0) if students1 else None
                right = students1.pop(0) if students1 else None
                seating_arrangement.append([left, middle, right])
                
        if len(seating_arrangement) >= benches:
            break  # Stop once we reach 16 benches

    return seating_arrangement
