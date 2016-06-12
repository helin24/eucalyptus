import math

def pentagon_pair():
  heap = Heap()
  heap.add(Node(pentagonal_diff(1,2), [1,2]))

  added = {1 : {2 : True}}

  while True:
    current_node = heap.remove_top_node()
    i = current_node.contents[0]
    j = current_node.contents[1]

    if i + 1 not in added:
      heap.add(Node(pentagonal_diff(i + 1, j + 1), [i + 1, j + 1]))
      added[i + 1] = {j + 1 : True}
    if j + 1 not in added[i]:
      heap.add(Node(pentagonal_diff(i, j + 1), [i, j + 1]))
      added[i][j + 1] = True

    sum_of_nums = sum(pentagonal_number(x) for x in current_node.contents)
    if is_pentagonal(sum_of_nums):
      if is_pentagonal(current_node.value):
        return current_node.value

#     # check if pentagonal_diff(i, j) is_pentagonal
#     if is_pentagonal(current_node.value):
# #      print current_node.contents
#       sum_of_nums = sum(pentagonal_number(x) for x in current_node.contents)
# #      print "sum is {0}".format(sum_of_nums)
#       if is_pentagonal(sum_of_nums):
#         print "found"
#         return current_node.value

def pentagonal_number(index):
  return index * (3 * index - 1) / 2

def pentagonal_diff(i, j):
  return pentagonal_number(j) - pentagonal_number(i)

def is_pentagonal(num):
  a = 3.0 / 2
  b = - 1.0 / 2
  c = - num

  root_pos = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

#  print "positive root is {0}".format(root_pos)
  if root_pos == math.floor(root_pos):
    return True
  else:
    return False

class Heap:
  def __init__(self):
    self.nodes = []

  def add(self, node):
    self.nodes.append(node)
    position = len(self.nodes) - 1
    
    parent_position = self.get_parent_position(position)
    
    while True:
      if parent_position is None or self.nodes[parent_position] <= self.nodes[position]:
        break
      self.nodes[position] = self.nodes[parent_position]
      self.nodes[parent_position] = node
      position = parent_position
      parent_position = self.get_parent_position(position)

    return self

  def remove_top_node(self):
    top_node = self.nodes[0]
    # move last node to first node
    last_node = self.nodes.pop()

    if len(self.nodes) == 0:
      return top_node

    current_position = 0
    self.nodes[current_position] = last_node

    # find node children
    while True:
      children_positions = self.get_child_positions(current_position)
      if len(children_positions) == 0:
        break
      self_smallest = True
      for child_position in children_positions:
        if self.nodes[child_position] <= self.nodes[current_position]:
          self_smallest = False
      if self_smallest:
        break

      # find min child node and swap
      if len(children_positions) == 1:
        self.swap(current_position, children_positions[0])
        current_position = children_positions[0]
      else:
        left_pos = children_positions[0]
        right_pos = children_positions[1]
        if self.nodes[left_pos] <= self.nodes[right_pos]:
          self.swap(current_position, left_pos)
          current_position = left_pos
        else:
          self.swap(current_position, right_pos)
          current_position = right_pos

    return top_node

  def get_parent_position(self, position):
    if position == 0: 
      return None 
    return (position - 1) / 2

  def get_child_positions(self, position):
    left_position = position * 2 + 1
    right_position = position * 2 + 2

    length = len(self.nodes)
    children = []
    
    if left_position < length:
      children.append(left_position)
    if right_position < length:
      children.append(right_position)

    return children

  def swap(self, position_one, position_two):
    temp = self.nodes[position_one]
    self.nodes[position_one] = self.nodes[position_two]
    self.nodes[position_two] = temp
    return self

  def __str__(self):
    final_str = ''
    count = 0
    for node in self.nodes:
      final_str += "\n %s : " % (count)
      final_str += node.__str__()
      count += 1

    return final_str


