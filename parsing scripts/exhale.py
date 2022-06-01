import glob
import os
import csv

dict = {}
with open("../data/aprilData/measures.csv","r") as f:
    id = []
    for ln in f:
        if ln.startswith("M1") or ln.startswith("M2") or ln.startswith("M3"):
            dict[ln[:3]] = []
            idx = ln.index("%") + 2
            dict[ln[:3]].append(ln[idx:-2])

i = 0
matrix = []
for directory in glob.glob('../data/aprilData/exhale/*'):
   path = directory + '/*.txt'
   name = os.path.basename(os.path.normpath(directory))[:3]
   for filename in glob.glob(path):
      with open(os.path.join(os.getcwd(), filename), 'r') as f:
         text = [float(x.strip()) for x in f.readlines()]
         row = []
         row.append(str(name + " " + str(dict[name])))
         row += text
         matrix.append(row)

transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
with open("../data/aprilData/training sets/exhale.csv", 'w') as out:
   writer = csv.writer(out)
   for row in transpose:
      writer.writerow(row)