#include <iostream>
using namespace std;
int main()
{
  int a = 2;
  double const b = 4;
  
  float c = 1.5;
  char d = 'A';
  
  printf("The value of a is %d\n",a);
  printf("The value of b is %lf\n",b);
  printf("The value of c is %.2f\n",c);
  printf("The value of c is %.4f\n",c);
  printf("The value of d is %c\n",d);
  cout<<"The value of a is "<<a<<"\n";
  cout<<"The value of b is "<<b<<"\n";
  cout<<"The value of c is "<<c<<"\n";
  cout<<"The value of d is "<<d<<"\n";
  return 0;
}
