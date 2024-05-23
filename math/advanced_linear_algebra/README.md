# Resources

##Read or watch:

The determinant | Essence of linear algebra
Determinant of a Matrix
Determinant
Determinant of an empty matrix
Inverse matrices, column space and null space
Inverse of a Matrix using Minors, Cofactors and Adjugate
Minor
Cofactor
Adjugate matrix
Singular Matrix
Elementary Matrix Operations
Gaussian Elimination
Gauss-Jordan Elimination
Matrix Inverse
Eigenvectors and eigenvalues | Essence of linear algebra
Eigenvalues and eigenvectors
Eigenvalues and Eigenvectors
Definiteness of a matrix Up to Eigenvalues
Definite, Semi-Definite and Indefinite Matrices Ignore Hessian Matrices
Tests for Positive Definiteness of a Matrix
Positive Definite Matrices and Minima
Positive Definite Matrices
As references:

numpy.linalg.eig
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is a determinant? How would you calculate it?
What is a minor, cofactor, adjugate? How would calculate them?
What is an inverse? How would you calculate it?
What are eigenvalues and eigenvectors? How would you calculate them?
What is definiteness of a matrix? How would you determine a matrix’s definiteness?
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 16.04 LTS using python3 (version 3.5)
Your files will be executed with numpy (version 1.15)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5)
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
Unless otherwise noted, you are not allowed to import any module
All your files must be executable
The length of your files will be tested using wc
Quiz questions
Great! You've completed the quiz successfully! Keep going! (Hide quiz)
Question #0
What is the determinant of the following matrix?

[[ -7, 0, 6 ]
  [ 5, -2, -10 ]
  [ 4, 3, 2 ]]


-14


14


-44


44

Question #1
What is the definiteness of the following matrix:

[[ -1, 2, 0 ]
  [ 2, -5, 2 ]
  [ 0, 2, -6 ]]


Negative definite


Indefinite


Negative semi-definite


Positive definite


Positive semi-definite

Question #2
What is the definiteness of the following matrix:

[[ 2, 2, 1 ]
  [ 2, 1, 3 ]
  [ 1, 3, 8 ]]


Negative definite


Indefinite


Negative semi-definite


Positive definite


Positive semi-definite

Question #3
What is the cofactor of the following matrix?

[[ 6, -9, 9 ],
  [ 7, 5, 0 ],
  [ 4, 3, -8 ]]


[[ -40, 56, 1 ],
        [ -45, -84, -54 ],
        [ -45, 63, 93 ]]


[[ -40, 56, 1 ],
        [ -44, -84, -54 ],
        [ -45, 63, 93 ]]


[[ -40, 56, 1 ],
       [ -45, -84, -54 ],
       [ -45, 64, 93 ]]


[[ -40, 56, 1 ],
        [ -44, -84, -54 ],
        [ -45, 64, 93 ]]

Question #4
What is the adjugate of the following matrix?

[[ -4, 1, 9 ],
  [ -9, -8, -5 ],
  [ -3, 8, 10 ]]


[[ -40, 62, 67 ],
        [ 105, -14, -101 ],
        [ -96, 29, 41 ]]


[[ -40, 62, 67 ],
       [ 105, -13, -101 ],
       [ -96, 29, 41 ]]


[[ -40, 62, 67 ],
        [ 105, -13, -101 ],
        [ -97, 29, 41 ]]


[[ -40, 62, 67 ],
        [ 105, -14, -101 ],
        [ -97, 29, 41 ]]

Question #5
Which of the following are also eigenvalues (λ) and eigenvectors (v) of A where
A = [[-2, -4, 2],
          [-2, 1, 2],
          [4, 2, 5]]


λ = 6; v = [[1], [6], [16]]


λ = -3; v = [[4], [-2], [3]]


λ = 5; v = [[2], [1], [1]]


λ = -5; v = [[-2], [-1], [1]]

Question #6
Is the following matrix invertible? If so, what is its inverse?

[[ 2, 1, 2 ]
  [ 1, 0, 1 ]
  [ 4, 1, 4 ]]


It is singular


[[ 4, 1, 4 ]
       [ 1, 0, 1 ]
      [ 2, 1, 2 ]]


[[ 4, 1, 2 ]
       [ 1, 0, 1 ]
       [ 4, 1, 2 ]]


[[ 2, 1, 4 ]
       [ 1, 0, 1 ]
       [ 2, 1, 4 ]]

Question #7
What is the minor of the following matrix?

[[ -7, 0, 6 ]
  [ 5, -2, -10 ]
  [ 4, 3, 2 ]]


[[ 26, 50, 23 ]
       [ -18, -39, -21 ]
       [ 12, 40, 15 ]]


[[ 26, 50, 23 ]
       [ -18, -39, -21 ]
       [ 12, 40, 14 ]]


[[ 26, 50, 23 ]
       [ -18, -38, -21 ]
       [ 12, 40, 15 ]]


