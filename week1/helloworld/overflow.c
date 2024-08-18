#include <cs50.h>
#include <stdio.h>
 
int main(void)
{
  int x = get_float("x: ");
  int y = get_float("y: ");

  printf("%i\n", x + y);
}
