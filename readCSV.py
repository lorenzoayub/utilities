from functions import readCSVData
import matplotlib.pyplot as plt
from typing import List


fieldsToBeRead = ['Umean']


vetorTempo = []
vetorUMean = []

# Define path to volume report file
path2File: str = '/home/lorenzo/' + 'outputFile.csv'

# Read Volume Report text file
#numberOfLines = readVR.seekNumberOfLines()

csvDict = readCSVData.readCSVdata(path2File)


# Arrays Creation

evolutionVector = [csvDict[i+1]['Time'] for i in range(1,len(csvDict))]
uMeanVector = [csvDict[i+1]['Umean'] for i in range(1,len(csvDict))]
# vetorTempo_Avg = []
# vetorUMean_Avg = []
# steps = 0
# for j in range(len(vetorUMean)):
#     tempo = vetorTempo[j]
#     if tempo == 0.01714:
#         steps = j
#     elif tempo > 0.01714:
#         vetorTempo_Avg.append(tempo)
#         soma = vetorUMean[j]
#         for k in range(j-steps, j):
#             soma = soma + vetorUMean[k]
#         vetorUMean_Avg.append(soma/steps)

#print(uMeanVector)

print(len(evolutionVector))
print(len(uMeanVector))
plt.scatter(evolutionVector, uMeanVector)
# # plt.scatter(vetorTempo_Avg, vetorUMean_Avg, label='averaged')
plt.xlabel('Time')
plt.ylabel('Umean')
plt.legend()
plt.show()
