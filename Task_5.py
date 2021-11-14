# Standardization
# Standardization refers to shifting the distribution of each attribute to have a mean of zero and a standard deviation of one (unit variance).

# It is useful to standardize attributes for a model that relies on the distribution of attributes such as Gaussian processes.

# Normalization
# Normalization refers to rescaling real-valued numeric attributes into a 0 to 1 range.

# Normalization makes the features more consistent with each other, which allows the model to predict outputs more accurately.




import pandas as pd
from Task_1 import Task1
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Task5:
    
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    # All the Tasks associated with this class.
    tasks = [
        "\n1. Normalization using MinMax Scaler will be performed here",
        "2. Standardization using Standard Scaler will be performed here",
        "3. Display the modified Dataset"
    ]
    
    tasks_normalization = [
        "\n1. Entered Column will be normalized",
        "2. Entire dataset will be normalized",
        "3. Display the modified dataset"
    ]

    tasks_standardization = [
        "\n1. ntered Column will be standardized",
        "2. Entire dataset will be standardized",
        "3. Display the modified dataset"
    ]

    def __init__(self, data):
        self.data = data
    
    # Performs Normalization on specific column or on whole dataset.
    def normalization(self):
        while(1):
            print("\nTasks under Normalization\U0001F447")
            for task in self.tasks_normalization:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Sorry..!!...Please try again. We are expecting integer values as input \U0001F974")
                    continue
                break
    
            if choice == -1:
                break
            
            # Performs normalization on the columns provided.
            elif choice == 1:
                print(self.data.dtypes)
                columns = input("Enter all the column"+ self.bold_start + "(s)" + self.bold_end + "you want to normalize (Press -1 to go back)  ").lower()
                if columns == "-1":
                    break
                for column in columns.split(" "):
                    # This is the basic approach to perform MinMax Scaler on a set of data.
                    try:
                        minValue = self.data[column].min()
                        maxValue = self.data[column].max()
                        self.data[column] = (self.data[column] - minValue)/(maxValue - minValue)
                    except:
                        print("\nSorry...this is not possible to perform\U0001F636")
                print("Task accomplished....\U0001F601")

            # Performs normalization on whole dataset.
            elif choice == 2:
                try:
                    self.data = pd.DataFrame(MinMaxScaler().fit_transform(self.data))
                    print("Task accomplished....\U0001F601")

                except:
                    print("\nSince String Columns are present. So, " + self.bold_start + "NOT" + self.bold_end + " possible.\U0001F636\nYou can try the first option though.")
                
            elif choice==3:
                DataDescription.showDataset(self)

            else:
                print("\nPlease try again because you have pressed the wrong key...\U0001F974")

        return

    # Function to perform standardization on specific column(s) or on whole dataset.
    def standardization(self):
        while(1):
            print("\nTasks under Standardization \U0001F447")
            for task in self.tasks_standardization:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Sorry..!!...Please try again. We are expecting integer values as input ")
                    continue
                break

            if choice == -1:
                break
            
            # This is the basic approach to perform Standard Scaler on a set of data.
            elif choice == 1:
                print(self.data.dtypes)
                columns = input("Enter all the column"+ self.bold_start + "(s)" + self.bold_end + "you want to normalize (Press -1 to go back)  ").lower()
                if columns == "-1":
                    break
                for column in columns.split(" "):
                    try:
                        mean = self.data[column].mean()
                        standard_deviation = self.data[column].std()
                        self.data[column] = (self.data[column] - mean)/(standard_deviation)
                    except:
                        print("\nSorry...this is not possible to perform\U0001F636")
                print("Task accomplished..\U0001F601")
                    
            # Performing standard scaler on whole dataset.
            elif choice == 2:
                try:
                    self.data = pd.DataFrame(StandardScaler().fit_transform(self.data))
                    print("Task accomplished..\U0001F601")
                except:
                    print("\nSince String Columns are present. So, " + self.bold_start + "NOT" + self.bold_end + " possible.\U0001F636\nYou can try the first option though.")
                break

            elif choice==3:
                DataDescription.showDataset(self)

            else:
                print("\nPlease try again because you have pressed the wrong key...\U0001F974")

        return

    # main function of the FeatureScaling Class.
    def scaling(self):
        while(1):
            print("\nTasks under Feature Scaling...\U0001F447")
            for task in self.tasks:
                print(task)
            
            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Sorry..!!...Please try again. We are expecting integer values as input \U0001F974")
                    continue
                break
            if choice == -1:
                break
            
            elif choice == 1:
                self.normalization()

            elif choice == 2:
                self.standardization()

            elif choice==3:
                Task1.showDataset(self)
            
            else:
                print("\nPlease select one among values 1,2,3 \U0001F974")
        # Returns all the changes on the DataFrame.
        return self.data