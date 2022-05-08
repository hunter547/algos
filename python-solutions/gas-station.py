# Keep in mind that only one solution exists. Therefore, if the cost to get to the next station
# is greater than the gas able to be received at the current station plus any gas in the tank, then
# we can safely assume that the current index can't be the starting point and we can move the
# start_station pointer to the next gas statiton in the list.
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, start_station, curr_tank = 0, 0, 0

        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            if (curr_tank < 0):
                curr_tank = 0
                start_station = i + 1

        return start_station if total_tank >= 0 else -1
