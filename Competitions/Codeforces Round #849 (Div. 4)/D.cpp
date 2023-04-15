#include <string>
#include <iostream>
#include <cstdio>

using namespace std;


int f(string str);


int main() {
    int amount;
    int lenth;
    int max;

    string str;
    string fir_str;
    string sec_str;

    cin >> amount;

    for (int step = 1; step <= amount; ++step) {
        max = 0;

        cin >> lenth;
        cin >> str;

        for (int place = 0; place < lenth / 2; ++place) {
            string fir_str = str;
            string sec_str = str;
            string sec_fir_str = str;
            string sec_sec_str = str;

            fir_str.erase(place + 1, lenth - 1);
            sec_str.erase(0, place + 1);

            sec_fir_str.erase(lenth - 1 - place, lenth - 1);
            sec_sec_str.erase(0, lenth - 1 - place);

            if (f(fir_str) + f(sec_str) > max) {
                max = f(fir_str) + f(sec_str);
            }

            if (f(sec_fir_str) + f(sec_sec_str) > max) {
                max = f(sec_fir_str) + f(sec_sec_str);
            }

                cout << fir_str;
                cout << ", ";
                cout << sec_str;
                cout << " ";
                cout << sec_fir_str;
                cout << ", ";
                cout << sec_sec_str;
                cout << "\n";

        }

        cout << max;
        cout << "\n";
    }

    return 0;
}


int f(string str) {
    int sum = 0;
    int array[26] = {0};
    int letter;

    for (int place = 0; place < str.size(); ++place) {
        letter = str[place];
        array[letter - 97] = 1;
    }

    for (int place = 0; place < 26; ++place) {
        if (array[place] != 0) {
            sum++;
        }
    }

    return sum;
}
