/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
	const digits = [
		[1000, "M"],
		[900, "CM"],
		[500, "D"],
		[400, "CD"],
		[100, "C"],
		[90, "XC"],
		[50, "L"],
		[40, "XL"],
		[10, "X"],
		[9, "IX"],
		[5, "V"],
		[4, "IV"],
		[1, "I"],
	];
	let res = [];
	for (let i = 0; i < digits.length; i++) {
		if (num === 0) break;
		const [value, symbol] = digits[i];
		const count = Math.floor(num / value);
		if (count) {
			res.push(symbol.repeat(count));
		}
		num = num % value;
	}
	return res.join("");
};
