'''
Two Number Sum

Write a function that takes in a non-empyt array of distinct integers
and an integer representing a target sum. If any two numbers in the
input array sum up to the target sum, the function should return them
in an array, in any order. If no two number sum up to the target sum,
the function should return an empty array.

Note that the target sum has to be obtained by summing two different
integers in the array; you can not add a single integer to itself in
order to obtain the target sum.

'''


def twoNumberSum(array, targetSum):
    '''
    The function receives an array and an integer as parameters.
    If any two numbers in the input array sum up to the target sum, 
    the function should return them in an array, in any order. 
    If no two number sum up to the target sum, the function should 
    return an empty array.

    Parameters
    -----------
    1. array: input array (integers)
    2. targetSum: the target value (integer) for testing the input array

    Notes
    -----
    - The camel case is not commom for naming funcion in Python.
      But it seems like it is a standard on the Algo Expert.
      Then I decided to follow the Algo Exert standard and 
      naming the functions using camel case.

    '''

    def _tuplesGenerator(array):
        pair_heads_index = [x for x in range(0, (len(array) - 1))]
        pair_tails_index = [x for x in range(1, len(array))]
        for i in pair_heads_index:
            for j in pair_tails_index:
                if (j <= i):
                    continue
                yield(array[i], array[j],)


    def _pairSum(pairs_array, target_sum):
        for pair in pairs_array:
            if (pair[0] + pair[1] == target_sum):
                return [pair[0], pair[1]]
        else:
            return []

        

    pairs_array = [x for x in _tuplesGenerator(array)]
    print(pairs_array)

    result = _pairSum(pairs_array, targetSum)
    print(result)
