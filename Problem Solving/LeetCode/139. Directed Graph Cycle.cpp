#include<bits/stdc++.h>
using namespace std;

class Solution {
  public:
    bool dfs(int node, vector<vector<int>> &adj,
             vector<bool> &visited, vector<bool> &recStack) {
        
        visited[node] = true;
        recStack[node] = true;

        for (int neigh : adj[node]) {
            if (!visited[neigh]) {
                if (dfs(neigh, adj, visited, recStack))
                    return true;
            }
            else if (recStack[neigh]) {
                return true; // cycle detected
            }
        }

        recStack[node] = false;
        return false;
    }

    bool isCyclic(int V, vector<vector<int>> &edges) {
        vector<vector<int>> adj(V);
        
        // build adjacency list from edge list
        for (auto &e : edges) {
            adj[e[0]].push_back(e[1]);
        }

        vector<bool> visited(V, false);
        vector<bool> recStack(V, false);

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (dfs(i, adj, visited, recStack))
                    return true;
            }
        }
        return false;
    }
};
