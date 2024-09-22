#include <stdio.h>

int main() {
    float valorCompra, desconto, valorFinal;
    
    printf("Valor da Compra\tDesconto\tValor Final\n");
    printf("----------------------------------------------\n");

    
    for (valorCompra = 500; valorCompra <= 3000; valorCompra += 100) {
        
        if (valorCompra > 500) {
            desconto = (valorCompra - 500) / 100;
            if (desconto > 25) {
                desconto = 25; 
            }
        } else {
            desconto = 1; 
        }

       
        valorFinal = valorCompra - (valorCompra * desconto / 100);

       
        printf("R$ %.2f\t\t%.0f%%\t\tR$ %.2f\n", valorCompra, desconto, valorFinal);
    }

    return 0;
}