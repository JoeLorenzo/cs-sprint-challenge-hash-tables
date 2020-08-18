def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # my approach would be to keep track of negative and positive numbers
    # in different dictionaries and lastly compare the two dictionary

    # dict of positive numbers
    positive = {}
    # dict of the absolute values of negative numbers to easily compare the
    # the two dicts for duplicates.  Making the negative numbers positive now
    # becomes a simple problem of finding duplicates
    negative = {}
    # a dict to push all the common absolute values
    dups = {}
    for num in a:
        if num not in positive or negative:
            # if positive
            if num > 0:
                # numbers will be our keys.  since we don't care about
                # anything else we will set the value to zero as a default.
                positive[num] = 0
            # if negative
            elif num < 0:
                # if negative number then get the absolute value of 
                # the negative number and push it to the negative dictionary 
                negative[(-1) * num] = 0

    # iterate through one dictionary and compare it to the other
    # if common values are found then push to the duplicate dict
    for k in positive.keys():
        if k in negative:
            dups[k] = 0
    
    # convert keys to a list to satisfy desired output
    return list(dups.keys())


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
