import pandas as pd

# Assuming jomashop and ITEMS are DataFrames
# Make sure to replace 'DATE', 'ITEM_NUMBER', and 'DATE_ADDED' with your actual column names

# Filtering the jomashop DataFrame
filtered_jomashop = jomashop[(jomashop['DATE'] > '09-01-2024') & (jomashop['ITEM_NUMBER'].isin(ITEMS['ITEM_NUMBER']))]

# Sorting the filtered DataFrame by DATE_ADDED in descending order
result = filtered_jomashop.sort_values(by='DATE_ADDED', ascending=False)

# Displaying the result
print(result)
