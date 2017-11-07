"""
I used conquer keyword here since this function is the one
that sorts the whole thing. It only begins conquering(Merging) when the partitioning is  complete.
"""
def conquer(left,right,array):
    #Just normal counters.
    #i-will be my Main Array counter as I will be doing in place sorting for memory efficiency
    #l and r- These will be my left and right partition counters.
    i = l = r = 0
    """
    I like while loops here as they give my that infinite loop that will go on till I tell it to stop.
    This loop here is the engine that will work on first gear, it will work on most of the cases, where there
    is something to compare in both the left and right partitions.
    I leave the code reading to you to figure out how this works.
    """
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            array[i] = left[l]
            l += 1
        else:
            array[i] = right[r]
            r += 1
        i += 1
    """
    A second gear in the merge engine, this will handle some of the cases. When say the right sub-array had the
    smallest elements and they have all been put in place, this will handle the sorting of the left section.
    The other loop can be thought of a think free flow gear that will handle te right sub-array, if it is the resisdual
    one. The first and second case can happen in reverse order, it just depends on your array and how elements are
    organized.
    """
    while l < len(left):
        array[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        array[i] = right[r]
        r += 1
        i += 1
    return array
"""
The Divisor, now this is where the divide manifests. 
Understand one thing, this function will split the parsed 
arraysinto smaller and smaller sections in groups of 3 
till only one element is Its right. How will it know one 
element is left? 
Look at the condition prior to the recursive calls. 
A single element in itself is considered sorted so 
when the divisionis done till only one element is left, 
then this little bad boy here knows it had divided the 
input completely and needs to start merging them. 
I will leave the code operation details for you to decipher.
"""
def mergeSort(array):
    mid=len(array)//2
    left=array[:mid]
    right=array[mid:]
    if len(array)>1:
        mergeSort(left)
        mergeSort(right)
    return conquer(left,right,array)
#Just a test case.
print(mergeSort([17,2,45,6,3,696,6,8,-1,114]))
TAGS
