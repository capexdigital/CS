#include <stdio.h>

int main() {
    int numeros[1000];
    int i;

    for (i = 0; i < 1000; i++) {
        numeros[i] = i;
    }

    for (i = 0; i < 1000; i++) {
        if (numeros[i] % 2 == 0) {
            printf("%d\n", numeros[i]);
        }
    }
    return 0;
}
