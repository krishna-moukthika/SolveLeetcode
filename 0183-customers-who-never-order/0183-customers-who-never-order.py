import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customer_ids = orders['customerId'].unique()
    filtered_customers = customers[~customers['id'].isin(customer_ids)]
    return filtered_customers[['name']].rename(columns={'name': 'Customers'})
