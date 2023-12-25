import re


# Could be more readable at the cost of performance, if we split the "parse input" and the "calculate output" parts
with open("input.txt", "r") as f:
    lines = f.readlines()
    total = 0

    for line in lines:
      pattern = re.compile("Game (\\d+):(.+)")
      [_, pickup_lines] = pattern.match(line).groups()

      min_required = {
        'red': 1,
        'green': 1,
        'blue': 1
      }

      pickup_lines = pickup_lines.strip()
      pickup_lines = pickup_lines.replace(";", ",").split(",")

      for pickup_line in pickup_lines:
        pattern = re.compile("(\\d+) (blue|green|red)")
        [amount, color] = pattern.match(pickup_line.strip()).groups()
        amount = int(amount)

        if amount > min_required[color]:
          min_required[color] = amount

      total += min_required["red"] * min_required["green"] * min_required["blue"]

    print(total)
