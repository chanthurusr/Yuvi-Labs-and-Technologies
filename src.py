import random

def get_int(prompt, min_val=None, max_val=None):
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        value = int(value)

        if min_val is not None and value < min_val:
            print(f"Value must be at least {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"Value must be at most {max_val}.")
            continue

        return value


def generate_even():
    return random.choice([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])


def print_grid(grid):
    for row in grid:
        line = ""
        for num in row:
            line += f"{num:02d} | "
        print(line.rstrip(" |"))
    print()


def print_highlighted(grid, x):
    count = 0
    for row in grid:
        line = ""
        for num in row:
            if num == x:
                line += f"[{num:02d}] "
                count += 1
            else:
                line += f"{num:02d}  "
        print(line)
    print()
    return count


def main():
    print("Step 1:")

    # Part 1: Grid size input
    n = get_int("Enter array size (for NXN array): ", 1, 50)

    # Generate NxN grid
    grid = [[generate_even() for _ in range(n)] for _ in range(n)]

    print("\nGenerated array:")
    print_grid(grid)

    # Ask user for X to highlight
    print("Step 2:")
    x = get_int("Enter a number to highlight (even number 2–20): ", 2, 20)

    if x % 2 != 0:
        print("Number must be even!")
        return

    print(f"\nWith {x} highlighted:\n")
    count = print_highlighted(grid, x)

    print(f"Number {x} appeared {count} time(s)")


if __name__ == "__main__":
    main()
