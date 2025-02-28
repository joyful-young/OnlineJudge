#include <iostream>
#include <vector>
#include <queue>
#define INF 1000000

using namespace std;

void dijkstra(vector<vector<pair<int, int>>>& adjL, vector<int>& dist, int start) {
    dist[start] = 0;

    // pq 초기화
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});
    
    while (!pq.empty()) {
        int cost = -pq.top().first;
        int v = pq.top().second;
        pq.pop();

        if (dist[v] < cost) continue;

        for (auto [w, d]: adjL[v]) {
            // start -> w보다 s -> v -> w가 작으면 갱신하고 큐에 넣기
            int via_cost = cost + d;
            if (via_cost < dist[w]) {
                dist[w] = via_cost;
                pq.push({-via_cost, w});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int V, E, K;
    cin >> V >> E;
    cin >> K;

    vector<vector<pair<int, int>>> adjL(V + 1);
    int u, v, w;
    for (int i = 0; i < E; i++){
        cin >> u >> v >> w;
        adjL[u].emplace_back(v, w);
    }

    vector<int> dist(V + 1, INF);
    dijkstra(adjL, dist, K);
    for (int i = 1; i <= V; i++) {
        if (dist[i] == INF) {
            cout << "INF" << "\n";
        } else {
            cout << dist[i] << "\n";
        }
    }
    
    return 0;
}