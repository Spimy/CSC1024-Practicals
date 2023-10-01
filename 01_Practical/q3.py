def question_3():
  light_speed = 3 * (10 ** 8)

  # Convert second to 1 year
  second_to_year = 60 * 60 * 24 * 365

  # Calculate distance of 1 light year in m
  distance_light_year = light_speed * second_to_year

  # Print out the result (:.2E converts to 2 decimal places)
  print(f"1 light year -> {distance_light_year:.2E}m")
