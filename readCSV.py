from functions import readCSVData
from typing import List, Dict

# Define path to csv file
path2File: str = '/home/lorenzo/' + 'outputFile.csv'

csvDict: Dict = readCSVData.readCSVdata(path2File)

