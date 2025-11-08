# Lab 9 – C# Console Applications

This folder contains four standalone C# console projects implementing all required lab activities plus a detailed `REPORT.md` with reasoning for Tasks 5–7.

## Projects
- `Task1HelloWorld` – Basic environment + greeting input
- `Task2Arithmetic` – OOP arithmetic operations + even/odd check
- `Task3LoopsFunctions` – for, foreach, do-while loops + static factorial
- `Task4ArraysMatrices` – bubble sort, flatten 2D row/col major, matrix multiplication

Target framework: `net8.0` (meets “.NET 6 or later”).

## Prerequisites
Install the .NET SDK (https://dotnet.microsoft.com/download). Confirm with:
```pwsh
dotnet --version
```

## Run Commands (PowerShell)
From repository root:
```pwsh
# 1. Hello World
dotnet run --project lab9/src/Task1HelloWorld/Task1HelloWorld.csproj

# 2. Arithmetic
dotnet run --project lab9/src/Task2Arithmetic/Task2Arithmetic.csproj

# 3. Loops & Factorial
dotnet run --project lab9/src/Task3LoopsFunctions/Task3LoopsFunctions.csproj

# 4. Arrays & Matrices
dotnet run --project lab9/src/Task4ArraysMatrices/Task4ArraysMatrices.csproj
```

## Sample Interactions
Arithmetic (division by zero handled):
```
Enter first number: 10
Enter second number: 0
Addition: 10
Subtraction: 10
Multiplication: 0
Division Error: Cannot divide by zero.
Sum 10 is Even
```

Factorial loop (exit command):
```
Input: 5
5! = 120
Input: exit
Exited input loop.
```

Bubble sort example:
```
Enter integers for bubble sort (space-separated):
> 5 2 9 1
Sorted: 1 2 5 9
```

Flattening demo:
```
Row-major:   1 2 3 4 5 6
Column-major:1 4 2 5 3 6
```

Matrix multiplication output (A 2x3 * B 3x2):
```
A x B = 
     58    64
    139   154
```

## Reasoning Answers
Detailed reasoning for Tasks 5–7 is in `lab9/REPORT.md` (section 3). It explains post-increment behavior, static `Main` requirements, format string handling, operator precedence, bitwise complement, overflow effects, empty loop due to trailing semicolon, and infinite recursion stack overflow.

## Notes
- No external dependencies; projects compile with default SDK.
- Factorial uses `BigInteger` to avoid overflow on modest inputs.
- Bubble sort is implemented manually per lab requirement.

## Reference
See `lab9/TASK.md` for original lab instructions and `lab9/REPORT.md` for full explanations.
