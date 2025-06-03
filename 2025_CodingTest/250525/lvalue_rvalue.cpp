#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

int main()
{
    string a = "abc";

    vector<string> vec;

    string b = std::move(a);
    vec.push_back(b);
    vec.push_back("def");

    std::cout << a << std::endl;

    a = "zzz";

    for (auto elem : vec)
    {
        std::cout << elem << std::endl;
    }

    std::cout << a << std::endl;
}