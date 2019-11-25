#include <cstdlib> 
#include <ctime> 
#include <iostream>
using namespace std;

int main() 
{ 
    srand((unsigned)time(0)); 
    
    int destiny;
    destiny = (rand()%2)+1; 
    
    if (destiny==1){
    cout << "You were spared by Thanos." << endl;
    }
    
    if (destiny==2){
    cout << "You were slain by Thanos, for the good of the Universe." << endl;
    }
    return 0;
}