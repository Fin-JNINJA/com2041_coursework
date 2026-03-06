#include <iostream>
#include <fstream>
using namespace std;

int main() {

    string text;
    ifstream InputFile;
    InputFile.open("../src/ukenglish.txt");
    while (InputFile >> text){
        cout<<text<<endl;

    }
    return 0;
}