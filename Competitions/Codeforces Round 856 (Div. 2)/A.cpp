#include <iostream>

using namespace std;


int main() {
    int n;

    cin >> n;

    char array[n] = {0};

    cin.getline(array, n, ',');

    cout << array[1];
}
