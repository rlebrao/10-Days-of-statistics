# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input()
data = list(map(int,(input().split())))
data.sort()
def getMedian(data, size):
    size = int(size)
    dataNumber = []
    for i in data:
        dataNumber.append(int(i))
    dataNumber.sort()
    if(size % 2 == 0):
        return (dataNumber[(int(size/2))] + dataNumber[int(size/2)-1])/2
    else:
        return int(dataNumber[int(((size + 1)/2)) -1])

median = getMedian(data, size)
if(int(size) %2 == 0):
    median_pos = data.index(round(median)+1)
else:
    median_pos = data.index(round(median))
L_half = data[:median_pos]
U_half = data[(median_pos):]

q_two = round(median)
q_one = round(getMedian(L_half, len(L_half)))
q_three = round(getMedian(U_half, len(U_half)))

print(q_one)
print(q_two)
print(q_three)

