import openpyxl

# Taxonomy: Workbook -> Sheet -> Cell
# IMPORTANT: Sheets are indexed from 0, Rows and Columns are indexed from 1.

# Example 1: Open and Read existing Excel file

example_wb = openpyxl.load_workbook('example.xlsx')
example_sheet = example_wb['Sheet1']
print(example_sheet['A1'].value)
print(example_sheet.cell(row=1, column=1).value)

# Input = Cell's name

searchTerm = ''
while searchTerm != '0':
    if searchTerm != '':
        print(example_sheet[searchTerm].value)
    searchTerm = input()

# Example 2: Create a workbook, write in it, then save it to the hard drive

# Create new workbook
wb = openpyxl.Workbook()
print(wb.sheetnames)

# Rename sheet
first_sheet = wb['Sheet']
first_sheet.title = 'Hello there'

# Write
first_sheet['A1'].value = 'First cell'
first_sheet['A2'].value = 100

# Save
wb.save('hello.xlsx')
