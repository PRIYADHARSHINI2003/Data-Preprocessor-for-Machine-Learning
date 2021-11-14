# One Hot Encoder
# A one hot encoding is a representation of categorical variables as binary vectors.

# This first requires that the categorical values be mapped to integer values.

# Then, each integer value is represented as a binary vector that is all zero values except the index of the integer, which is marked with a 1.

# Label Encoder
# Label Encoding refers to converting the labels into a numeric form so as to convert them into the machine-readable form.

# Machine learning algorithms can then decide in a better way how those labels must be operated.

# It is an important pre-processing step for the structured dataset in supervised learning.





import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from Task_1 import Task1

class Task4:
    # The Task associated with this class.
    tasks = [
        '\n1. Display the columns which are categorical',
        '2. One Hot Encoding to change selected categorical data parameters',
        '3. Display the modified Dataset'
    ]
    def __init__(self, data):
        self.data = data

    # function to show all the categorical columns and number of unique values in them.
    def categoricalColumn(self):
        print('\n{0: <20}'.format("Categorical Column") + '{0: <5}'.format("Unique Values"))
        # select_dtypes selects the columns with object datatype(which could be further categorize)
        for column in self.data.select_dtypes(include="object"):
            print('{0: <20}'.format(column) + '{0: <5}'.format(self.data[column].nunique()))

    # function to encode any particular column
    def encoding(self):
        categorical_columns = self.data.select_dtypes(include="object")
        while(1):
            column = input("\nEnter the choice of your column which you would like to Hot Encode..(Press -1 to go back)  ").lower()
            if column == "-1":
                break
            # The encoding function is only for categorical columns.
            if column in categorical_columns:
                self.data = pd.get_dummies(data=self.data, columns = [column])
                print("One Hot Encoding accomplished.....\U0001F601")
                
                choice = input("Do you want to continue One Hot Encoding..??(y/n)  ")
                if choice == "y" or choice == "Y":
                    continue
                else:
                    self.categoricalColumn()
                    break
            else:
                print("Please try again..No such column exists\U0001F974")

    # The main function of the Categorical class.
    def categoricalMain(self):
        while(1):
            print("\nTasks\U0001F447")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required. Try again...\U0001F974")
                    continue
                break

            if choice == -1:
                break
            
            elif choice == 1:
                self.categoricalColumn()

            elif choice == 2:
                self.categoricalColumn()
                self.encoding()

            elif choice == 3:
                Task1.showDataset(self)

            else:
                print("\nPlease select one among values 1,2,3 \U0001F974")
        # return the data after modifying
        return self.data
