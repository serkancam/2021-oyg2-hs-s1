#include <stdio.h>
int min(int x, int y, int z) {
if (x < y) {
if (x < z)
return x;
else
return z;
} else if (y < z) {
return y;
} else
return z;
}
int d(char* a, char* b, int n, int m) {
if (n == 0)
return m;
if (m == 0)
return n;
if (a[n-1] == b[m-1])
return d(a, b, n-1, m-1);
return 1 + min(d(a, b, n, m-1), d(a, b, n-1, m),
d(a, b, n-1, m-1));
}
int main() {
printf("%d ", d("1111", "1100", 4, 4));
printf("%d ", d("01", "1100", 2, 4));
printf("%d", d("araba", "aba", 6, 3));
}