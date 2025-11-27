import sys

# Taking scores from command line
if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
else:
    scores = [10, 20, 30]

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
