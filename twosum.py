
def find_two_sum(nums, target:int):
    # Loop through each number
    for i in range(len(nums)):
        # Loop through remaining numbers
        for j in range(i + 1, len(nums)):
            # Check if current pair adds up to target
            if nums[i] + nums[j] == target:
                return [i, j]
    # Return empty list when no values are found
    return []


numbers = [1,2,4,12,11]
target = int(input("Enter a number to find its two sum indexes"))
result = find_two_sum(numbers, target)
if result:
    print(f"Indices of numbers that add up to {target}: {result}")
else:
    print(f"No two numbers add up to {target}")