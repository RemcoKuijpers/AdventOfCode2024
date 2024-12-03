# Advent of code 2024 day 1 puzzle

# Read text file
with open("in.txt") as f:
    lines = f.read().splitlines()

# Construct the 2 lists
list1 = []
list2 = []
for line in lines:
    split = line.split()
    list1.append(split[0])
    list2.append(split[1])

# Sort both lists and convert to int
list1.sort()
list2.sort()
list1 = list(map(int, list1))
list2 = list(map(int, list2))

# PART 1
# Compute distances
d = []
for i in range(len(list1)):
    d.append(abs(list1[i]-list2[i]))

# Compute sum of all distances
sum = sum(d)
print(sum)

#PART 2
similarity = 0
for num in list1:
    count = list2.count(num)
    similarity += num * count

print(similarity)
