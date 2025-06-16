import pandas as pd
import numpy as np

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, employee, left_on='managerId', right_on='id', how='left', suffixes=('', '_manager'))
    result = merged_df[merged_df['salary'] > merged_df['salary_manager']]
    return result[['name']].rename(columns={'name': 'Employee'})