set1 = frozenset({1, 2, 3})
ls = list(set1)
subsets = [frozenset({})]

for j in ls:
    subsets.append(frozenset({j}))
    for k in ls:
        subsets.append(frozenset({j, k}))

subsets.append(set1)
print(len(frozenset(subsets)))
for i in frozenset(subsets):
    print(i)
    
# def power_set(i):
#     i_list = list(i)
#     n = len(i_list)

#     # Calculate the total number of subsets (2^n)
#     total_subsets = 2 ** n

#     # Generate all subsets using binary representation
#     all_subsets = []
#     for subset_index in range(total_subsets):
#         subset = set()
#         for j in range(n):
#             # Check if the j-th bit of subset_index is set (1)
#             if (subset_index >> j) & 1:
#                 subset.add(i_list[j])
#         all_subsets.append(frozenset(subset))

#     return all_subsets

# # Example usage:
# i = frozenset({1, 2, 3})
# result = power_set(i)
# for subset in result:
#     print(subset)
