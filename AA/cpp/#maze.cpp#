#include <bits/stdc++.h>
using namespace std ;

#define LIM 505


char maze[LIM][LIM];
bool path[LIM][LIM];
int n, m, k;

int posx[] = {1,-1,0,0};
int posy[] = {0,0,1,-1};

bool is_valid(int x, int y){
  if (x>=0 && x<n && y>=0 && y<m){
    return true;
  }else{
    return false;
  }
}

void dfs(int x,int y) {
  path[x][y] = true;
  k--;

  if (k!=0) {
    for (int i = 0; i<4; i++) {
      int a, b;
      a = x + posx[i];
      b = y + posy[i];
      if (is_valid(a,b)) {
	if (maze[a][b]=='.') {
	  if (!path[a][b]) {
	    dfs(a,b);
	  }
	}
      }
    }
  }
}



  int main() {
    memset(path,false,sizeof path);
    scanf("%d %d %d",&n,&m,&k);
    
    for (int i = 0; i<n; i++) {
      scanf("%s",maze[i]);
    }
    vector < pair <int,int> > cells;
    for (int i = 0; i<n; i++){
      for (int j = 0; j<m; j++){
	if (maze[i][j]=='.'){
	  cells.push_back(pair <int,int>(i,j));
	}
      }
    }
    k = cells.size()-k;
    dfs(cells[0].first, cells[0].second);
    for (int i = 0; i<cells.size(); i++) {
      if (!path[cells[i].first][cells[i].second]) {
	maze[cells[i].first][cells[i].second] = 'X';
      }
    }
    for (int i = 0; i<n; i++) {
      puts(maze[i]);
    }
  }
