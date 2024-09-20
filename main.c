#include <stdio.h>

int main() {
    float a, b, c;
    float temp;

    printf("Digite o valor A: ");
    scanf("%f", &a);
    printf("Digite o valor B: ");
    scanf("%f", &b);
    printf("Digite o valor C: ");
    scanf("%f", &c);
    printf("Ordem lida: %.2f, %.2f, %.2f\n", a, b, c);
    if (a > b) {
        temp = a;
        a = b;
        b = temp;
    }
    if (a > c) {
        temp = a;
        a = c;
        c = temp;
    }
    if (b > c) {
        temp = b;
        b = c;
        c = temp;
    }

    printf("Ordem crescente: %.2f, %.2f, %.2f\n", a, b, c);
    printf("Ordem decrescente: %.2f, %.2f, %.2f\n", c, b, a);

    return 0;
}
