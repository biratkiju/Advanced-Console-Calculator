# Advanced Console Calculator

A menu-driven Python console project based on the supplied **Advanced Console Calculator** assignment.

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Run

Open a terminal in this folder and run:

```bash
python advanced_calculator.py
```

On Windows, this also works:

```powershell
py advanced_calculator.py
```

## Features

1. Basic arithmetic: addition, subtraction, multiplication, division, power and square root
2. Trigonometry: sin, cos, tan, inverse trig, sec, cosec, cot, sinh, cosh and tanh
3. Exponential and logarithmic functions
4. Factorial, permutations and combinations
5. Numerical first derivative
6. Numerical second derivative
7. Definite integration using Simpson's rule
8. Unit conversions
9. Quadratic equation solver (real and complex roots)
10. Fibonacci, prime test, GCD and LCM
11. Mean, median, population variance and standard deviation
12. Polynomial derivative from coefficients
13. Newton-Raphson root finding
14. Bisection root finding
15. Calculation history
16. Secant root finding
17. Partial derivatives for f(x, y)
18. Cosine Taylor-series comparison
19. Trapezoid versus Simpson integration comparison
20. 2x2 matrix addition, multiplication, determinant and inverse

The project demonstrates `if/elif/else`, `while`, `for`, `lambda`, `def`, parameters, return values, and `try/except`.

## Entering mathematical expressions

For derivative, integration and root-finding features, enter expressions such as:

- `x**2 + 3*x + 2`
- `sin(x)`
- `exp(-x**2)`
- `x**3 - x - 2`

For partial derivatives, use two variables:

- `x**2 + x*y + y**2`

Use `**` for powers. The expression parser also converts `^` to `**`.

Supported functions include `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sinh`, `cosh`, `tanh`, `exp`, `log`, `log10`, `sqrt`, `fabs`, `floor` and `ceil`. Constants `pi` and `e` are available.

## History

When you select Exit, this session's history is appended to `history.txt` in the project folder. The history option displays saved entries and current-session entries.

## Important notes

- Trigonometric menu inputs are in degrees. Inverse trigonometric inputs are ratios.
- The numerical derivative and integration features are approximations.
- Simpson's rule automatically adjusts an odd number of strips to the next even number.
- Statistics calculates population variance (dividing by the number of values).
- User expressions are evaluated with a restricted AST parser; arbitrary Python statements and built-ins are not accepted.

## Suggested project structure

```text
Advanced_Console_Calculator/
├── advanced_calculator.py
├── README.md
├── requirements.txt
├── .gitignore
└── history.txt       # created when calculations are saved on exit
```

## Suggested viva topics

1. Difference between `lambda` and `def`
2. Difference between `for` and `while`
3. Why degrees are converted to radians for Python's `math` trigonometric functions
4. Why central difference is used for numerical derivatives
5. Why Simpson's rule requires an even number of strips
6. What happens if Newton-Raphson reaches a point where the derivative is zero
7. Difference between permutation and combination
