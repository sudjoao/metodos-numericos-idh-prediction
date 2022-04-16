def get_g(index, x):
    if index == 1:
        return 1
    return x

def takeResults():
    for i in matrizA:
      final.append(i[len(i)-1])

def getone(pp):
    for i in range(len(matrizA[0])):
        if matrizA[pp][pp] != 1:
            q00 = matrizA[pp][pp]

            for j in range(len(matrizA[0])):
                matrizA[pp][j] = matrizA[pp][j] / q00

def getzero(r, c):
    for i in range(len(matrizA[0])):
        if matrizA[r][c] != 0:
            q04 = matrizA[r][c]
    
            for j in range(len(matrizA[0])):
                matrizA[r][j] = matrizA[r][j] - ((q04) * matrizA[c][j])

def transformMatriz (matrizA, results):
  for i, v in enumerate(results):
    matrizA[i].append(v)
    
  return matrizA

def hdiCalculator(final, ano):
  hdi = final[0] + final[1]*(ano)
  return hdi

years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
hdis = [0.699,0.718,0.742,0.744,0.754,0.757,0.758,0.761,0.762,0.765]
m = len(years)

matrizA = []
results = []
for i in range(1, 3):
    tmp = []
    for j in range(1,3):
        sum = 0
        for k in range(0, m):
            sum += get_g(i, years[k]) * get_g(j, years[k])
        tmp.append(sum)
    matrizA.append(tmp)

for i in range (1, 3):
    sum = 0
    for j in range(0, m):
        sum += hdis[j] * get_g(i, years[j])
    results.append(sum)

transformMatriz(matrizA, results)

for i in range(len(matrizA)):
    getone(i)

    for j in range(len(matrizA)):
        if i != j:
            getzero(j, i)

ano = int(input("Qual ano deseja simular o IDH brasileiro? "))

final = []
takeResults()

hdi = hdiCalculator(final, ano)
print(hdi)