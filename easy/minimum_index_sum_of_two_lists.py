# Minimum Index Sum of Two Lists

# Suppose Andy and Doris want to choose a restaurant for dinner, and they both
# have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index
# sum. If there is a choice tie between answers, output all of them with no
# order requirement. You could assume there always exists an answer.

# Example 1:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

class Solution:
  def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    restaurants = {}
    for index, restaurant in enumerate(list1):
      restaurants[restaurant] = index
    results = {}
    for index, restaurant in enumerate(list2):
      if restaurant in restaurants:
        results[restaurant] = index + restaurants[restaurant]
    return [key for key, value in results.items() if value == min(results.values())]
    
        
      