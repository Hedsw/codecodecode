// A famous recently-solved problem in AI, Go is a board game played by two players on a square board. Both players can only place stones (either white or black) on open spaces of the board.  Stones that are adjacent to each other form a group.

// For example, consider the following 3x3 board:

// w w -
// b - -
// - b b

// There are 3 groups of stones on this board, one white and two black.  The most important property of a group of stones is the number of empty spaces on the outside of it.  These empty spaces are known as the group’s liberties.

// In the example above:
// The group at position 2,2 (the bottom right corner) has 3 liberties.
// The group at position 1,0 (the left edge) has 2 liberties.
// The group at position 0,1 (the top) has 2 liberties.

// Given as input a Go board and the location of one stone on the board, can you count the number of liberties of this group?

void dfs(vector<vector<char>>&grid, int x, int y, char pattern, int &count){
    
    //if(x<0 || y< 0 || x> grid.size()-1 || y > grid[0].size()-1) return;
    //cout<<"x"<<x<<"y"<<y<<endl;
    if(grid[x][y] == '-'){
        cout<<"liberties at "<<x<<"and "<<y<<endl;
        count++;
        return;
    }

    int rowSize = grid.size();
    int colSize = grid[0].size();
    
    
    grid[x][y] = 'x';
    
    if(x>0 && grid[x-1][y] != 'x' &&(grid[x-1][y] == '-' || grid[x-1][y] == pattern))
        {dfs(grid, x-1, y,pattern, count);}
    if(x<rowSize-1 && grid[x+1][y] != 'x' && (grid[x+1][y] == '-' || grid[x+1][y] == pattern)) 
        {dfs(grid, x+1,y,pattern, count);}
    if(y>0 && grid[x][y-1] != 'x' && (grid[x][y-1] == '-' || grid[x][y-1] == pattern)) 
        {dfs(grid, x, y-1,pattern, count);}
    if(y<colSize-1  && grid[x][y+1] != 'x' && (grid[x][y+1] == '-' || grid[x][y+1] == pattern)) 
        {dfs(grid, x, y+1,pattern, count);}
    
    
    
}

int numOfLiberties(vector<vector<char>>&grid, int stone_x, int stone_y) {
    if(grid.size()==0) 
        return -1;
    int numLiberties = 0;
    
    if(grid[stone_x][stone_y] == 'w' || grid[stone_x][stone_y] == 'b')
        dfs(grid,stone_x,stone_y,grid[stone_x][stone_y],numLiberties);
    
    cout<<numLiberties<<" at location "<<stone_x<<" and "<<stone_y<<endl;
    return numLiberties;    
}


int main() {
    std::cout << "Hello World!\n";
    vector<vector<char>> grid {{'w','w','-'}, {'b','-','-'}, {'-','b','b'}};
    
    int libertis = numOfLiberties(grid,2,2);
    cout<<libertis<<endl;
    
    int libertisa = numOfLiberties(grid,0,1);
    cout<<libertisa<<endl;
    
    int libertisc = numOfLiberties(grid,1,0);
    cout<<libertisc<<endl;
}