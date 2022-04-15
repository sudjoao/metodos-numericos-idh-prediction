def get_g(index, x):
    if index == 1:
        return 1
    if index == 2:
        return x
    return x**2


years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
hdis = [0.699,0.718,0.742,0.744,0.754,0.757,0.758,0.761,0.762,0.765]
m = len(years)

a = []
b = []
for i in range(1, 4):
    tmp = []
    for j in range(1,4):
        sum = 0
        for k in range(0, m):
            sum += get_g(i, years[k]) * get_g(j, years[k])
        tmp.append(sum)
    a.append(tmp)

for i in range (1,4):
    sum = 0
    for j in range(0, m):
        sum += hdis[j] * get_g(i, years[j])
    b.append(sum)
print(a)
print(b)
# 10a1 + 20145a2 + 40582185a3 = 7.46
