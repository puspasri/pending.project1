def product_to_tuple(tup):
    """
    Calculates the product of all numbers in a given tuple.
    Args:
    tup:The input tuple containing numbers .
    Returns:The product of all numbers in the tuple."""
    result =1
    for num in tup:
        result*= num 
        return result 
    #Example usage 
    my_tuple = (2,3,4,5)
    product=(my_tuple)
    print("Product of numbers in the tuple:",product)