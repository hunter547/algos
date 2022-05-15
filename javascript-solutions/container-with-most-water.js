/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
	let max = 0,
		left = 0,
		right = height.length - 1;

	while (left < right) {
		const currentMax = Math.min(height[left], height[right]) * (right - left);
		max = Math.max(currentMax, max);
		height[right] > height[left] ? left++ : right--;
	}
	return max;
};
