# This is from an exercise in the slices module of Treehouse Python track. Learning how to make slices forwards and back with reverse and forward orders.

def first_4(iterable):
	return iterable[:4]

def first_and_last_4(iterable):
    first = iterable[:4]
    last = iterable[-4:]
    combo = first + last 
    return combo

def odds(iterable):
    return iterable[1::2]

# Here was the difficult one. There is more than one way to do it, but I found this way. I have to look at it again later.
def reverse_evens(iterable):
    iterable1 = iterable[::2]
    iterable2 = iterable1[::-1]
    return iterable2