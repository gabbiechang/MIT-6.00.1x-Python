count = 0
maxCount = 0
result = 0

for i in range(len(s) - 1):
    if (s[i] <= s[i + 1]):
        count += 1
        if count > maxCount:
            maxCount = count
            result = i + 1
    else:
        count = 0

start = result - maxCount
print("Longest substring in alphabetical order is: " + s[start:result + 1])