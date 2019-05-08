import bin.thinker.model.tree.tree as tree

(_ROOT, _DEPTH, _BREADTH) = range(3)

tree = tree.Tree()

tree.add_node("0")  # root node
tree.add_node("1", "0")
tree.add_node("2", "0")
tree.add_node("3", "0")


tree.display("0")
print("***** DEPTH-FIRST ITERATION *****")
for node in tree.traverse("0"):
    print(node)
print("***** BREADTH-FIRST ITERATION *****")
for node in tree.traverse("0", mode=_BREADTH):
    print(node)