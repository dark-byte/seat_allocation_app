import pandas as pd

def load_student_data(file_path):
    data = pd.read_csv(file_path)
    # Extract department from the USN
    data['department'] = data['usn'].apply(lambda usn: usn[5:7].upper())
    data = data.sort_values(by=['department', 'usn'])
    return data

def group_students_by_department(student_df):
    return student_df.groupby('department')
