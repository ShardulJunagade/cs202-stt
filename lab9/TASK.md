# Lab Assignment 9

**Course:** CS202 Software Tools and Techniques for CSE  
**Lab Topic:** Development of C# Console Applications  
**Date:** 13th October 2025

## Objective

This lab introduces students to .NET development using C# in Visual Studio. The focus is on creating simple console applications to understand basic syntax, control structures, and object-oriented programming principles in C#.

## Learning Outcomes

By the end of this lab, students will be able to:
- Set up and use Visual Studio for .NET development.
- Write and execute basic C# console applications.
- Implement fundamental programming constructs: loops, conditionals, and functions.
- Apply object-oriented programming concepts in C#.

## Lab Requirements

- Operating System: **Windows**
- Software: Visual Studio 2022 (Community Edition), Visual Studio with .NET SDK
- Programming Language: C# (latest stable version)

## Lab Activities:

### 1. Setting Up .NET Development Environment.
- Open Visual Studio and create a new **C# Console Application** project.
- Ensure the target framework is .NET 6 or later.
- Write a simple program (any) and run it.

### 2. Understanding Basic Syntax and Control Structures
- Write an object-oriented C# program that:
  - Accepts user input¹ for two numbers.
  - Performs addition, subtraction, multiplication, and division.
  - Uses **if-else** conditions to determine if the sum is even or odd.
  - Displays the results using **Console.WriteLine()**.

### 3. Using Loops and Functions
- Design an object-oriented C# program that:
  - Uses a **for** loop to print numbers from 1 to 10.
  - Uses a **foreach** loop to print numbers from 1 to 10.
  - Uses a **do-while** loop to keep asking the user for input until they enter **exit**.
  - Defines and calls a function² that calculates the factorial of a number provided by the user.

---

¹ Use Visual Studio IDE suggestions to identify the method that should be called to achieve this.  
² You should make this function **static** if your logic if outside the Main() method AND you do not plan to create any objects on which to call this function.

---

### 4. Using Single and Multi-dimensional Arrays
- Design an object-oriented C# program that:
  - Implements the bubble sort algorithm on array³ of integers. You should not use any library functions to achieve this task. The entire logic must be present in your C# code.
  - Stores a 2-D array into one 1-D array in: (i) row major order, (ii) column major order.
  - Performs matrix multiplication of two matrices A and B and stores the resultant in matrix C and print it.

### 5. Output Reasoning (Level 0)
- **What will be the output of the following C# code? Why?**

    ```
    using System; //namespace
    class Program //default visibility⁴ is 'internal' if not specified
    {
        public static void Main(string[] args)
        {
            int a = 0; //default visibility is 'private' (in a class)
            Console.WriteLine(a++);
        }
    }
    ```

- **What will be the output of the following C# code? Why?**

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

### 6. Output Reasoning (Level 1)
- **What will be the output of the following C# code? Why?**

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

---

³ https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/arrays  
⁴ https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/access-modifiers

---

- **What will be the output of the following C# code⁵? Why?**

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

### 7. Output Reasoning (Level 2)
- **What will be the output of the following C# code⁶? Why?**

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

- **What will be the output of the following C# code⁷? Why?**
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

---

⁵ https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements  
⁶ https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/exception-handling  
⁷ https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/collection-expressions

---



## Resources

- Lecture 9 Slides
- https://learn.microsoft.com/en-us/dotnet/csharp