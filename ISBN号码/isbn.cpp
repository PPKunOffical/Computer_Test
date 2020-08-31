#include<bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[]){
	freopen("isbn.in","r",stdin); 
	freopen("isbn.out","w",stdout); 
	char num[10];
	scanf("%c-%c%c%c-%c%c%c%c%c-%c",&num[0],&num[1],&num[2],&num[3],&num[4],&num[5],&num[6],&num[7],&num[8],&num[9]);
	short int cf=0;
	for (short int i = 0; i < 9; ++i)
		cf+=(num[i]-'0')*(i+1);
	if(cf%11==num[9]-'0' ||(cf%11==10 && num[9]=='X'))
		cout<<"Right";
	else{
		if(cf%11!=10)
			cout<<num[0]<<"-"<<num[1]<<num[2]<<num[3]<<"-"<<num[4]<<num[5]<<num[6]<<num[7]<<num[8]<<"-"<<cf%11;
		else
			cout<<num[0]<<"-"<<num[1]<<num[2]<<num[3]<<"-"<<num[4]<<num[5]<<num[6]<<num[7]<<num[8]<<"-X";
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
