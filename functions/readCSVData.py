from typing import Dict, List, Any, Union
import csv


def seekSize(fileArg: Union[str, List]) -> Dict[str, int]:
    numLinhas: int = 0
    numColunas: int = 0

    if type(fileArg) is str:
        with open(fileArg) as file:
            linhas: List = file.readlines()
            numLinhas: int = len(linhas)
            numColunas: int = len(linhas[0])
    elif type(fileArg) is list:
        numLinhas: int = len(fileArg)
        numColunas: int = len(fileArg[0])
    return {'rows': numLinhas, 'columns': numColunas}


def readCSVdata(csvPath: str, cabecalho='none') -> Dict:

    # Creates dict to be returned
    csvInfo: Dict[int, Any] = {}
    
    tamanho: Dict[str, int] = seekSize(csvPath)
    
    # Read CSV file
    with open(csvPath) as file:
        csvreader = csv.reader(file)
        linhas: List = list(csvreader) 
        numLines: int = tamanho['rows']
        numColumns: int = tamanho['columns']
       
        if cabecalho == 'rows': 
            for j in range(1, numLines):
                csvInfo[j+1] = {}
                for coluna in range(numColumns):
                    if '(' in linhas[j][coluna]:
                        csvInfo[j+1][linhas[0][coluna]] = linhas[j][coluna]
                    else:
                        csvInfo[j+1][linhas[0][coluna]] = float(linhas[j][coluna])
 
        elif cabecalho == 'columns': 
            for j in range(1, numColumns):
                csvInfo[j+1] = {}
                for k in range(numLines):
                    if '(' in linhas[j][coluna]:
                        csvInfo[j+1][linhas[j][0]] = linhas[j][k]
                    else:
                        csvInfo[j+1][linhas[j][0]] = float(linhas[j][k])

        elif cabecalho == 'none': 
            pass

    return csvInfo


if __name__ == '__main__':
    path2VolumeReport: str = '/home/lorenzo/' + 'outputFile.csv'
    readCSVdata(path2VolumeReport)

