namespace Task1HelloWorld;

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Task 1: .NET environment verification.");
        Console.WriteLine("Enter your name: ");
        string? name = Console.ReadLine();
        Console.WriteLine($"Hello, {name ?? "Anonymous"}! .NET is set up correctly.");
    }
}
