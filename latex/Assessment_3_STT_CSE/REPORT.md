# Lab Assignment 9 Report

- Course: CS202 – Software Tools and Techniques for CSE
- Lab Topic: Development of C# Console Applications
- Name: Shardul Junagade (23110297)
- Date: 13th October 2025

Repository path: `lab9/`

---

## Introduction

This lab was a gentle, hands-on tour of C# and .NET using small console programs. I split the work into four focused projects to keep each idea clear: a quick environment check, arithmetic with a simple class, a few loop patterns plus a factorial function, and a set of array/matrix tasks. I also reasoned through the output of the snippets in Tasks 5–7 so the “why” behind each output was explicit.

---

## Tools

- OS: Windows 11; Shell: PowerShell 7
- .NET SDK: .NET 8 (meets the “.NET 6 or later” requirement)
- IDE/Editor: Visual Studio 2022 Community and/or VS Code
- Git: for version control (optional but handy)

Project layout used in this lab:
- `lab9/src/Task1HelloWorld/`
- `lab9/src/Task2Arithmetic/`
- `lab9/src/Task3LoopsFunctions/`
- `lab9/src/Task4ArraysMatrices/`

All projects are SDK-style and have no external package dependencies.

![Environment Details](./images/env.png)
![Project Structure](./images/proj.png)

---

## Setup

I set up a fresh .NET environment on Windows and validated it with a tiny console app before working on the lab projects.

Visual Studio path (recommended by the lab):
1) Install Visual Studio 2022 (Community Edition) with the “.NET desktop development” workload selected.
![Workload Selection](./images/workload.png)

2) Confirm the SDK is on PATH:
   ```pwsh
   dotnet --version
   ```
3) Create a new C# Console App in Visual Studio and set the Target Framework to .NET 8.0 in project properties.
![New Project Wizard](./images/1.png)

![Project Target Framework](./images/2.png)

![.NET Version Selection](./images/4.png)

CLI alternative (works well from VS Code):
```pwsh
# Create and run a throwaway test app
dotnet new console -f net8.0 -o sandbox-console
dotnet run --project sandbox-console/sandbox-console.csproj
```


---

## Methodology and Results (Combined)

### Task 1 – Environment check and basic I/O
Code intent: confirm console I/O and runtime. Reads a name via `Console.ReadLine()` and prints a greeting.
Path: `lab9/src/Task1HelloWorld/Program.cs`
Run:
```pwsh
dotnet run --project lab9/src/Task1HelloWorld/Task1HelloWorld.csproj
```
Result: Prompts for a name and echoes a greeting; verifies SDK and terminal interaction.

![Task1 code snippet](./images/5.png)

![Task1 console output](./images/6.png)

### Task 2 – Arithmetic + even/odd
Design: Small `Calculator` class with explicit methods (`Add`, `Subtract`, `Multiply`, `Divide`). Division guarded against zero with an exception caught at call site.
Path: `lab9/src/Task2Arithmetic/Program.cs`
Run:
```pwsh
dotnet run --project lab9/src/Task2Arithmetic/Task2Arithmetic.csproj
```
Result: Prints four operation results and states whether the sum is even or odd. Division by zero produces a clear message.

![Task2 code (Calculator class)](./images/7.png)

![Task2 sample output](./images/8.png)

### Task 3 – Loops and factorial
Design: Demonstrates `for`, `foreach`, and a `do-while` loop. Factorial provided by `MathUtils.Factorial(int)` returning `BigInteger` to avoid premature overflow.
Path: `lab9/src/Task3LoopsFunctions/Program.cs`
Run:
```pwsh
dotnet run --project lab9/src/Task3LoopsFunctions/Task3LoopsFunctions.csproj
```
Result: Two sequences 1..10 printed; interactive loop ends cleanly on `exit`; factorial results shown for valid integers, error for negatives.

![Task3 code snippet](./images/9.1.png)

![Task3 code snippet](./images/9.2.png)

![Task3 interactive session output](./images/10.png)

### Task 4 – Arrays and matrices
Design: Manual bubble sort with shrinking pass; row-major and column-major flattening; matrix multiply with dimension check and aligned printer.
Path: `lab9/src/Task4ArraysMatrices/Program.cs`
Run:
```pwsh
dotnet run --project lab9/src/Task4ArraysMatrices/Task4ArraysMatrices.csproj
```
Result: Sorted list echoed back; flattening shows differing orders; multiplication prints a 2x2 matrix from 2x3 and 3x2 inputs.

![Task4 Array Algorithms snippet](./images/11.1.png)

![Task4 Matrix Algorithms snippet](./images/11.2.png)

![Task4 Program snippet](./images/11.3.png)

![Task4 interactive session output](./images/12.png)

### Aggregate Run Commands
```pwsh
dotnet run --project lab9/src/Task1HelloWorld/Task1HelloWorld.csproj
dotnet run --project lab9/src/Task2Arithmetic/Task2Arithmetic.csproj
dotnet run --project lab9/src/Task3LoopsFunctions/Task3LoopsFunctions.csproj
dotnet run --project lab9/src/Task4ArraysMatrices/Task4ArraysMatrices.csproj
```

