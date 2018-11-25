# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input()
arrData = list(input().split())
arrW = list(input().split())

def getWMean(size, arrData, arrW):
    totalW = sum(map(int,arrW))
    arrData = map(int,arrData)
    values = sum([v * int(arrW[k]) for k,v in enumerate(arrData)])
    return round(values/totalW,1)

print(getWMean(size, arrData, arrW))