size = input()
data = list(input().split())

def getMean(data, size):
    total = 0;
    for i in data:
        total += float(i)
    return total / int(size)

def getMedian(data, size):
    size = int(size)
    dataNumber = []
    for i in data:
        dataNumber.append(float(i))
    dataNumber.sort()
    if(size % 2 == 0):
        return (dataNumber[(int(size/2))] + dataNumber[int(size/2)-1])/2
    else:
        return dataNumber[dataNumber[((size + 1)/2)]]

def getMode(data, size):
    dataNumber = []
    for i in data:
        dataNumber.append(float(i))
    data = dataNumber
    d = {k:0 for k in data}
    for i in data:
        d[i] = data.count(i)
        sumTotal = 0
    for (k,v) in d.items():
        sumTotal += v
    if(sumTotal == int(len(set(data)))):
        return min(set(data))
    else:
        mValue = d[max(d, key=d.get)]
        unique = [k for (k,v) in d.items() if v == mValue]
        return min(unique)

print(getMean(data, size))
print(getMedian(data,size))
print(getMode(data,size))