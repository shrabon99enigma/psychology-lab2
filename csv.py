import pandas as pd

df = pd.DataFrame({
    "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015],
    "Date": [
        "2025-01-01","2025-01-02","2025-01-03","2025-01-04","2025-01-05",
        "2025-01-06","2025-01-07","2025-01-08","2025-01-09","2025-01-10",
        "2025-01-11","2025-01-12","2025-01-13","2025-01-14","2025-01-15"
    ],
    "Product": [
        "Laptop","Mouse","Keyboard","Monitor","Printer",
        "Desk","Chair","Pen","Notebook","USB Drive",
        "Table","Sofa","Book","Calculator","Headphones"
    ],
    "Category": [
        "Electronics","Electronics","Electronics","Electronics","Electronics",
        "Furniture","Furniture","Stationery","Stationery","Electronics",
        "Furniture","Furniture","Stationery","Stationery","Electronics"
    ],
    "Sales": [
        50000,1500,2500,12000,18000,
        10000,7000,300,1200,2500,
        15000,35000,800,2200,4500
    ]
})

df.to_csv("sales_data.csv", index=False)
print("sales_data.csv created successfully!")