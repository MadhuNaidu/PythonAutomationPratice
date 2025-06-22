
"""
1. What are the python charecterstics?
2. What is a python path?
3. what are the datatypes with examples?
4. What are the inbuilt methods with examples?
5. string methods with methods?
6. list methods with examples?
7. diff b/w list and tuple?
8. diff b/w insert, append and extend?
9. diff b/w pop and remove, clear?
10. diff shallow and deep copy with example?
11. how to sort a list with ascending and descnding order?
12. What is a dict and where to use?
13. how many ways we can get the values from dict?
14. how many ways we can update the dict?
15. diff b/w pop and popitem()?
16. what are the available methods in sets?
17. What is a slicing? examples?
18. What is a index in python and how it will be useful?
19. Find the largest, second largest and lowest, second lowest num for the list?
20. Sort the list?
21. Sort the list without inbuilt functions?
22. What is a function and how many types we have with examples?
23. what is the use of return keyword?
24. what are the ways we can provide function args?
25. *args and **kwargs?
26. special functions with examples?
27. diff break, continue and pass?
28. diff b/w for and while with use cases?
"""


def find_nearby_duplicates(lst):
    from collections import defaultdict

    pos_dict = defaultdict(list)
    for index, num in enumerate(lst):
        pos_dict[num].append(index)

    min_distance = float('inf')
    result_elements = []

    for num in pos_dict:
        positions = pos_dict[num]
        if len(positions) >= 2:
            current_min = min(positions[i + 1] - positions[i] for i in range(len(positions) - 1))
            if current_min < min_distance:
                min_distance = current_min
                result_elements = [num]
            elif current_min == min_distance:
                result_elements.append(num)

    return sorted(result_elements) if result_elements else []


# Test cases
input1 = [1, 2, 3, 1, 2, 5, 5, 4, 3]
print(find_nearby_duplicates(input1))  # Expected output: [5]

input2 = [1, 2, 3, 1, 2, 5, 4, 3]
print(find_nearby_duplicates(input2))  # Expected output: [1,2]