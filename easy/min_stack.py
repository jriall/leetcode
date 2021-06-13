# Min Stack

class MinStack:
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack = []
    self.mins = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    current_min = val if len(self.mins) == 0 else min(val, self.mins[-1])
    self.mins.append(current_min)

  def pop(self) -> None:
    self.stack.pop()
    self.mins.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