[[ 26, 50, 23 ]
       [ -18, -38, -21 ]
       [ 12, 40, 14 ]]

Question #8
Is the following matrix invertible? If so, what is its inverse?

[[ 1, 0, 1 ]
  [ 2, 1, 2 ]
  [ 1, 0, -1 ]]


It is singular


[[ 0.5, 0, 0.5 ]
       [ 2, 1, 0 ]
       [ 0.5, 0, 0.5 ]]


[[ 0.5, 0, 0.5 ]
       [ 0, 1, 2 ]
       [ 0.5, 0, 0.5 ]]


[[ 0.5, 0, 0.5 ]
       [ -2, 1, 0 ]
       [ 0.5, 0, -0.5 ]]

Question #9
Given
A = [[-2, -4, 2],
          [-2, 1, 2],
          [4, 2, 5]]
v = [[2], [-3], [-1]]
Where v is an eigenvector of A, calculate A10v


None of the above


[[2048], [-3072], [-1024]]


[[118098], [-177147], [-59049]]


[[2097152], [-3145728], [-1048576]]

Question #10
What is the definiteness of the following matrix:

[[ 2, 1, 1 ]
  [ 1, 2, -1 ]
  [ 1, -1, 2 ]]


Negative definite


Indefinite


Negative semi-definite


Positive definite


Positive semi-definite

Tasks
0. Determinant
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a function def determinant(matrix): that calculates the determinant of a matrix:

matrix is a list of lists whose determinant should be calculated
If matrix is not a list of lists, raise a TypeError with the message matrix must be a list of lists
If matrix is not square, raise a ValueError with the message matrix must be a square matrix
The list [[]] represents a 0x0 matrix
Returns: the determinant of matrix
alexa@ubuntu-xenial:advanced_linear_algebra$ cat 0-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    determinant = __import__('0-determinant').determinant

    mat0 = [[]]
    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(determinant(mat0))
    print(determinant(mat1))
    print(determinant(mat2))
    print(determinant(mat3))
    print(determinant(mat4))
    try:
        determinant(mat5)
    except Exception as e:
        print(e)
    try:
        determinant(mat6)
    except Exception as e:
        print(e)
alexa@ubuntu-xenial:advanced_linear_algebra$ ./0-main.py 
1
5
-2
0
192
matrix must be a list of lists
matrix must be a square matrix
alexa@ubuntu-xenial:advanced_linear_algebra$
Repo:

GitHub repository: alu-machine_learning
Directory: math/advanced_linear_algebra
File: 0-determinant.py
 
8/8 pts
1. Minor
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a function def minor(matrix): that calculates the minor matrix of a matrix:

matrix is a list of lists whose minor matrix should be calculated
If matrix is not a list of lists, raise a TypeError with the message matrix must be a list of lists
If matrix is not square or is empty, raise a ValueError with the message matrix must be a non-empty square matrix
Returns: the minor matrix of matrix
alexa@ubuntu-xenial:advanced_linear_algebra$ cat 1-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    minor = __import__('1-minor').minor

    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(minor(mat1))
    print(minor(mat2))
    print(minor(mat3))
    print(minor(mat4))
    try:
        minor(mat5)
    except Exception as e:
        print(e)
    try:
        minor(mat6)
    except Exception as e:
        print(e)
alexa@ubuntu-xenial:advanced_linear_algebra$ ./1-main.py 
[[1]]
[[4, 3], [2, 1]]
[[1, 1], [1, 1]]
[[-12, -36, 0], [10, -34, -32], [47, 13, -16]]
matrix must be a list of lists
matrix must be a non-empty square matrix
alexa@ubuntu-xenial:advanced_linear_algebra$
Repo:

GitHub repository: alu-machine_learning
Directory: math/advanced_linear_algebra
File: 1-minor.py
 
7/7 pts
2. Cofactor
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a function def cofactor(matrix): that calculates the cofactor matrix of a matrix:

matrix is a list of lists whose cofactor matrix should be calculated
If matrix is not a list of lists, raise a TypeError with the message matrix must be a list of lists
If matrix is not square or is empty, raise a ValueError with the message matrix must be a non-empty square matrix
Returns: the cofactor matrix of matrix
alexa@ubuntu-xenial:advanced_linear_algebra$ cat 2-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    cofactor = __import__('2-cofactor').cofactor

    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(cofactor(mat1))
    print(cofactor(mat2))
    print(cofactor(mat3))
    print(cofactor(mat4))
    try:
        cofactor(mat5)
    except Exception as e:
        print(e)
    try:
        cofactor(mat6)
    except Exception as e:
        print(e)
alexa@ubuntu-xenial:advanced_linear_algebra$ ./2-main.py 
[[1]]
[[4, -3], [-2, 1]]
[[1, -1], [-1, 1]]
[[-12, 36, 0], [-10, -34, 32], [47, -13, -16]]
matrix must be a list of lists
matrix must be a non-empty square matrix
alexa@ubuntu-xenial:advanced_linear_algebra$
Repo:

