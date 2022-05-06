/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function (gas, cost) {
	let currTank = 0,
		totalTank = 0,
		startStation = 0;
	for (let i = 0; i < gas.length; i++) {
		currTank += gas[i] - cost[i];
		totalTank += gas[i] - cost[i];
		if (currTank < 0) currTank = 0;
		startStation = i + 1;
	}

	return totalTank >= 0 ? startStation : -1;
};
