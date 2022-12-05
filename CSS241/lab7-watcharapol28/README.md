# System of Linear Equation

## 1.Basic Gaussian Elimination and Back Substitution</br >

```math
\begin{align*}
6x_1 -2x_2 +2x_3+4x_4 &= 16  \\
12 x_1 -8x_2 +6x_3 +10x_4 &=26\\
3x_1 -13x_2 +9x_3 +3x_4 &= -19\\
-6x_1 +4x_2 +x_3 -18x_4 &= -34
\end{align*}
```
Solution is </br >
```math
x_1 =3, x_2=1, x_3= -2, x_4 =1
```

## 2 Gaussian Elimination with Scaled Partial Pivoting</br >
```math
\begin{align*}
3x_1 -13x_2 +9x_3+3x_4 &= -19  \\
-6 x_1 +4x_2 +x_3 -18x_4 &= -34\\
6x_1 -2x_2 +2x_3 +4x_4 &= 16\\
12x_1 -8x_2 +6x_3 +10x_4 &= 26
\end{align*}
```
Solution is </br >
```math
x_1 =3, x_2=1, x_3= -2, x_4 =1
```

## 3. Dict of primes whose key is the index of prime number.
```math
\begin{Bmatrix}
1  & .5 & 0 &  0\\
.5 & 1  & .5&  0\\
0  & .5 & 1 &  .5\\
0 &   0 & .5&  1
\end{Bmatrix}\begin{Bmatrix} x_1\\x_2\\x_3\\x_4 \end{Bmatrix}= \begin{Bmatrix}1.5\\2\\2\\1.5\end{Bmatrix}

 ```
 คำตอบคือ
 ```math
\begin{Bmatrix} x_1\\x_2\\x_3\\x_4 \end{Bmatrix}= \begin{Bmatrix}1.\\1.\\1.\\1.\end{Bmatrix}
 ```
