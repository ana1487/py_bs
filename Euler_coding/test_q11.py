# Define the range of a and b
a_range = range(2, 101)
b_range = range(2, 101)

# Use a set to store unique terms
distinct_terms = set()

# Generate all combinations of a^b and add them to the set
for a in a_range:
    for b in b_range:
        distinct_terms.add(a**b)

# Output the number of distinct terms
print("Number of distinct terms:", len(distinct_terms))
