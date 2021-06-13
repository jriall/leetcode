# Maximum Population Year

# You are given a 2D integer array logs where each logs[i] = [birthi, deathi]
# indicates the birth and death years of the ith person.

# The population of some year x is the number of people alive during that year.
# The ith person is counted in year x's population if x is in the inclusive
# range [birthi, deathi - 1]. Note that the person is not counted in the year
# that they die.

# Return the earliest year with the maximum population.

# Example 1:

# Input: logs = [[1993,1999],[2000,2010]]
# Output: 1993
# Explanation: The maximum population is 1, and 1993 is the earliest year with
# this population.

class Solution:
  def maximumPopulation(self, logs: List[List[int]]) -> int:
    population_map = {}
    for year in range(1950, 2051):
      population_map[year] = 0
      for person in logs:
        if person[0] <= year < person[1]:
          population_map[year] += 1
    max_population = max(population_map.values())
    for year in range(1950, 2051):
      if population_map[year] == max_population:
        return year
        