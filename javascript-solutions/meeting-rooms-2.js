/**
 * @param {number[][]} intervals
 * @return {number}
 */
const minMeetingRooms = function (intervals) {
	if (!intervals.length) return 0;
	const startTimes = intervals
		.sort((a, b) => a[0] - b[0])
		.map((interval) => interval[0]);
	const endTimes = intervals
		.sort((a, b) => a[1] - b[1])
		.map((interval) => interval[1]);
	let usedRooms = 0;

	let endPointer = 0;

	intervals.forEach((interval, i) => {
		// The start time of this meeting starts later than or at the ending time of the least recently started meeting
		// which means a room is now free to be reused
		if (startTimes[i] >= endTimes[endPointer]) {
			// Free up a room
			usedRooms -= 1;
			// Move to the next least recently used meeting end time
			endPointer += 1;
		}
		// Increase the number of rooms, this will be cancelled out when the previous if statement equates to true
		usedRooms += 1;
	});
	return usedRooms;
};
