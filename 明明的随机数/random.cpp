#include<bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[]){
	freopen("random.in","r",stdin);
	freopen("random.out","w",stdout);
	int n;
	cin>>n;
	int m[101];
	set<int>s;
	for (int i = 0; i < n; ++i)
	{
		cin>>m[i];
		s.insert(m[i]);
	}
	cout<<s.size()<<std::endl;
	while(!(s.empty())){
		cout<<*s.begin()<<" ";
		s.erase(s.begin());
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
} 
