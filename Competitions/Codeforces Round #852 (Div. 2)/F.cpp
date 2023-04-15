#include <iostream>

using namespace std;


int main() {
    int n, q;

    cin >> n >> q;

    char array[n] = {0};

    cin.getline(array, n, ' ');

    cout << array[0];
}
