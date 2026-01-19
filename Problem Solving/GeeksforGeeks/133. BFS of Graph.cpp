#include<bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> bfs(vector<vector<int>> &adj) {
        int V = adj.size();
        vector<int> bfsTraversal;
        vector<bool> visited(V, false);
        queue<int> q;

        // Start BFS from node 0
        visited[0] = true;
        q.push(0);

        while (!q.empty()) {
            int node = q.front();
            q.pop();
            bfsTraversal.push_back(node);

            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        return bfsTraversal;
    }
};