#   1
# 2   4
#3 
class Node:
  def __init__(self, value, contents):
    self.value = value 
    self.contents = contents

  def __cmp__(self, other):
    return cmp(self.value, other.value)

  def __str__(self):
    return "Node with value: %s and content: %s" % (self.value, self.contents.__str__())

# x = Node(1, 2)
# y = Node(2, 3)
# print x > y
# print y > x

print pentagon_pair()

# How to check through combinations of numbers? [1,2] then [1,3] etc.?
# How to check through combinations in order? Have a current pair and a next pair.
# Start with current pair is smallest possible [1,2] and next pair is [2,3]
# Use a heap and keep putting adjacent things into heap
# Start with [1,2] and add [1,3] and [2,3]
# After checking [1,2] check [1,3] because it has the lowest. Add [1,4]
# Then check [2,3] and add [3,4] and [2,4]
# print is_pentagonal(5)
# print is_pentagonal(6)
# print is_pentagonal(117)

# What about the sum of two pentagonal numbers?

# The difference between indices i and j where j > i
# D[i,j] = 4 * (j - i) + 3 * (j^2 / 2 - 3j / 2 + 1) = 4j - 4i + 3j^2 / 2 - 9j / 2 + 3 = 3j^2 / 2 - j / 2 - 4i + 3

# D[1,2] = 6 - 1 - 4 + 3 = 4
# D[1,3] = 27/2 - 3/2 - 4 + 3 = 11
# D[2,4] = 24 - 2 - 8 + 3 = 17

# 1st and 2nd - 4 = (4 * 1 + 0) = (4 * 1) + (0 * 3)
# 1st and 3rd - 11 = (4 * 2 + 3) = (4 * 2) + (1 * 3)
# 1st and 4th - 21 = (4 * 3 + 9) = (4 * 3) + ( ????
# 1st and 5th - 34 = (4 * 4 + 18)
# 1st and 6th - 50 = (4 * 5 + 30)
# 1st and 7th - 69 = (4 * 6 + 45)

# 2nd and 3rd - 7 = (4 * 1 + 3) = (4 * 1 + 3 * 1)
# 2nd and 4th - 17 = (4 * 2 + 9) = (4 * 2 + 3 * 3)
# 2nd and 5th - 30 = (4 * 3 + 18) = (4 * 3 + 3 * 6)
# 2nd and 6th - 46 = (4 * 4 + 30) = (4 * 4 + 3 * 10)
# 2nd and 7th - 65 = (4 * 5 + 45)

# For two indices i and j, it seems the difference is going to be 4 * (j - i) + 3 * x
# x is a number that depends only on j and is equal to ...
# j = 2 : x = 0
# j = 3 : x = 1
# 4 : 3
# 5 : 6
# 6 : 10

# (j - 2) * 1 + (j - 3) * 2 + (j - 3) * 3 (for j = 4)
# xn+1 = xn + (n - 2)
# xn+1 = xn-1 + (n - 3) + (n - 2) until we reach x = 0

# x2 = 0 + (j - 2) = 0
# x3 = (j - 1 - 2) + (j - 2) = (j - 3) + (j - 2) = 2j - 5
# x4 = (j - 2 - 2) + (j - 1 - 2) + (j - 2) = (j - 4) + (j - 3) + (j - 2) = 3j - 9
# x5 = 4j - 14
# x6 = 5j - 20

# xj = j * (j - 1) - (2 * (j - 1) + (j - 2) * (j - 1) / 2)
# xj = j2 - j - (2j - 2 + (j^2 - 3j + 2) / 2)
# xj = j^2 - j - 2j + 2 - j^2 / 2 + 3j/2 - 1
# xj = j^2 / 2 - 3j / 2 + 1

# x2 = 2 - 3 + 1 = 0
# x3 = 9/2 - 9/2 + 1 = 1
# x4 = 8 - 6 + 1 = 3
# x5 = 25/2 - 15/2 + 1 = 6
# x6 = 18 - 9 + 1 = 10

# differences between each difference is always 3

