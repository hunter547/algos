from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])
        maxUnits = 0
        while truckSize > 0 and len(boxTypes) > 0:
            currentBox = boxTypes.pop()
            if currentBox[0] <= truckSize:
                maxUnits += currentBox[0] * currentBox[1]
            else:
                maxUnits += truckSize * currentBox[1]
            truckSize -= currentBox[0]
        return maxUnits
