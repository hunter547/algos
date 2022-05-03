from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        used_rooms = 0

        end_pointer = 0

        for i in range(len(intervals)):
            if (start_times[i] >= end_times[end_pointer]):
                used_rooms -= 1
                end_pointer += 1

            used_rooms += 1

        return used_rooms
