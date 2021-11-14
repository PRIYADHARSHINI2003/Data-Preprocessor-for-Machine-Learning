import pandas as pd

class Task6:

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    def __init__(self, data):
        self.data = data

    # download the modified DataFrame as .csv file
    def download(self):
        toBeDownload = {}
        for column in self.data.columns.values:
            toBeDownload[column] = self.data[column]

        newFileName = input("\nEnter the " + self.bold_start +"FILENAME" + self.bold_end +" you want? (Press -1 to go back):  ")
        if newFileName=="-1":
            return
        newFileName = newFileName + ".csv"
        # index=False as this will not add an extra column of index.
        pd.DataFrame(self.data).to_csv(newFileName, index = False)
        
        print("Your file is downloaded in your current directory...Please check it\U0001F601")
        
        if input("Please press 'y' to exit or 'n' to continue with modifications in the dataset) ").lower() == 'y':
            print("Leaving the command line interface...Byeeee\U0001F44B")
            exit()
        else:
            return
