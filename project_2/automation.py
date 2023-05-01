import openpyxl as o
"""import os  #to understand where code is running
print(os.getcwd())"""

inv_file = o.load_workbook("inventory.xlsx")
product_list = inv_file['Sheet1']

#task 1. to find the quantity of products per supplier
profucts_per_supplier = {}
for product_row in range(2, product_list.max_row+1):
    supplier_name = product_list.cell(product_row, 4).value

    if supplier_name in profucts_per_supplier:
        current_num_products = profucts_per_supplier.get(supplier_name)
        profucts_per_supplier[supplier_name] = current_num_products+1
    else:
        profucts_per_supplier[supplier_name] = 1

print(profucts_per_supplier)