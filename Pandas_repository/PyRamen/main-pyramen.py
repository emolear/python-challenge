import pandas as pd

menu_df = pd.read_csv("C:/Users/erino/UC Berkeley Fintech Bootcamp/UCB-VIRT-FIN-PT-09-2023-U-LOLC/02-Python/Starter_Code/PyRamen/Resources/menu_data.csv")
print(menu_df.head())

sales_df = pd.read_csv("C:/Users/erino/UC Berkeley Fintech Bootcamp/UCB-VIRT-FIN-PT-09-2023-U-LOLC/02-Python/Starter_Code/PyRamen/Resources/sales_data.csv")
print(sales_df.head())

report = {}
for _, sale in sales_df.iterrows():
    quantity = sale["Quantity"]
    menu_item = sale["Menu_Item"]

    if menu_item not in report:
        report[menu_item] = {
            "01-count":0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0
        }

matched_items = menu_df[menu_df["item"] == menu_item]
if not matched_items.empty:
    item_info = matched_items.iloc[0]
    price = item_info["price"]
    cost = item_info["cost"]

    report[menu_item]["01-count"] += quantity
    report[menu_item]["02-revenue"] += price * quantity
    report[menu_item]["03-cogs"] += cost * quantity
    report[menu_item]["04-profit"] += (price - cost) * quantity

else:
    print(f"{menu_item} does not match any item in the menu! NO MATCH!")

with open("C:/Users/erino/Homework_Repos/python-challenge/Pandas_repository/PyRamen/report_output.txt", "w") as file:
    for ramen_type, metrics in report.items():
        file.write(f"{ramen_type}\n")
    for metric_name, metric_value in metrics.items():
        file.write(f" {metric_name}: {metric_value}\n")

 