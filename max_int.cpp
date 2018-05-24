#include <iostream>
#include <string>
#include <math.h>

int main()
{
    int a;
    a = 2147483647+1;
    int b;
    b = pow(2,33);;
    std::cout<<a<<std::endl;
    std::cout<<b;

}

/*
result:
-2147483648
2147483647
*/

// 最大值为2的31次方-1，即2147483647。
