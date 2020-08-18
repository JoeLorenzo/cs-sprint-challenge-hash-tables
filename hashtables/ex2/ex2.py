#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # the output should be an array with destinations only
    # the way the classes are linked reminds me of a linked
    # list thus could be iterated in a similar fasion.

    # initialize an empty hash table to hold the tickets 
    ticks = {}
    
    # iterate through the input array to push each
    # ticket into to ticks hash table
    for ticket in tickets:
        ticks[ticket.source] = ticket.destination

    # initialize a 'current' variable to the first ticket
    # this is will be a temperary variable to hold the current
    # ticket as the tickets are iterated 
    current = ticks["NONE"]

    # initialize an empty array for the output
    # destinations will be pushed here
    ticks_arr = []

    # iterate through the ticks dictionary until we get to the
    # last ticket.  the logic here should look a lot like iterating
    # through a linked list.
    while current != "NONE":
        ticks_arr.append(current)
        current = ticks[current]
    
    # append a "NONE" to the ouptut array to make test pass.
    ticks_arr.append("NONE")
    return ticks_arr
    
    # O(n) time complexity 
    # O(n) space complexity
