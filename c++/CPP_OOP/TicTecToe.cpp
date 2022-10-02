
// Time Complexity - O(n) because as for every move we are iterating over n cells 
// 4 times to check for each of the column, row, diagonal row, and anti-diagonal. 
// Space Compleixty - O(n^2)
class TicTacToe {
public:
    vector<vector<int>> board;
    int n;

    TicTacToe(int n) {
        board.assign(n, vector<int>(n, 0));
        this->n = n;
    }

    int move(int row, int col, int player) {
        board[row][col] = player;
        if (checkCol(col, player) ||
            checkRow(row, player) ||
            (row == col && checkDiagonal(player)) ||
            (row == n - col - 1 && checkAntiDiagonal(player))) {
            return player;
        }
        // No one wins
        return 0;
    }

    bool checkDiagonal(int player) {
        for (int row = 0; row < n; row++) {
            if (board[row][row] != player) return false;
        }
        return true;
    }

    bool checkAntiDiagonal(int player) {
        for (int row = 0; row < n; row++) {
            if (board[row][n - row - 1] != player) return false;
        }
        return true;
    }

    bool checkCol(int col, int player) {
        for (int row = 0; row < n; row++) {
            if (board[row][col] != player) return false;
        }
        return true;
    }

    bool checkRow(int row, int player) {
        for (int col = 0; col < n; col++) {
            if (board[row][col] != player) return false;
        }
        return true;
    }
};

// Optimized Solution
/*
Our goal is to find if a player has won by marking an entire row, column, diagonal, 
or anti diagonal cells. Can we find this in constant time without iterating over each of the horizontal, 
vertical, and diagonal rows on every move? Yes! Let's find out how.

Let's break the problem into 2 parts,

First, on every move, we must determine whether a player has marked all of the cells in a row or column. 
In other words, we could say that, 
if there are n rows and n columns on a board, the player must have marked a certain row or column n times.

Second, on every move, we must determine whether a player has marked all of the cells on the main diagonal or anti-diagonal. 
Irrespective of the size of the board, there can only be one diagonal and one anti-diagonal.
*/
// Time Complexity - O(1)
// Space Compliexity - O(n) because we use arrays rows and cols of size n. 
// The variables diagonal and antiDiagonal use constant extra space.
class TicTacToe {
public:
    vector<int> rows;
    vector<int> cols;
    int diagonal;
    int antiDiagonal;

    TicTacToe(int n) {
        rows.assign(n, 0);
        cols.assign(n, 0);
        diagonal = 0;
        antiDiagonal = 0;
    }

    int move(int row, int col, int player) {
        int currentPlayer = (player == 1) ? 1 : -1;
        // update currentPlayer in rows and cols arrays
        rows[row] += currentPlayer;
        cols[col] += currentPlayer;
        // update diagonal
        if (row == col) {
            diagonal += currentPlayer;
        }
        // update anti diagonal
        if (col == (cols.size() - row - 1)) {
            antiDiagonal += currentPlayer;
        }
        int n = rows.size();
        // check if the current player wins
        if (abs(rows[row]) == n ||
            abs(cols[col]) == n ||
            abs(diagonal) == n ||
            abs(antiDiagonal) == n) {
            return player;
        }
        // No one wins
        return 0;
    }
};