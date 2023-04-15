#include <string>
#include <iostream>

using namespace std;


int main() {
    bool flag;

    int amount;
    int lenth;
    int x;
    int y;

    string str;
    char letter;

    string U = "U";
    string D = "D";
    string R = "R";
    string L = "L";

    cin >> amount;

    for (int step = 1; step <= amount; ++step) {
        x = 0;
        y = 0;

        cin >> lenth;
        cin >> str;

        for (int place = 0; place < lenth; ++place) {
            flag = false;
            letter = str[place];

            if (U.find(letter) + 1 != 0) {
                ++y;
            } else if (D.find(letter) + 1 != 0) {
                --y;
            } else if (R.find(letter) + 1 != 0) {
                ++x;
            } else if (L.find(letter) + 1 != 0) {
                --x;
            }

            if (x == 1 && y == 1) {
                cout << "Yes\n";

                flag = true;

                break;
            }
        }

        if (!flag) {
            cout << "No\n";
        }
    }

    return 0;
}
