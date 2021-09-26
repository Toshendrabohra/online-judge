#include<bits/stdc++.h>

#define fill(arr,c) memset(arr,c,sizeof(arr))
#define perm(r) next_permutation(all(r))
//it gives bool value ans permute the string lexoggraphically
#define sortdesc greater<int>()
#define ll long long int 
//std::setfill('0') << std::setw(5) << 25; it adds leaing zeroes;
#define f(i,a) for(ll i=0;i<a;i++)
#define fo(i,a) for(ll i=1;i<=a;i++)
#define foo(i,x,n,c) for(ll i=x;i<n;i+=c)
#define foi(i,x,n,c) for(ll i=x;i>=n;i+=c)
#define fauto(i,m) for(auto i:m)
#define forall(a) for( auto itr=a.begin();itr!=a.end();itr++)
#define ld long double
#define in push_back
#define vl vector<ll >
#define o(a) cout<<a
#define os(a) cout<<a<<" "
#define en cout<<"\n";
#define testcase ll t ;cin>>t; while(t--)
#define ff first
#define ss second
#define all(a) (a).begin(), (a).end()
#define sz(a)  (a).size()
#define prec(n) fixed<<setprecision(n)
#define mp make_pair
#define bitcount  __builtin_popcountll
#define imin o("imin");en;
//for interactive use endl after every output and fflush(stdout) after every input//
using namespace std;

void fastio()
{
    	ios::sync_with_stdio(0);
cin.tie(0);

}

int main()
{
fastio();
vl a(5001,-1);
ll l=0,r=0;
ll x=1;
while(r<5000)
{
	l=x;
	r=0;
	ll cnt=0,cur=1;
	while(cnt<x)
	{
		r+=cur;
		cur+=2;
		cnt++;
	}
	foo(i,l,min(r+1,(ll)5001),1)
	{
		if(a[i]==-1)
		a[i]=x;
	}
	x++;
}
testcase
{
ll n;
cin>>n;
os(a[n]);
en;
}
return 0;
}