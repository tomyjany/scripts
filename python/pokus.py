class Node:
    def __init__(self, val):
        self.val = val
jedna = Node(1)
dva = Node(2)
tri = Node(3)
q = [jedna, dva, tri]
for i in q:
    i.val = 10
print(jedna.val)
