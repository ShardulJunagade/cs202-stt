# Lab Assignment 9 Report

- Course: CS202 – Software Tools and Techniques for CSE
- Lab Topic: Development of C# Console Applications
- Name: Shardul Junagade
- Roll Number: 23110297
- Date: 13th October 2025

Repository Path: `lab9/`

---

## 1. Introduction, Setup, and Tools

### 1.1 Introduction
This lab introduces C# and .NET through a set of small console applications that exercise basic syntax, control flow, functions, arrays, and object-oriented structure. I implemented separate, focused programs corresponding to each activity, along with reasoning answers for the code snippets in Tasks 5–7.

### 1.2 Environment and Tools
- OS: Windows 11; Terminal: PowerShell 7
- .NET SDK: .NET 8 (compatible with the requirement “.NET 6 or later”)
- Editor/IDE: VS Code / Visual Studio 2022 Community

### 1.3 Project Structure
- `lab9/src/Task1HelloWorld/` — Environment verification and simple I/O
- `lab9/src/Task2Arithmetic/` — OOP arithmetic (+, −, ×, ÷) + even/odd on sum
- `lab9/src/Task3LoopsFunctions/` — for/foreach/do-while + static factorial function
- `lab9/src/Task4ArraysMatrices/` — bubble sort, 2D→1D (row/col major), matrix multiplication
- `lab9/REPORT.md` — this detailed report
- `lab9/README.md` — quick run instructions

All projects target `net8.0` and use the SDK-style `csproj` format. No external packages are required.

---

## 2. Implementation Details

### 2.1 Task 1 — Setup and a Simple Program
- Files: `lab9/src/Task1HelloWorld/Program.cs`
- Summary: Reads a name via `Console.ReadLine()` and prints a greeting to verify .NET and I/O are working.

Run:
- `pwsh`: `dotnet run --project lab9/src/Task1HelloWorld/Task1HelloWorld.csproj`

### 2.2 Task 2 — Basic Syntax and Control Structures
- Files: `lab9/src/Task2Arithmetic/Program.cs`
- OOP: `Calculator` class exposes `Add`, `Subtract`, `Multiply`, `Divide` (throws on divide-by-zero).
- I/O: Reads two numbers, prints results of all four operations, and reports even/odd for their sum using `if-else` logic via `% 2`.

Run:
- `pwsh`: `dotnet run --project lab9/src/Task2Arithmetic/Task2Arithmetic.csproj`

### 2.3 Task 3 — Loops and Functions
- Files: `lab9/src/Task3LoopsFunctions/Program.cs`
- Loops: 
  - `for` prints 1..10 inline.
  - `foreach` prints 1..10 from `Enumerable.Range(1, 10)`.
  - `do-while` accepts input until the user types `exit` (case-insensitive).
- Function: Static `MathUtils.Factorial(int)` returns a `BigInteger` to handle larger inputs and throws on negatives.

Run:
- `pwsh`: `dotnet run --project lab9/src/Task3LoopsFunctions/Task3LoopsFunctions.csproj`

### 2.4 Task 4 — Arrays and Matrices
- Files: `lab9/src/Task4ArraysMatrices/Program.cs`
- Bubble Sort: In-place, no library sorting calls, stable pass shrinking (`n--` per outer pass) until no swaps.
- 2D→1D Flattening:
  - Row-major: iterate rows then cols, append to 1D.
  - Column-major: iterate cols then rows, append to 1D.
- Matrix Multiplication: Validates `A` columns equals `B` rows; triple-nested loops compute `C = A × B` and a printer outputs right-aligned columns.

Run:
- `pwsh`: `dotnet run --project lab9/src/Task4ArraysMatrices/Task4ArraysMatrices.csproj`

---

## 3. Output Reasoning (Tasks 5–7)

### 3.1 Task 5 — Level 0

A) Code:
```
using System; //namespace
class Program //default visibility is 'internal' if not specified
{
    public static void Main(string[] args)
    {
        int a = 0; //default visibility is 'private' (in a class)
        Console.WriteLine(a++);
    }
}
```
Output: `0`
- Reason: Post-increment (`a++`) returns the original value (0), then increments `a` to 1 after evaluation.

B) Code:
```
using System;
class Program
{
    public void Main(string[] args)
    {
        int a = 0;
        Console.WriteLine(a++);
    }
}
```
Output: Compilation error
- Reason: Entry point must be a `static` `Main`. This class defines an instance method `Main`, so the compiler reports: “Program does not contain a static 'Main' method suitable for an entry point.”

### 3.2 Task 6 — Level 1

