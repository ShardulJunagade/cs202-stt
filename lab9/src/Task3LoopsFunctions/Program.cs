using System.Numerics;

namespace Task3LoopsFunctions;

public static class MathUtils
{
    public static BigInteger Factorial(int n)
    {
        if (n < 0) throw new ArgumentException("Factorial is not defined for negative numbers.");
        BigInteger result = 1;
        for (int i = 2; i <= n; i++) result *= i;
        return result;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Task 3: Loops and Functions\n");

        Console.WriteLine("for loop 1..10:");
        for (int i = 1; i <= 10; i++) Console.Write(i + (i < 10 ? ", " : "\n"));

        Console.WriteLine("\nforeach loop 1..10:");
        int[] numbers = Enumerable.Range(1, 10).ToArray();
        foreach (int n in numbers) Console.Write(n + (n < 10 ? ", " : "\n"));

        Console.WriteLine("\ndo-while: type commands; type 'exit' (case-insensitive) to quit.");
        string? input;
        do {
            Console.Write("Enter something: ");
            input = Console.ReadLine();
            if (input == null) break;
            if (!input.Equals("exit", StringComparison.OrdinalIgnoreCase))
                Console.WriteLine($"You typed: {input}");
        } while (!input.Trim().Equals("exit", StringComparison.OrdinalIgnoreCase));
        Console.WriteLine("Exited input loop.");

        Console.WriteLine("\nType a number to get its factorial, or 'exit' to quit.");
        // string? input;
        do
        {
            Console.Write("Input: ");
            input = Console.ReadLine();
            if (input is null) continue;
            if (input.Trim().Equals("exit", StringComparison.OrdinalIgnoreCase)) break;
            if (int.TryParse(input, out int n))
            {
                try
                {
                    Console.WriteLine($"{n}! = {MathUtils.Factorial(n)}");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error: {ex.Message}");
                }
            }
            else
            {
                Console.WriteLine("Please enter a valid integer or 'exit'.");
            }
        } while (true);

        Console.WriteLine("Exited input loop.");
    }
}
