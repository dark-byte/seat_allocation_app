
import pandas as pd

def load_student_data(file_path):
    return pd.read_csv(file_path)

def filter_students_by_department(student_df, departments):
    return student_df[student_df['department'].isin(departments)]
