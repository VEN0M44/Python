#include <iostream>

int main()
{
    int money = 0;
    std::string inp;
    while (true)
    {
        std::cout << money << " : ";
        getline(std::cin, inp);
        money += 1;
    }
}