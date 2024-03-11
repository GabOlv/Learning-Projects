from tkinter import filedialog as files  # Import the file dialog from tkinter
import pandas as pd  # Import pandas library for load excel files

def open_file():
    try:
        # Open the window to select the Excel files
        file_path_1 = files.askopenfilename(title="Select Excel file", filetypes=[("Excel files", "*.xlsx;*.xls")])
        print("File 1: ", file_path_1)
        
        # Prompt the user to enter the sheet name for the first file
        sheet_name1 = input("Enter the sheet name for the first file (press Enter for default): ")
        if sheet_name1 == '':
            sheet_name1 = None  # Default sheet setting if no input
        print("Selected sheet for File 1:", sheet_name1)
        
        # Ask the user to select the second Excel file
        file_path_2 = files.askopenfilename(title="Select Excel file", filetypes=[("Excel files", "*.xlsx;*.xls")])
        print("File 2: ", file_path_2)
        
        # Prompt the user to enter the sheet name for the second file
        sheet_name2 = input("Enter the sheet name for the second file (press Enter for default): ")
        if sheet_name2 == '':
            sheet_name2 = None  # Default sheet setting if no input
        print("Selected sheet for File 2:", sheet_name2)
        
        # Checks if the paths of the two files are valid
        if file_path_1 and file_path_2:
            load_files(file_path_1, sheet_name1, file_path_2, sheet_name2)
        else:
            print("Error")
    except Exception as e:
        # Handle any exceptions that may occur during file selection or user input
        print(e)

def load_files(path1, sheet1, path2, sheet2):
    try:
        # Read Excel files into pandas DataFrames
        if sheet1 is None:
            # If sheet1 is None, set the first sheet of the file
            df1 = pd.read_excel(path1)
        else:
            # If sheet1 is specified, read the specified sheet into DataFrame df1
            df1 = pd.read_excel(path1, sheet_name=sheet1)
            
        if sheet2 is None:
            # If sheet2 is None, set the first sheet of the file
            df2 = pd.read_excel(path2)
        else:
            # If sheet2 is specified, read the specified sheet into DataFrame df2
            df2 = pd.read_excel(path2, sheet_name=sheet2)
        
        # Call the function to compare the contents of two Excel files
        compare_excel(df1, df2)
    except Exception as e:
        # Handle any exceptions that may occur during file reading
        print("Cannot read the files. Error:", e)

def compare_excel(df1, df2):
    # Check if the DataFrames are equal
    if not df1.equals(df2):
        # If DataFrames are not equal, proceed to find differences
        print("Differences between DataFrames:")
        
        # Iterate over the rows of both DataFrames using enumerate
        for idx, (row1, row2) in enumerate(zip(df1.values, df2.values)):
            # Initialize an empty dictionary to store differences for the current row
            row_diff = {}
            
            # Iterate over columns and values of the current row
            for col, val1, val2 in zip(df1.columns, row1, row2):
                # Exclude NaN values from the comparison and check if values are different
                if pd.notna(val1) and pd.notna(val2) and val1 != val2:
                    # If values are different, store the difference in the row_diff dictionary
                    row_diff[col] = (val1, val2)

            # Print the differences of rows
            if row_diff:
                print(f"Row {idx + 2} - File 1: {', '.join(f'{col}={val[0]}' for col, val in row_diff.items())} "
                      f"and File 2: {', '.join(f'{col}={val[1]}' for col, val in row_diff.items())}")
    else:
        # If DataFrames are equal, print a message indicating no differences
        print("No differences found.")

open_file()
i = input("Digite qualquer botão para finalizar...")