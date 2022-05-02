const merge = function (intervals) {
	// Sort the intervals array by the first element of each
	// interval. This will allow for sequential comparison of each
	// interval and extend a previous interval the merged array
	intervals.sort((a, b) => a[0] - b[0]);

	// Declare an array that the merged intervals will be stored in
	const merged = [];

	// Begin looping through the sorted intervals array
	intervals.forEach((interval, i) => {
		const lastInterval = merged[merged.length - 1];
		// If the merged array is empty or the ending number of the
		// last interval in the merged array is less than the
		// beginning number of the current interval, then simply add
		// the interval to the merged array
		if (!merged.length || lastInterval[1] < interval[0]) {
			merged.push(interval);
			// Otherwise, extend the last interval in the merged array to
			// the ending number of the current interval (i.e. (1, 3) is extended to (1, 5))
		} else {
			lastInterval[1] = Math.max(lastInterval[1], interval[1]);
		}
	});

	return merged;
};

// Execute Test
// Input: [[1,3],[2,6],[8,10],[15,18]]
// Expected: [[1,6],[8,10],[15,18]]
console.log(
	merge([
		[1, 3],
		[2, 6],
		[8, 10],
		[15, 18],
	])
);
