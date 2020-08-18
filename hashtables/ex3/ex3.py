def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # the output will ONLY be the numbers that are in common
    # all the nested input arrays. 
    
    # because we could have up to 1 million elements in each array
    # putting array elements in a dictionary for instant lookup is 
    # the way to go.
    # because we are working with nested arrays we will try to mirror 
    # this with a dictionary that has nested dictionaries each representing 
    # an individual array
    list_of_lists = {}
    
    # a dynamic variable to distinguish the nested dictionary
    list_num = 1

    # here we loop through each nested array in the input array
    # to push each individual array to the empty list_of_lists dictionary
    # though we will have a nested for loop here the run time is 
    # essentially O(n) because the maximum number of nested arrays
    # will be limited to 10 according to the readME file
    for arr in arrays:
        # list_key is a dynamic f string to name our nested dicts
        list_key = f"list {list_num}"
        # initalize a temperary empty dict with dynamic f string as a variable
        list_key = {}

        # for each array we will iterate through each element
        for num in arr:
            # check if the number is already in our temperary dict
            if num not in list_key:
                # if not already in temperary dict push to temperary dict
                # the numbers will be the keys
                # since we only care about keys we set values to zero
                list_key[num] = 0
        # when loop finishes iterating through each number in the array
        # push the current temperary dictionary to list_of_lists dictionary
        list_of_lists[f"list {list_num}"] = list_key
        # increment list_num value so the next array is appropriately named
        list_num += 1

    # because the numbers in each array must be in all of the arrays it does
    # not matter which array we use as a comparison array
    # here we will arbitrarily pick the first list in our created dictionary
    list_1 = list_of_lists["list 1"]

    # here we make a copy of the first list in our to dictionary house
    # the intersections or the common values in each array
    intersections = dict(list_of_lists["list 1"])
   
    # iterate through each nested dictionary in list_of_lists
    # the values here are dictionaries of each array
    for value in list_of_lists.values():
        # iterate through our camparison dictionary of the first array
        for k in list_1.keys():
            # if the number in the camparison dict is NOT in the current 
            # iterated list than remove that number from the intersections dict 
            if k not in value:
                intersections.pop(k, None)
    return list(intersections.keys())


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
