/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
	const digits = {
		M: 1000,
		CM: 900,
		D: 500,
		CD: 400,
		C: 100,
		XC: 90,
		L: 50,
		XL: 40,
		X: 10,
		IX: 9,
		V: 5,
		IV: 4,
		I: 1,
	};
	const digitsMap = new Map(Object.entries(digits));

	let result = 0,
		i = 0;

	while (i < s.length) {
		if (i < s.length - 1 && digitsMap.has(s.substring(i, i + 2))) {
			result += digitsMap.get(s.substring(i, i + 2));
			i++;
		} else {
			result += digitsMap.get(s.charAt(i));
		}
		i++;
	}
	return result;
};
