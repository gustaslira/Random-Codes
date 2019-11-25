#include <iostream>
#include <string>
using namespace std;

int main() {
  
  int num1, num2;
  char operador;

  cout << "1° valor: ";
  cin >> num1;
  cout << "Operação: ";
  cin >> operador;
  cout << "2° valor: ";
  cin >> num2;

  if (operador == '+'){
    cout << endl;
    cout << num1 + num2 << endl;
  }

  if (operador == '*'){
    cout << endl;
    cout << num1 * num2 << endl;
  }

  if (operador == '-'){
    cout << endl;
    cout << num1 - num2 << endl;
  }

  if (operador == '/'){
    cout << endl;
    cout << num1 / num2 << endl;
  }
}