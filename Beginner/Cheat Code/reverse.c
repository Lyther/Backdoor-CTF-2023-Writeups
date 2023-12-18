#include <stdio.h>

int main() {
    char v4[16] = {27, 25, 81, 30, 36, 13, 0, 13, 120, 65, 110, 32, 114, 12, 2, 24};
    char v5[16] = "flag{c4n't_HESOY";
    char v6[16] = "xxxxxxxxxxxxxxxx";

    for (int i = 0; i < 16; i++) {
        char result = (char)(*(i+v4) ^ v5[i]);
        printf("%c ", result);
        v6[15-i] = result;
    }
    printf("\n");
    for (int i = 0; i < 16; i++) {
        printf("%c", v5[i]);
    }
    for (int i = 0; i < 16; i++) {
        printf("%c", v6[i]);
    }
    return 0;
}