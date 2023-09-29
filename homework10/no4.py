'''
No. 4 
Write a Python function which, given a list of lists representing a table,
prints that table on the screen.

The first member of the list contains a header row which gives the name for 
each column of the table. The other members represent the other rows of the table,
each of them is matched with all columns of the header.
'''
def print_table(ls):
    for i in ls:
        for j in i:
            print(j, end="\t")
        print()

print_table([["x", "y"], [0,0], [10,10], [200, 200]])
print()
print_table([["ID", "Name", "Surname"], ["001", "Guido", "van Rossum"], ["002", "Donald", "Knuth"], ["003", "Gordon", "Moore"]])