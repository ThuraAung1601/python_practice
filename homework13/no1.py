'''
No. 1
Write a function to traverse and print a binary tree recursion python.
For example, print_btree( [1, [[11, [111, 112]], [12, [121, [122, [1221, 1222]]]]]], 0)
1
.11
..111
..112
.12
..121
..122
...1221
...1222
'''

def print_btree(tree, depth=0):
    if isinstance(tree, list):
        if len(tree) == 2:
            node, children = tree
            print("." * depth + str(node))
            for child in children:
                print_btree(child, depth + 1)
        elif len(tree) == 1:
            node = tree[0]
            print("." * depth + str(node))
    else:
        print("." * depth + str(tree))

tree = [1, [[11, [111, 112]], [12, [121, [122, [1221, 1222]]]]]]
print("Tree:", tree)
print_btree(tree)