GitHub repository: alu-machine_learning
Directory: math/advanced_linear_algebra
File: 2-cofactor.py
 
7/7 pts
3. Adjugate
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a function def adjugate(matrix): that calculates the adjugate matrix of a matrix:

matrix is a list of lists whose adjugate matrix should be calculated
If matrix is not a list of lists, raise a TypeError with the message matrix must be a list of lists
If matrix is not square or is empty, raise a ValueError with the message matrix must be a non-empty square matrix
Returns: the adjugate matrix of matrix
alexa@ubuntu-xenial:advanced_linear_algebra$ cat 3-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    adjugate = __import__('3-adjugate').adjugate

    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(adjugate(mat1))
    print(adjugate(mat2))
    print(adjugate(mat3))
    print(adjugate(mat4))
    try:
        adjugate(mat5)
    except Exception as e:
        print(e)
    try:
        adjugate(mat6)
    except Exception as e:
        print(e)
alexa@ubuntu-xenial:advanced_linear_algebra$ ./3-main.py 
[[1]]
[[4, -2], [-3, 1]]
[[1, -1], [-1, 1]]
[[-12, -10, 47], [36, -34, -13], [0, 32, -16]]
matrix must be a list of lists
matrix must be a non-empty square matrix
alexa@ubuntu-xenial:advanced_linear_algebra$
Repo:

GitHub repository: alu-machine_learning
Directory: math/advanced_linear_algebra
File: 3-adjugate.py
 
7/7 pts
4. Inverse
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a function def inverse(matrix): that calculates the inverse of a matrix:

matrix is a list of lists whose inverse should be calculated
If matrix is not a list of lists, raise a TypeError with the message matrix must be a list of lists
If matrix is not square or is empty, raise a ValueError with the message matrix must be a non-empty square matrix
Returns: the inverse of matrix, or None if matrix is singular
alexa@ubuntu-xenial:advanced_linear_algebra$ cat 4-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    inverse = __import__('4-inverse').inverse

    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(inverse(mat1))
    print(inverse(mat2))
    print(inverse(mat3))
    print(inverse(mat4))
    try:
        inverse(mat5)
    except Exception as e:
        print(e)
    try:
        inverse(mat6)
    except Exception as e:
        print(e)
alexa@ubuntu-xenial:advanced_linear_algebra$ ./4-main.py 
[[0.2]]
[[-2.0, 1.0], [1.5, -0.5]]
None
[[-0.0625, -0.052083333333333336, 0.24479166666666666], [0.1875, -0.17708333333333334, -0.06770833333333333], [0.0, 0.16666666666666666, -0.08333333333333333]]
matrix must be a list of lists
matrix must be a non-empty square matrix
alexa@ubuntu-xenial:advanced_linear_algebra$
Repo:

GitHub repository: alu-machine_learning
Directory: math/advanced_linear_algebra
File: 4-inverse.py
 
7/7 pts
5. Definiteness
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a function def definiteness(matrix): that calculates the definiteness of a matrix:

matrix is a numpy.ndarray of shape (n, n) whose definiteness should be calculated
If matrix is not a numpy.ndarray, raise a TypeError with the message matrix must be a numpy.ndarray
If matrix is not a valid matrix, return None
Return: the string Positive definite, Positive semi-definite, Negative semi-definite, Negative definite, or Indefinite if the matrix is positive definite, positive semi-definite, negative semi-definite, negative definite of indefinite, respectively
If matrix does not fit any of the above categories, return None
You may import numpy as np
alexa@ubuntu-xenial:advanced_linear_algebra$ cat 5-main.py 
#!/usr/bin/env python3

if __name__ == '__main__':
    definiteness = __import__('5-definiteness').definiteness
    import numpy as np

    mat1 = np.array([[5, 1], [1, 1]])
    mat2 = np.array([[2, 4], [4, 8]])
    mat3 = np.array([[-1, 1], [1, -1]])
    mat4 = np.array([[-2, 4], [4, -9]])
    mat5 = np.array([[1, 2], [2, 1]])
    mat6 = np.array([])
    mat7 = np.array([[1, 2, 3], [4, 5, 6]])
    mat8 = [[1, 2], [1, 2]]

    print(definiteness(mat1))
    print(definiteness(mat2))
    print(definiteness(mat3))
    print(definiteness(mat4))
    print(definiteness(mat5))
    print(definiteness(mat6))
    print(definiteness(mat7))
    try:
        definiteness(mat8)
    except Exception as e:
        print(e)
alexa@ubuntu-xenial:advanced_linear_algebra$ ./5-main.py 
Positive definite
Positive semi-definite
Negative semi-definite
Negative definite
Indefinite
None
None
matrix must be a numpy.ndarray
alexa@ubuntu-xenial:advanced_linear_algebra$
Repo:

GitHub repository: alu-machine_learning
Directory: math/advanced_linear_algebra
File: 5-definiteness.py
