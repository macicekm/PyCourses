import pandas as pd

# reading the JSON data using json.load()
file = 'test.json'
df = pd.read_json(file)


# Export to CSV
df.to_csv('testJson.csv',index=0,header=None)

# Export to XLSX

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('testJson.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()