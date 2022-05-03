// Breadth First Search approach

const numIslands = function (grid) {
	if (!grid || grid.length === 0) return 0;

	let islands = 0;
	let height = grid.length;
	let width = grid[0].length;
	let visited = new Map();
	const directions = [
		[1, 0],
		[0, 1],
		[-1, 0],
		[0, -1],
	];

	function insideGrid(row, col) {
		return 0 <= row && row < height && 0 <= col && col < width;
	}

	function mapKey(row, col) {
		return `${row} by ${col}`;
	}

	for (let i = 0; i < height; i++) {
		for (let j = 0; j < width; j++) {
			if (grid[i][j] === "1" && !visited[mapKey(i, j)]) {
				islands += 1;
				// Start BFS logic
				const queue = new BFSQueue();
				queue.enqueue([i, j]);
				visited[mapKey(i, j)] = true;
				while (!queue.isEmpty()) {
					const pair = queue.dequeue();
					directions.forEach((direction) => {
						const newRow = pair[0] + direction[0];
						const newCol = pair[1] + direction[1];
						if (
							insideGrid(newRow, newCol) &&
							!visited[mapKey(newRow, newCol)] &&
							grid[newRow][newCol] === "1"
						) {
							queue.enqueue([newRow, newCol]);
							visited[mapKey(newRow, newCol)] = true;
						}
					});
				}
			}
		}
	}
	return islands;
};

// Helper classes
class BFSQueue {
	constructor() {
		this.items = [];
	}

	enqueue(element) {
		this.items.push(element);
	}

	dequeue() {
		if (this.isEmpty()) {
			return null;
		}
		return this.items.shift();
	}

	isEmpty() {
		return this.items.length === 0;
	}
}
