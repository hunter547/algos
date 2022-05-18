/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
	let l = 0,
		r = matrix[0].length - 1;
	while (l < r) {
		for (let i = 0; i < r - l; i++) {
			const top = l,
				bottom = r;

			// store the top left value as a temp value
			const topLeft = matrix[top][l + i];

			// move bottom left to top left
			matrix[top][l + i] = matrix[bottom - i][l];

			// move bottom right to bottom left
			matrix[bottom - i][l] = matrix[bottom][r - i];

			// move top right to bottom right
			matrix[bottom][r - i] = matrix[top + i][r];

			// move the top left temp value to top right
			matrix[top + i][r] = topLeft;
		}
		r--;
		l++;
	}
};
