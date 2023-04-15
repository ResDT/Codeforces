#include <iostream>

using namespace std;


int main() {
    int amount;
    int lenth;

    cin >> amount;

    for (int step = 0; step < amount; ++step) {
        cin >> lenth;

        int array[lenth];

        for (int place = 0; place < lenth; ++place) {
            cin >> array[place];
        }

        for (int cut = 0; cut < lenth; ++cut) {
            int cut_last = cut;
            int res = array[cut_last];
            int d = 1;
            int m = 1;

            while (cut_last) {
                if (array[cut_last - 1] >= d + 1) {
                    res *= array[cut_last - 1];
                    ++d;
                    --cut_last;
                    ++m;
                }
            }

            cout << m << " ";
        }
    }

    return 0;
}
