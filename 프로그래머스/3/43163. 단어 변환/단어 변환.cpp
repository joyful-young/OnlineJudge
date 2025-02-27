#include <string>
#include <vector>
#include <queue>

using namespace std;

bool can_convert(string word1, string word2) {
    vector<bool> check(word2.length(), false);
    int cnt = 0;
    bool is_duplicate;
    for (char c: word1) {
        is_duplicate = false;
        for (int i = 0; i < word2.length(); i++) {
            if (c == word2[i] && !check[i]) {
                check[i] = true;
                is_duplicate = true;
                break;
            }
        }
        if (!is_duplicate) cnt++;
        if (cnt > 1) return false;
    }
    return cnt == 1;
}

vector<vector<bool>> get_graph(vector<string>& words) {
    int n = words.size();
    vector<vector<bool>> graph(n, vector<bool>(n, false));
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (can_convert(words[i], words[j])) {
                graph[i][j] = true;
                graph[j][i] = true;
            }
        }
    }
    return graph;
}

int bfs(vector<vector<bool>>& graph, vector<int>& visited, 
        vector<string>& words, string target) {
    // begin 단어 노드 방문 처리
    queue<int> q; q.push(words.size() - 1);
    visited[words.size() - 1] = 0;
    
    while (!q.empty()) {
        int t = q.front(); q.pop();
        if (words[t] == target) {
            return visited[t];
        }
        for (int i = 0; i < graph.size(); i++) {
            if (graph[t][i] && visited[i] == -1) {
                visited[i] = visited[t] + 1;
                q.push(i);
            }
        }
    }
    return 0;
}

int solution(string begin, string target, vector<string> words) {
    words.push_back(begin);
    vector<vector<bool>> graph = get_graph(words);
    vector<int> visited(words.size(), -1);
    return bfs(graph, visited, words, target);
}