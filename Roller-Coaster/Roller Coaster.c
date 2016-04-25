#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
    int L;
    int C;
    int N;
    scanf("%d%d%d", &L, &C, &N);
    int* queue = malloc(sizeof(int)*N);
    for (int i = 0; i < N; i++) {
        int Pi;
        scanf("%d", &Pi);
        queue[i] = Pi;
    }


    long long dirhams = 0;
    if (C < N) {
        int index = 0;
        for (int i = 0; i < C; i++) {
            
            int rem_places = L;
            int begin_index = index;
            while (queue[index] <= rem_places) {
                rem_places -= queue[index];
                if (index < N - 1)
                    ++index;
                else
                    index = 0;
                if (index == begin_index)
                    break;
            }
            dirhams += L - rem_places; 
        }
    } else {
        int* incasari = malloc(sizeof(int)*N);
        int* indecsi = malloc(sizeof(int)*N);
        for (int i = 0; i < N; i++) {
            int index = i;
            int rem_places = L;
            int begin_index = index;
            while (queue[index] <= rem_places) {
                rem_places -= queue[index];
                if (index < N - 1)
                    ++index;
                else
                    index = 0;
                if (index == begin_index)
                    break;
            }
            incasari[i] += L - rem_places;
            indecsi[i] = index;
        }
        int index = 0;
        for (int i = 0; i < C; i++) {
            dirhams += incasari[index];
            index = indecsi[index];
        }
    }
    // Write an action using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("%llu\n", dirhams);

    return 0;
}
