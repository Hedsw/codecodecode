Intuition:

We can only flip a row 0 or 1 time (eg. flipping 2 times is the same as flipping 0 time)
We can only flip a column 0 or 1 time (eg. flipping 2 times is the same as flipping 0 time)
Knowing the 1st row and the 1st column, we can uniquely determine to flip or not
After the flipping, if there is still 1 in the grid, then fails
Step:

For each row, if the leftmost is 1, we must flip, else we must not flip the row (eg. the leftmost value determines the whole row)
For each column, if the uppermost is 1, we must flip, else we must not flip the column (eg. the uppermost value determines the whole column)
If after previous steps, there is still an 1 in the grid, then fails

// Time comp - O(N)
// Space Comp - O(N)

bool removeOnes(vector<vector<int>>& grid) 
{
	int m=grid.size(),n=grid[0].size();
	for(int i=0;i<m;i++) // flip the row if the leftmost is 1
		if(grid[i][0]==1)
			for(int j=0;j<n;j++) grid[i][j]=!grid[i][j];

	for(int j=1;j<n;j++) // flip the column if the uppermost is 1
		if(grid[0][j]==1)
			for(int i=0;i<m;i++) grid[i][j]=!grid[i][j];

	for(int i=0;i<m;i++) // check if any element is 1 in the grid
		for(int j=0;j<n;j++)
			if(grid[i][j]) return false;

	return true;
}