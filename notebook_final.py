import pandas as pd

# cargo el insumo
dataset_path = r"C:\Users\DELL\Documents\GitHub\proyectofinalLaboDatos\synthetic_customer_data.csv"
data = pd.read_csv(dataset_path)


print(data.head())
print(data.info())
