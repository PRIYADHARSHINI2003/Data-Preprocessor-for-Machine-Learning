from Task_1 import Task1
from Task_2 import Task2
from Task_3 import Task3
from Task_4 import Task4
from Task_5 import Task5
from Task_6 import Task6


class Task:

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"
    
    # The Task associated with this class. This is also the main class of the project.
    tasks = [
        '1. Describing the data based on choice entered by the user',
        '2. Encoding Variable to Number to fit the requirements of Machine Learning Model',
        '3. Scaling of a particular feature in the Dataset (Standardization & Normalization)',
        '4. Final Dataset download after modifications',
        '5. Null values/Missing values on dataset are replaced according to users choice '
    ]

    data = 0
    
    def __init__(self):
        self.data = Task2().inputFunction()
        print("\n\n" + self.bold_start + "WELCOME TO DATA PREPROCESSOR FOR MACHINE LEARNING!!!" + self.bold_end + "\n\n")

    # function to remove the target column of the DataFrame.
    def removeTargetColumn(self):
        print("Columns\U0001F447\n")
        for column in self.data.columns.values:
            print(column, end = "  ")
        
        while(1):
            column = input("\nWhich is the target variable:(Press -1 to exit)  ").lower()
            if column == "-1":
                exit()
            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                try:
                    self.data.drop([column], axis = 1, inplace = True)
                except KeyError:
                    print("No column present with this name. Try again......\U0001F974")
                    continue
                print("Done.......\U0001F601")
                break
            else:
                print("Try again with the correct column name...\U0001F974")
        return
    
    def printData(self):
        print(self.data)

    # main function of the Preprocessor class.
    def preprocessorMain(self):
        self.removeTargetColumn()
        while(1):
            print("\nTasks (Preprocessing)\U0001F447\n")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input("\nWhat do you want to do? (Press -1 to exit):  "))
                except ValueError:
                    print("Integer Value required. Try again.....\U0001F974")
                    continue
                break

            if choice == -1:
                exit()

            # moves the control into the DataDescription class.
            elif choice==1:
                Task1(self.data).describe()


            # moves the control into the Imputation class.
            elif choice==2:
                self.data = Task4(self.data).categoricalMain()


            # moves the control into the FeatureScaling class.
            elif choice==3:
                self.data = Task5(self.data).scaling()


            # moves the control into the Download class.
            elif choice==4:
                Task6(self.data).download()
            
            elif choice==5:
                self.data=Task3(self.data).imputer()

            else:
                print("\nWrong Integer value!! Try again..\U0001F974")

# obj is the object of our Preprocessor class(main class).
obj = Task()
# the object 'obj' calls the main function of our Preprocessor class.
obj.preprocessorMain()