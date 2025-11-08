using System;

namespace Task2Arithmetic;

public class Calculator
{
    public double Add(double a, double b) => a + b;
    public double Subtract(double a, double b) => a - b;
    public double Multiply(double a, double b) => a * b;
    public double Divide(double a, double b)
    {
        if (b == 0) throw new DivideByZeroException("Cannot divide by zero.");
        return a / b;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Task 2: Arithmetic Operations and Even/Odd Check");
        double first = ReadNumber("Enter first number: ");
        double second = ReadNumber("Enter second number: ");
        var calc = new Calculator();

        Console.WriteLine($"Addition: {calc.Add(first, second)}");
        Console.WriteLine($"Subtraction: {calc.Subtract(first, second)}");
        Console.WriteLine($"Multiplication: {calc.Multiply(first, second)}");
        try
        {
            Console.WriteLine($"Division: {calc.Divide(first, second)}");
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine($"Division Error: {ex.Message}");
        }

        double sum = calc.Add(first, second);
        Console.WriteLine(sum % 2 == 0 ? $"Sum {sum} is Even" : $"Sum {sum} is Odd");
    }

    private static double ReadNumber(string prompt)
    {
        while (true)
        {
            Console.Write(prompt);
            string? input = Console.ReadLine();
            if (double.TryParse(input, out double value)) return value;
            Console.WriteLine("Invalid number, please try again.");
        }
    }
}
