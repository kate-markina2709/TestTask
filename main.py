import pandas as pd
import numpy as np
import sys

# При запуске аргументы: 0 - название файла программы (main.py), 1 - название конфигурационного файла, 2 - название файла данных
conf_ = sys.argv[1]
conf = pd.read_csv(conf_, sep='=', header=None)
#conf = pd.read_table("conf.txt", sep='=', header=None)
data_ = sys.argv[2]
data = open(data_).readlines()
#data = open("data.txt").readlines()
replace_let = np.zeros(len(data), dtype=np.int8)

for i in range(len(data)):
    data[i] = data[i].replace('\n', '')
    for j in range(len(conf)):
        replace_let[i] += data[i].count(conf[0][j])
        if conf[0][j] in data[i]:
            data[i] = data[i].replace(conf[0][j], conf[1][j])
result = {replace_let[i]:data[i] for i in range(len(data))}
result = sorted(result.items(), reverse=True)
a = result[0][1]
for k in range(len(data)):
    print(result[k][1])


