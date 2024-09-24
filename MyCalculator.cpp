#include <iostream>
using namespace std;

int main() {
    float Num1, Num2;
    cout << "Enter the first number: ";
    cin >> Num1;
    cout << "Enter the second number: ";
    cin >> Num2;

    int choice;
    while (true) { // Input validation
        cout << "Enter 1 to add, 2 to subtract, 3 to multiply and 4 to divide: ";
        cin >> choice;

        if (choice == 1 || choice == 2 || choice == 3 || choice == 4) {
            break;
        } else {
            cout << "That was not a valid choice! Please try again." << endl;
        }
    }

    float result;
    switch (choice) {
        case 1:
            result = Num1 + Num2;
        break;
        case 2:
            result = Num1 - Num2;
        break;
        case 3:
            result = Num1 * Num2;
        break;
        case 4:
            if (Num2 != 0) {
                result = Num1 / Num2;
            } else {
                cout << "Can't divide by zero" << endl;
                return 1;
            }
        break;
        default:

                cout << "Unexpected error" << endl;
        return 1; 
    }

    cout << "The answer is: " << result<<endl;
    return 0;
}
