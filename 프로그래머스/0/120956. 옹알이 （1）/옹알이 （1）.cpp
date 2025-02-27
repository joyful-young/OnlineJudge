#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool can_speak(string word) {
    int i = 0;
    while (i < word.size()) {
        if (word[i] == 'a') {
            if (word.substr(i, 3) != "aya") return false;
            i += 3;
        } else if (word[i] == 'y') {
            if (word.substr(i, 2) != "ye") return false;
            i += 2;
        } else if (word[i] == 'w') {
            if (word.substr(i, 3) != "woo") return false;
            i += 3;
        } else if (word[i] == 'm') {
            if (word.substr(i, 2) != "ma") return false;
            i += 2;
        } else {
            return false;
        }
    }
    return true;
}

int solution(vector<string> babbling) {
    int answer = 0;
    for (auto& word: babbling) {
        if (can_speak(word)) answer++;
    }
    return answer;
}