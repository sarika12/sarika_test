# Modules to be used : -
# The series, 11+ 22+ 33+ ... + 1010= 10405071317.
# Find the last ten digits of the series, 11+ 22+ 33+ ... + 10001000.

sum_value = 0
for i in range(1, 1001):
    sum_value = sum_value + pow(i, i)
# print(sum_value)
n = sum_value
a = []
b = []
i = 0
while i < 10:
    rem = n % 10
    a.append(rem)
    n = n // 10
    i = i + 1
# print(a)# print the list of elements
i = 9
# reversed the list
while i >= 0:
    b.append(a[i])
    i = i - 1
#print (b) # print the reveresd elemets
for i in b:
    print(i, end='')
#sarika_test
