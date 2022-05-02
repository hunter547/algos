from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Sort the intervals array by the first element of each
    # interval. This will allow for sequential comparison of each
    # interval and extend a previous interval the merged array
    intervals.sort(key=lambda x: x[0])

    # Declare an array that the merged intervals will be stored in
    merged = []

    # Begin looping through the sorted intervals array
    for interval in intervals:
        # If the merged array is empty or the ending number of the
        # last interval in the merged array is less than the
        # beginning number of the current interval, then simply add
        # the interval to the merged array
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        # Otherwise, extend the last interval in the merged array to
        # the ending number of the current interval (i.e. (1, 3) is extended to (1, 5))
        else:
            merged[-1][1] = max(interval[1], merged[-1][1])
    return merged


# Execute Test
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Expected: [[1,6],[8,10],[15,18]]
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
