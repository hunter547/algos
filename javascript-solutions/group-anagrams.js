/**
 * @param {string[]} strs
 * @return {string[][]}
 */

// using sort
const groupAnagrams = function (strs) {
	const map = new Map();

	strs.forEach((v) => {
		const key = v.split("").sort().join("");
		map.has(key) ? map.set(key, [...map.get(key), v]) : map.set(key, [v]);
	});

	return [...map.values()];
};
