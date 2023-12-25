import re

max_allowed = {
   'red': 12,
    'green': 13,
    'blue': 14
}


# Could be more readable at the cost of performance, if we split the "parse input" and the "calculate output" parts
with open("input.txt", "r") as f:
    lines = f.readlines()
    total = 0

    for line in lines:
      pattern = re.compile("Game (\\d+):(.+)")
      [game_id, pickup_lines] = pattern.match(line).groups()
      game_id = int(game_id)

      pickup_lines = pickup_lines.strip()
      pickup_lines = pickup_lines.replace(";", ",").split(",")
      failed_to_match = False

      for pickup_line in pickup_lines:
        pattern = re.compile("(\\d+) (blue|green|red)")
        [amount, color] = pattern.match(pickup_line.strip()).groups()
        amount = int(amount)

        if amount > max_allowed[color]:
          failed_to_match = True
          break

      if not failed_to_match:
         total += game_id

    print(total)
