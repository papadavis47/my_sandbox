
def combo(iter1, iter2):
    list_of_tuples = []
    for index, item in enumerate(iter1):
        list_of_tuples.append( (iter1[index], iter2[index]) )
    return list_of_tuples

    # this took me awhile, because I am unused to the working with enumerate and I am not used to working with tuples. I learned a lot today.