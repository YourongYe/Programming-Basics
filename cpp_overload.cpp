
#include <iostream>
#include <string>

using namespace std;

int add(int a, int b){
    return a+b;
}

int add(int a, int b, int c){
    return a+b+c;
}

std::string add(std::string a, std::string b, std::string c){
    return a+"+"+b+"+"+c;
}

int main()
{
    cout<<add(1,2)<<endl;
    cout<<add(1,2,3)<<endl;
    cout<<add("a","b","blabla")<<endl;

    return 0;
}
