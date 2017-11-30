import numpy as np

listcount = []
liststr = []
rows = []
cols = []
# read graph.txt
f = open("graph.txt")
line = f.readline()

# get the row and column of the array to be created
while line:
    listcount = line.split()
    liststr.append(listcount)
    rows.append(listcount[0])
    cols.append(listcount[1])
    line = f.readline()
row = int(max(rows))+1
col = int(max(cols))+1
a = np.zeros((row, col))    # create the array
f.close()
n = row

# give value to the array
for i in liststr:
    row = int(i[0])
    col = int(i[1])
    a[row][col] = float(i[2])

# make Matrix M
b = np.transpose(a)
m = np.zeros(b.shape)
for i in range(b.shape[0]):
    for j in range(b.shape[1]):
        if a[j].sum() == 0:
            m[i][j] = 0
        else:
            m[i][j] = b[i][j] / (a[j].sum())
print("Matrix M :")
print(m)

# initialize rj
rj = np.zeros((m.shape[0], 1))
for i in range(m.shape[0]):
    rj[i] = float(1) / m.shape[0]
print("Original rank vector (rj):")
print(rj)

# PageRank
beta = 0.85
count = 0
while not (rj == beta * np.dot(m, rj) + (1 - beta) / n).all():
    rj = beta*np.dot(m, rj) + (1-beta)/n
    count += 1
print("Converged rank vector (R):")
print(rj)
print("Iteration counts:")
print(count)
