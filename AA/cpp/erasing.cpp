#include <stdio.h>
#include <iostream>

using namespace std;

int n,d,curr,queue[10][100000],head[10],tail[10],i,toshow,last;
char line[100005];

int main(){
		while(true){
			scanf("%d %d",&n,&d);
			if (n==0 && d== 0){				
				break;
			}
			cin >> line;
			
			for(i = 0; i < 10; i++) head[i] = tail[i] = 0;
			for(i = 0; i < n; i++){
				curr = line[i]-'0';
				queue[curr][tail[curr]++] = i;
			}
			for(last = 0,toshow = n-d;toshow; ){
				for(i = 9; i >= 0; i--){
					while(head[i] != tail[i] && queue[i][head[i]] < last) head[i]++;
					if(head[i]!=tail[i] && queue[i][head[i]] <= n-toshow){
						toshow--;
						cout << i;
						last = queue[i][head[i]++];
						break;
					}
				}
			}
			cout << '\n';
		}
	return 0;
}
