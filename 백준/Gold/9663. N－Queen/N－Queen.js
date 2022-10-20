const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString();

const n = parseInt(inputData);


function findQueens(n) {
  // 이곳에 작성합니다.
  const visited_col = new Array(n).fill(0);
  const visited_diagonal_1 = new Array(2 * n).fill(0);
  const visited_diagonal_2 = new Array(2 * n).fill(0);

  let answer = 0;

  const n_queen = (row, n) => {
    if (row === n) {
      answer += 1;
      return;
    }

    for (let col = 0; col < n; col++) {
      if (
        visited_col[col] == 0 &&
        visited_diagonal_1[row + col] == 0 &&
        visited_diagonal_2[row - col + n] == 0
      ) {
        visited_col[col] = 1;
        visited_diagonal_1[row + col] = 1;
        visited_diagonal_2[row - col + n] = 1;

        n_queen(row + 1, n);

        visited_col[col] = 0;
        visited_diagonal_1[row + col] = 0;
        visited_diagonal_2[row - col + n] = 0;
      }
    }
  };

  n_queen(0, n);
  return answer;
}

console.log(findQueens(n));
