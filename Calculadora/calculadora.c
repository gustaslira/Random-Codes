#include<stdio.h>
#include<math.h>

int main()
{
    float num1,num2,result;
    char op;
  
    printf("1° valor: ");
    scanf("%f",&num1);
    printf("Operação: ");
    scanf(" %c",&op);
    printf("2° valor: ");
    scanf("%f",&num2);

    if (op == '+'){
      printf("%f",result=num1+num2);
    }
    if (op == '-'){
      printf("%f",result=num1-num2);
    }
    if (op == '*'){
      printf("%f",result=num1*num2);
    }
    if (op == '/'){
      printf("%f",result=num1/num2);
    }
    return 0;
}
        