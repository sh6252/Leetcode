import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    second_highest = salaries.iloc[1]
    
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})