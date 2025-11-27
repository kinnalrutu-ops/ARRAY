import sys

if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
else:
    scores = [10, 20, 30]   

total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