### Output Reasoning (Tasks 5–7)

Below, I separated each snippet as it appeared in the handout and wrote what I observed, why it happened, and the exact output. I also added image placeholders for the code and the console output I captured.

#### Task 5 — Level 0 (Code A)
Explanation: I ran the program containing a single post-increment expression inside `Console.WriteLine`. The post-increment operator returned the current value of `a` before performing the increment, so the console displayed `0`. Immediately after evaluation, `a` became `1`, but that new value was not part of the printed output. This confirmed the standard right-to-left evaluation of the post-increment without any hidden side effects.

Output I observed:
```text
0
```

![L0A – code](./images/13.png)
![L0A – output](./images/14.png)

#### Task 5 — Level 0 (Code B)
Explanation: I attempted to build the second variant where `Main` was defined as an instance method (`public void Main`). The C# compiler emitted error CS5001 because the runtime entry point must be a static method with a valid signature (e.g., `static void Main(string[] args)`). Since that requirement was not met, the assembly did not produce any executable output and the program never started.

Compiler behavior I observed:
```text
error CS5001: Program does not contain a static 'Main' method suitable for an entry point
```

![L0B – build error](./images/15.png)

#### Task 6 — Level 1 (Code A)
Explanation: I evaluated the sequence of increments carefully. First `b = a++` captured `0` then advanced `a` to `1`. In `Console.WriteLine(a++.ToString(), ++a, -a++)`, the first argument became the format string "1" (after `a++` advanced `a` to `2`), so the remaining evaluated arguments (`++a` making `a = 3`, and `-a++` yielding `-3` then `a = 4`) were ignored for printing but still executed. The second line concatenated the string versions of `4` and `-5` (with `a` moving from `4` to `6`), yielding `4-5`. Finally, `~b` computed the bitwise complement of `0`, producing `-1`.

Output I observed:
```text
1
4-5
-1
```

![L1A – code](./images/16.png)
![L1A – output](./images/17.png)

#### Task 6 — Level 1 (Code B: Top-level statements)
Explanation: I used top-level statements so the compiler generated an implicit `Main`. The pre-increment `++x` raised `x` from `3` to `4` before the addition, making `y = 2 + 4 = 6`. Left shift `3 << 2` multiplied the value by 4 yielding `12`; right shift `10 >> 1` divided by 2 yielding `5`. The bitwise complement operator applied two’s-complement inversion, so `~12` became `-13` and `~5` became `-6`.

Output I observed:
```text
int x = 3;
int y = 2 + ++x;
x = 4 and y = 6
x = 3 << 2;
y = 10 >> 1;
x = 12 and y = 5
x = -13 and y = -6
```

![L1B – code](./images/18.png)
![L1B – output](./images/19.png)

#### Task 7 — Level 2 (Code A)
Explanation: I initialized `i` to `int.MaxValue` and evaluated `-(i+1)-i` under the default unchecked arithmetic. The expression `i + 1` overflowed to `int.MinValue`; negating `int.MinValue` left it unchanged due to range asymmetry, and subtracting `i` yielded the wrapped result `1`. The `for` loop’s trailing semicolon created an empty loop body that repeatedly overflowed `i` and never allowed execution to reach the `"Program ended!"` line.

Output I observed:
```text
1
```
(The program did not print "Program ended!" and did not terminate in a reasonable time.)

![L2A – code](./images/20.png)
![L2A – output](./images/21.png)

#### Task 7 — Level 2 (Code B)
Explanation: I ran the recursive program where `Main(["CS202"])` invoked itself without a termination condition. Each invocation consumed another stack frame until the process exhausted stack space. The console printed a long stack trace repeating the same frame many times, which is why it appeared to run for a while; after dumping the trace, the runtime terminated the process due to a stack overflow.

Behavior I observed:
```text
...
...
...
at Program.Main(System.String[])
at Program.Main(System.String[])
at Program.Main(System.String[])
at Program.Main(System.String[])
at Program.Main(System.String[])
...
C:\Users\shardul\source\repos\stt-lab9\stt-lab9\bin\Debug\net8.0\stt-lab9.exe (process 24320) exited with code -1073744151
```

![L2B – code](./images/22.png)
![L2B – runtime termination](./images/23.png)

---

## Conclusion

In this lab I implemented four focused C# console projects and verified core language features: input/output, arithmetic with simple classes, looping constructs, factorial computation, and array/matrix algorithms including bubble sort and multiplication. I also analyzed seven reasoning snippets, confirming operator semantics, overflow behavior, format string handling, and recursion limits. The work strengthened my practical understanding of evaluation order and memory effects while keeping the implementations minimal and explicit.

---

## References
- Lab handout: `lab9/TASK.md`
- Microsoft C# docs: https://learn.microsoft.com/en-us/dotnet/csharp
- Arrays: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/arrays
- Access modifiers: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/access-modifiers
- Top-level statements: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements
- Exceptions and overflow: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/exception-handling
- Collection expressions: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/collection-expressions
