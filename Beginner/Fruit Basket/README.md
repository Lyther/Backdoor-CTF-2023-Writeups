# Beginner/Fruit Basket

🍎🍌🍇🍓🍊🥭🍍🍑🍈🍉

nc 34.70.212.151 8006

Downloads: [chal](./chal)

## Solution

The key to this challenge is the random seed. In C language, this seed is set to the server time (up to seconds). In previous challenge we can see the server is using UTC time.

1. Change my local machine to UTC time zone.
2. Generate the random sequence with current time.

The code in C language as follow:

```c
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
```

The result might be wrong due to the latency between local machine and the server, try some times more.

## Flag

```plaintext
flag{fru17s_w3r3nt_r4nd0m_4t_a11}
```

