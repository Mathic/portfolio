import pandas as pd

def read_choco_data():
    file_path = "../chocolate/static/chocolate/data/datasets_1919_3310_flavors_of_cacao.csv"
    df = pd.read_csv(file_path)
    print(df.head())

read_choco_data()

# from .models import ChocolateBar
# ModuleNotFoundError: No module named '__main__.models'; '__main__' is not a package
