#include<iostream>
using namespace std;

int withdrawmoney(int current ,int amount)
{
    if (current >= amount)
    {
        current = current - amount;
        return current;
    }
    else
    {
        cout<<"Insufficient Balance"<<endl;
        return current;
    }