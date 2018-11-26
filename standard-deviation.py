# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input()
values = list(input().split())

def getMean(data, size):
    total = 0;
    for i in data:
        total += float(i)
    return total / int(size)

mean = getMean(values, size)

variance = sum((int(i) - mean)**2 for i in values)/int(size)
print(round(variance**0.5,1))