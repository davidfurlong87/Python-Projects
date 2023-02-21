def max_area(height_list):
    # takes a list of integers representing peaks on a graph.
    # calculates the maximum volume of water which could be stored between these two peaks
    volume = 0
    hash_table = {index:height_list[index] for index in range(len(height_list))}
    for i in range(len(height_list)-1):
        for j in range(i+1, len(height_list)):
            width = j-i
            if hash_table[i] > hash_table[j]:
                height = hash_table[j]
            else:
                height = hash_table[i]
            if (width * height) > volume:
                volume = width * height
    return volume

max_area([1,8,6,2,5,4,8,3,7])
print()
max_area([1,1])
print()
max_area([4,3,2,1,4])
print()
max_area([1,2,1])