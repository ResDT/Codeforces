#include <string>
#include <iostream>

using namespace std;


int main() {
    int amount;
    int lenth;

    string str;

    cin >> amount;

    for (int step = 1; step <= amount; ++step) {
        cin >> lenth;
        cin >> str;

        while (str.size() > 0 && str[0] != str[str.size() - 1]) {
            str.erase(0, 1);
            str.pop_back();
        }

        if (!str.size()) {
            cout << 0;
        } else {
            cout << str.size();
        }

        cout << "\n";
    }

    return 0;
}
