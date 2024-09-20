#include <stdio.h>

int main()
{
    float faturamento = 0.0, valor_venda;
    float limite = 54000;
    
     for (int i = 0; i<5; i++) {
         
         printf("Digite o valor dos cliente %d:", i + 1);
          scanf("%f", &valor_venda);
          
           faturamento += valor_venda;
     }
       if (faturamento > limite) {
           
           printf("Faturamento superou a loja B em: R$ %.2f\n", faturamento - limite);
      } else {
           
           printf("Faturamento nao atingiu a loja B: R$ %.2f\n", faturamento);
       } 
      
   printf("Ass. Pedro Tales");    
    
    return 0;
}
