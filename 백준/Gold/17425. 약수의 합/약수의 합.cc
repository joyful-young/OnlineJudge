// 17425. 약수의 합

#include <iostream>
int MAX_IDX = 1000001;
long long arr[1000001] = {0, };

int main() {
    std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
    std::cout.tie(NULL);
    int T, N;
    std::cin >> T;
    
    for (int i = 1; i < MAX_IDX; i++) {
        for (int j = i; j < MAX_IDX; j += i) {
            arr[j] += i;
        }
        arr[i] += arr[i - 1];
    }
    for (int i = 0; i < T; i++) {
        std::cin >> N;
        std::cout << arr[N] << "\n";
    }
    return 0;
}
