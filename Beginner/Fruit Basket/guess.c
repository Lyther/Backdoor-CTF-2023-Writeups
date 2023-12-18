#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char* fruits[10] = {"Apple", "Orange", "Mango", "Banana", "Pineapple", "Watermelon", "Guava", "Kiwi", "Strawberry", "Peach"};

int main() {
    srand(time(0LL));
    for (int i = 0; i <= 49; i++) {
        int r = rand() % 10;
        printf("%s\n", fruits[r]);
    }
}