#include<bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
	freopen("./common.in","r",stdin);
	freopen("./common.out","w",stdout);
	int a=0,n;
	cin>>n;
	for (int i = 1; i < n+1; ++i)
	{
		a+=n/i;
	}
	cout<<a<<endl;
	fclose(stdin);
	fclose(stdout);
	return 0;
}
