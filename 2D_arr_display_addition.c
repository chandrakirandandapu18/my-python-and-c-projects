#include <stdio.h>

void accept(int [20][20], int, int);
void display(int [20][20], int, int);
void add_matrix(int [20][20], int [20][20], int [20][20], int, int);

int main(void)
{
    int a[20][20], b[20][20], sum[20][20], r, c;

    printf("Enter no.of rows ans ciols : ");
    if (scanf("%d%d", &r, &c) != 2)
        return 1;

    printf("Enter %d no.of elements in matrix A :", r * c);
    accept(a, r, c);

    printf("Enter %d no.of elements in matrix B :", r * c);
    accept(b, r, c);

    printf("Given elements in matrix A:\n");
    display(a, r, c);

    printf("Given elements in matrix B:\n");
    display(b, r, c);

    printf("After addition:\n");
    add_matrix(a, b, sum, r, c);
    display(sum, r, c);

    return 0;
}

void accept(int x[20][20], int m, int n)
{
    int i, j;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &x[i][j]);
        }
    }
}

void display(int x[20][20], int m, int n)
{
    int i, j;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%d ", x[i][j]);
        }
        printf("\n");
    }
}

void add_matrix(int x[20][20], int y[20][20], int z[20][20], int m, int n)
{
    int i, j;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            z[i][j] = x[i][j] + y[i][j];
        }
    }
}
