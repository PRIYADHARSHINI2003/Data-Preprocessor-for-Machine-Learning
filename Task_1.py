
# describe():
# The describe() method is used for calculating some statistical data like percentile, mean and std of the numerical values of the Series or DataFrame.

# It analyzes both numeric and object series and also the DataFrame column sets of mixed data types.

# The describe() function is used to generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding NaN values.

# info():
# The info() method prints information about the DataFrame.

# The information contains the number of columns, column labels, column data types, memory usage, range index, and the number of cells in each column (non-null values).

# The info() function is used to print a concise summary of a DataFrame.

# This method prints information about a DataFrame including the index dtype and column dtypes, non-null values

import pandas as pd



class Task1:
# The "tasks" variable will storing the list of three different tasks under "Describing the data based on choice entered by the user".
    tasks = [
        '\n1. Description of a specified column ',
        '2. Display Column Properties',
        '3. Display the modified Dataset'
    ]

    def __init__(self, data):
        self.data = data

    # The function that prints the database on the command line.
    def showDataset(self):
        while(1):
            try:
                rows = int(input(("\nPlease enter the number of rows to display...(Press -1 to go back)  ")))
                if rows == -1:
                    break
                if rows <= 0:
                    print("Enter a positive integer...\U0001F974")
                    continue
                print(self.data.head(rows))
            except ValueError:
                print("Sorry..!!...Please try again. We are expecting integer values as input \U0001F974")
                continue
            break
        return

    # function to print all the columns
    def showColumns(self):
        for column in self.data.columns.values:
            print(column, end="  ")

    # function to describe the dataset or any specific column.
    def describe(self):
        while(1):
            print("\nTasks under Data Description...\U0001F447")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nPlease enter your choice...(Press -1 to go back)  ")))
                except ValueError:
                    print("Sorry..!!...Please try again. We are expecting integer values as input \U0001F974")
                    continue
                break

            if choice==-1:
                break
                        
            elif choice==1:
                self.showColumns()
                while(1):
                    describeColumn = input("\n\nPlease enter the column name so that we could give the description about it").lower()
                    try:
                        # describe() function is used to tell all the info regarding any specific column.
                        print(self.data[describeColumn].describe())
                    except KeyError:
                        print("Sorry..!!..Column not found...Please netr the correct column name\U0001F974")
                        continue
                    break
            
            elif choice==2:
                # describe() function is used to tell all the info about the database.
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())

            elif choice==3:
                self.showDataset()

            else:
                print("\nPlease select one among values 1,2,3 \U0001F974")
