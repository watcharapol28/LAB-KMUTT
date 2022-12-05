# System of Linear Equation
You must use the algorithm name specified in each problem

## 1.Solving Linear System of Equations through LU decomposition</br >

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
x_1 =3, x_2=1, x_3= -2, x_4 =1,\\
	 L=\begin{Bmatrix}
		1&0&0&0\\
		2&1&0&0\\
		0.5&3&1&0\\
		-1&-0.5&2&1
	\end{Bmatrix},
     U=\begin{Bmatrix}
     	6&-2&2&4\\
     	0&-4&2&2\\
     	0&0&2&-5\\
     	0&0&0&-3
     \end{Bmatrix}
```

## 2 Jacobi iterative method</br >
```math
A = \begin{Bmatrix}
2&-1&0\\
-1&3&-1\\
0&-1&2
\end{Bmatrix}, b = \begin{Bmatrix}
1\\
8\\
-5
\end{Bmatrix}
```
Solution is </br >
```math
x_1 =2, x_2=3, x_3= -1
```
