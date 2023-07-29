'''You decide to go for a very long drive on a very straight road. Along this road are five cities. As
you travel, you record the distance between each pair of consecutive cities.
You would like to calculate a distance table that indicates the distance between any two of the cities
you have encountered.
Input Specification
The first line contains 4 positive integers less than 1000, each representing the distances between
consecutive pairs of consecutive cities: specifically, the ith integer represents the distance between
city i and city i + 1.
'''

distances = list(map(int, input().split()))
result = []

for i in range(5):
    row = []
    for j in range(5):
        if i == j:
            row.append(0)
        elif i < j:
            row.append(sum(distances[j:i]))
        else:
            row.append(sum(distances[j:i]))
    result.append(row)

for row in result:
    print(" ".join(str(x) for x in row))