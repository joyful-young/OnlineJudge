#include <iostream>
void solve() {
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < n - i; j++) {
            std::cout << " ";
        }
        for (int k = 0; k < i; k++) {
            std::cout << "*";
        }
        std::cout << "\n";
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            std::cout << " ";
        }
        for (int k = 0; k < n - i; k++) {
            std::cout << "*";
        }
        if (i != n - 1) {
            std::cout << "\n";
        }
    }
}

int main() {
    solve();
    return 0;
}