#include <string>
#include <iostream>
#include <cstdio>

using namespace std;


int main() {
    int amount;
    string str = "codeforces";
    char letter;

    scanf("%d", &amount);

    for (int step = 1; step <= amount; ++step) {
        cin >> letter;

        if (str.find(letter) + 1) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }

    return 0;
}
