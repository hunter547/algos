const twoSum = function (nums, target) {
	const twoMap = new Map();
	for (let i = 0; i < nums.length; i++) {
		const complement = target - nums[i];
		if (twoMap.has(complement)) {
			return [twoMap.get(complement), i];
		}
		twoMap.set(nums[i], i);
	}
};

// Execute test
// Expected result for target 10 and nums array [2, 3, 5, 8, 4, 6] is [0, 3]
console.log(twoSum([2, 3, 5, 8, 4, 6], 10));
