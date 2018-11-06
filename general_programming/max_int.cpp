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
# A integer could be 32 or 64 bits, it depends on the operating system or the complier. 
# 一个比特用于表示正负号，所以是2的31次方。又因为从0开始，不是从1，所以要-1.
# signed int value: -(2**31) ~ 2**31-1
# unsigned int value: 0 ~ 2**32
