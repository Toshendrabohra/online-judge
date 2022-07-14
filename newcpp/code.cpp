#include <bits/stdc++.h>



using namespace std;



#define endl "\n"



#define ll long long int



#define f(n) for (int i = 0; i < n; i++)



#define fo(n) for (int j = 0; j < n; j++)



#define foo(n) for (int i = 1; i <= n; i++)



#define ff first



#define ss second



#define pb push_back



#define pii pair<int, int>



#define vi vector<int>



#define vp vector<pii>



#define mod 1000000007



void fastio()



{



	ios_base::sync_with_stdio(0);



	cin.tie(0);



#ifndef ONLINE_JUDGE



	freopen("ain.txt", "r", stdin);



	freopen("aout.txt", "w", stdout);



#endif

}



int main()



{



	// fastio();



	int tt;



	cin >> tt;



	while (tt--)



	{



		ll n;



		cin >> n;



		if (((n % 4) & 1) || (n < 4))



		{



			cout << -1 << endl;



			continue;

		}



		ll mx = n / 4;



		ll mn = n / 6;



		if ((n % 6) & 1)



		{



			cout << -1 << endl;



			continue;

		}



		else if ((n % 6) == 4 || (n % 6) == 2)



		{



			mn++;

		}



		cout << mn << "  << endl<<endl;

	}

}

