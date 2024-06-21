import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_countries = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    bc = big_countries[['name', 'area', 'population']]
    return bc
    