/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
const suggestedProducts = function (products, searchWord) {
	products.sort();
	const result = new Map();
	let prefix = "";
	for (let i = 0; i < searchWord.length; i++) {
		prefix += searchWord.charAt(i);
		result.set(prefix, []);
		for (let j = 0; j < products.length; j++) {
			if (result.get(prefix).length === 3) {
				break;
			}
			if (products[j].substring(0, i + 1) === prefix) {
				result.set(prefix, [...result.get(prefix), products[j]]);
			}
		}
	}
	return [...result.values()];
};
