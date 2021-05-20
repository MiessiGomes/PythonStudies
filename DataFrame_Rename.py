import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xlsxwriter
import numpy as np

url_dados = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'
dados = pd.read_csv(url_dados, compression = 'zip')
print(type(dados))

for x in range(0, 1000):
    test = 'test'
    dados.columns = dados.columns.str.replace('-', '')
print(dados)

write = pd.ExcelWriter('dataExcel.xlsx')

dados.to_excel(write, sheet_name = 'Planilha', index = False)

write.save()