Code:
```
class Program
{
    public static void Main(string[] args)
    {
        int a = 0;
        int b = a++;
        Console.WriteLine(a++.ToString(),++a,-a++);
        Console.WriteLine((a++).ToString() + (-a++).ToString());
        Console.WriteLine(~b);
    }
}
```
Step-by-step:
- Start: `a = 0`
- `b = a++` → `b = 0`, `a = 1`
- First WriteLine: `a++.ToString()` uses `a` (1), prints format string "1", then `a` becomes 2; `++a` makes `a = 3`; `-a++` passes `-3` then `a = 4`. Because the first argument is treated as a composite format string with no placeholders, extra args are ignored. So it prints: `1`.
- Second WriteLine: now `a = 4`. `(a++).ToString()` → "4", `a = 5`; `(-a++).ToString()` → `-5`, `a = 6`. Concatenation prints: `4-5`.
- Third WriteLine: `~b` with `b = 0` gives `~0 = -1`.

Output:
```
1
4-5
-1
```

### 3.3 Task 6 — Top-level statements

Code:
```
using System;
/*you can also write top level code outside of a class. C# takes
care of this by providing internal entry point Main*/

Console.WriteLine("int x = 3;");
Console.WriteLine("int y = 2 + ++x;");

int x = 3; //default visibility is 'internal' (outside a class)
int y = 2 + ++x;
Console.WriteLine($"x = {x} and y = {y}");

Console.WriteLine("x = 3 << 2;");
Console.WriteLine("y = 10 >> 1;");

x = 3 << 2;
y = 10 >> 1;
Console.WriteLine($"x = {x} and y = {y}");

x = ~x;
y = ~y;
Console.WriteLine($"x = {x} and y = {y}");
```
Output:
```
int x = 3;
int y = 2 + ++x;
x = 4 and y = 6
x = 3 << 2;
y = 10 >> 1;
x = 12 and y = 5
x = -13 and y = -6
```
- Reason: `++x` pre-increments to 4, so `y = 2 + 4 = 6`.
- Shifts: `3 << 2 = 12`, `10 >> 1 = 5`.
- Bitwise complement: `~n = -(n + 1)`, so `~12 = -13`, `~5 = -6`.

### 3.4 Task 7 — Level 2

A) Code:
```
using System;
public class Program
{
    static void Main()
    {
        try
        {
            int i=int.MaxValue;
            Console.WriteLine(-(i+1)-i);
            for(i=0; i<=int.MaxValue;i++); //note semicolon here
            Console.WriteLine("Program ended!");
        }
        catch(Exception ex)
        {
            Console.WriteLine(ex.ToString());
        }
    }
}
```
Output: Prints `1` then the program never reaches "Program ended!" (effectively hangs).
- Reason 1 (overflow arithmetic in unchecked context): `i = int.MaxValue`, `i + 1` wraps to `int.MinValue`. Negating `int.MinValue` in unchecked context yields `int.MinValue` again. So the expression becomes `int.MinValue - int.MaxValue` which wraps to `1`.
- Reason 2 (infinite loop): The semicolon makes an empty loop body. The loop condition is `i <= int.MaxValue`. When `i` overflows past `int.MaxValue`, it wraps to `int.MinValue`, which still satisfies the condition, so the loop never terminates.

B) Code:
```
using System;
public class Program
{
    static void Main(string[] args)
    {
        Main(["CS202"]);
    }
}
```
Output: The process terminates with a `StackOverflowException` (no user output).
- Reason: This is infinite recursion — `Main` calls itself with a new string array (C# 12 collection expression `[...]`) and has no base case. There is no `try/catch`, so the runtime aborts the process when the stack is exhausted.

---

## 4. Notes and Reflections
- Using a `BigInteger` for factorial avoids overflow for moderate inputs and keeps the example robust.
- The first `Console.WriteLine` in Task 6 intentionally demonstrates format-string overload behavior: when the first argument is a plain string without placeholders, additional args are ignored.
- For arrays/matrices, I kept the implementations explicit (no LINQ for core algorithms) to align with the requirement to write the logic ourselves.

---

## 5. How to Run (Short)
See `lab9/README.md` for concise commands. In brief, from the repo root in PowerShell:

```
# Hello World / environment check
dotnet run --project lab9/src/Task1HelloWorld/Task1HelloWorld.csproj

# Arithmetic with even/odd
dotnet run --project lab9/src/Task2Arithmetic/Task2Arithmetic.csproj

# Loops and factorial
dotnet run --project lab9/src/Task3LoopsFunctions/Task3LoopsFunctions.csproj

# Arrays and matrices
dotnet run --project lab9/src/Task4ArraysMatrices/Task4ArraysMatrices.csproj
```

---

## 6. References
- Lab handout: `lab9/TASK.md`
- Microsoft C# docs: https://learn.microsoft.com/en-us/dotnet/csharp
- Arrays: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/arrays
- Access modifiers: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/access-modifiers
- Top-level statements: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements
- Exceptions and overflow: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/exception-handling
- Collection expressions: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/collection-expressions
