const slidingWindow = function (s) {
	const seen = new Map();
	let ans = 0;
	let i = 0;
	let j = 0;
	while (j < s.length) {
		if (seen.has(s[j])) {
			i = Math.max(i, seen.get(s[j]));
		}
		ans = Math.max(ans, j - i + 1);
		seen.set(s[j], j + 1);
		j++;
	}
	return ans;
};

// Execute test
console.log(slidingWindow("abcabcdabab"));
