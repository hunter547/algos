/**
 * @param {number[][]} boxTypes
 * @param {number} truckSize
 * @return {number}
 */
var maximumUnits = function (boxTypes, truckSize) {
	boxTypes.sort((a, b) => a[1] - b[1]);
	let maxUnits = 0;
	while (truckSize > 0 && boxTypes.length > 0) {
		const currentBox = boxTypes.pop();
		if (currentBox[0] <= truckSize) {
			maxUnits += currentBox[0] * currentBox[1];
		} else {
			maxUnits += truckSize * currentBox[1];
		}
		truckSize -= currentBox[0];
	}
	return maxUnits;
};
