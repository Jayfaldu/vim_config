#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp> 
#define pb push_back
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0)
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define f first
#define s second
#define int long long
#define sz(x) (ll)(x.size())
using namespace std;
using namespace __gnu_pbds;
 
template<typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
 
int getRand(int l, int r)
{
    uniform_int_distribution<int> uid(l, r);
    return uid(rng);
}

const int mod = 1e9+7;

int expo_pow(int x,int y){
 if(y == 0) return 1;
  y=y%(mod-1);
  x%=mod;
  if(y==0) y=mod-1;
  int res=1;
  while(y){
    if(y&1) res=(res*x)%mod;
    x=(x*x)%mod;
    y>>=1; 
  }
  return res;
}

ll add()
{
    return 0;
}

template <typename T, typename... Types>
T add(T var1, Types... var2){
    return (((((ll)(var1)) % mod + (ll)(add(var2...))) % mod) + mod) % mod;
}

ll mul(){
    return 1;
}

template <typename T, typename... Types>
T mul(T var1, Types... var2){
    return (((ll)(var1)) % mod * (ll)(mul(var2...))) % mod;
}

void solve(){

}


signed main(){
  fast;
  int test = 1;
  cin>>test;
  int i=1;
  while(test--){
    solve();
  }
}



