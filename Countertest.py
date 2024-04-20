from collections import Counter
A = "vnpbeutxfqxriiajoejjmtjcx"

print(Counter(A))
count=0
for i in Counter(A).keys():
    count=+Counter(A).get(i)%2

print(count)
