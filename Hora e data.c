#include <stdio.h>
int main() {
    int t, d, dia, mes, ano, hora, minuto;
    printf("DATA E HORA\n");
    printf("Digite o dia: ");
    scanf("%d",&dia);
    printf("Digite o mês: ");
    scanf("%d",&mes);
    printf("Digite o ano: ");
    scanf("%d",&ano);
    if (mes == 1)
    printf("%d/Janeiro/%d",dia,ano);
    printf("Vamos dormir");
    
return 0;
}