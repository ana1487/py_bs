def draw_christmas_tree(levels, star_on_top=True):
    if star_on_top:
        print(" " * (levels - 1) + "*")  # Star on top of the tree
    for i in range(levels):
        spaces = levels - i - 1
        branches = "*" * (2 * i + 1)
        print(" " * spaces + branches)
    trunk_width = levels // 3
    trunk_height = max(2, levels // 4)
    for _ in range(trunk_height):
        print(" " * (levels - trunk_width // 2 - 1) + "|" * trunk_width)

# Customizable input for levels of the tree
try:
    levels = int(input("How tall should the Christmas tree be (number of levels)? "))
    draw_christmas_tree(levels)
except ValueError:
    print("Please enter a valid number!")
