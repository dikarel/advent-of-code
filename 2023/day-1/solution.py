with open("input.txt", "r") as f:
    input_lines = f.readlines()
    total = 0

    for line in input_lines:

        # Get first digit
        first_digit = None
        for c in line:
            if c.isdigit():
                first_digit = c
                break

        # Get last digit
        last_digit = None
        for i in range(len(line) - 1, -1, -1):
            c = line[i]
            if c.isdigit():
                last_digit = c
                break

        total += int(first_digit + last_digit)

    print(total)
