def arithmetic(a, difference, n):

    '''Calculates the sum of a arithmetic serie of n elements.

       An arithmetic sequence is of the form: a, a+d, a+2d, a+3d,...

       n is the number of elements in the sequence.'''

    #Get the arithmetic sequence

    sequence = [a+difference*x for x in range(n)]

    #Calculates its sum

    return sum(sequence)
