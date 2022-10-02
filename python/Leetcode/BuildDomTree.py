class Tree:
      def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self,node):
    self.children.append(node)

  def _print(self, level=0):
    print(self.value)
    for i, child in enumerate(self.children):
      print("level ", level, " child ", i ," ", end="")
      child._print(level + 1)



def create_tree(values):
  value = values.pop(0)
  values.pop()
  tree = Tree(value)
  while len(values) != 0:
    # get values between start tag and end tag using stack
    new_values_to_traverse = []
    start = values.pop(0)
    stack = [start]
    while len(stack) != 0 and len(values) != 0:
      new_value = values.pop(0)
      if new_value == stack[-1][0] + "/" + stack[-1][1:]:
        stack.pop()
      if len(stack) != 0:
        new_values_to_traverse.append(new_value)
      if "/" not in new_value:
        stack.append(new_value)
    new_tree = Tree(start)
    if len(new_values_to_traverse) != 0:
      new_tree.add_child(create_tree(new_values_to_traverse))
    tree.add_child(new_tree)
  return tree


html_str="<div>\n<div>\n<a>\n<div>\n</div>\n</a>\n</div>\n<div>\n<a>\n</a>\n</div>\n</div>"
create_tree(html_str.split("\n")).print()