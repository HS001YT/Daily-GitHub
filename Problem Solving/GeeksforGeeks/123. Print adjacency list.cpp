#include<bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<vector<int>> printGraph(int V, vector<pair<int, int>>& edges) {
        vector<vector<int>> adj(V);

        for (auto &e : edges) {
            int u = e.first;
            int v = e.second;

            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        return adj;
    }
};
