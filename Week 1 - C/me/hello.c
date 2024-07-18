// This program accepts user's name, and greats the user with the name.
#include <cs50.h>
#include <stdio.h>

void print_me(string name);

int main(void)
{
    // This code receives input (name) from the user
    string name = get_string("What is your name? ");
    // Function call to print the greeting
    print_me(name);
}

// This function print the greeting
void print_me(string name)
{
    printf("Hello, %s\n", name);
}