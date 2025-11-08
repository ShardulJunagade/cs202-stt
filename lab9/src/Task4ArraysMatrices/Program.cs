namespace Task4ArraysMatrices;

public static class ArrayAlgorithms
{
    public static void BubbleSort(int[] arr)
    {
        if (arr == null || arr.Length <= 1) return;
        bool swapped;
        int n = arr.Length;
        do
        {
            swapped = false;
            for (int i = 1; i < n; i++)
            {
                if (arr[i - 1] > arr[i])
                {
                    int tmp = arr[i - 1];
                    arr[i - 1] = arr[i];
                    arr[i] = tmp;
                    swapped = true;
                }
            }
            n--; // last element after each pass is at correct position
        } while (swapped);
    }

    public static int[] FlattenRowMajor(int[,] matrix)
    {
        int rows = matrix.GetLength(0);
        int cols = matrix.GetLength(1);
        int[] result = new int[rows * cols];
        int k = 0;
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                result[k++] = matrix[i, j];
        return result;
    }

    public static int[] FlattenColMajor(int[,] matrix)
    {
        int rows = matrix.GetLength(0);
        int cols = matrix.GetLength(1);
        int[] result = new int[rows * cols];
        int k = 0;
        for (int j = 0; j < cols; j++)
            for (int i = 0; i < rows; i++)
                result[k++] = matrix[i, j];
        return result;
    }
}

public static class MatrixAlgorithms
{
    public static int[,] Multiply(int[,] A, int[,] B)
    {
        int rA = A.GetLength(0), cA = A.GetLength(1);
        int rB = B.GetLength(0), cB = B.GetLength(1);
        if (cA != rB) throw new ArgumentException("Incompatible dimensions for multiplication.");
        int[,] C = new int[rA, cB];
        for (int i = 0; i < rA; i++)
            for (int j = 0; j < cB; j++)
            {
                int sum = 0;
                for (int k = 0; k < cA; k++)
                    sum += A[i, k] * B[k, j];
                C[i, j] = sum;
            }
        return C;
    }

    public static void Print(int[,] M)
    {
        int rows = M.GetLength(0), cols = M.GetLength(1);
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                Console.Write(M[i, j].ToString().PadLeft(6));
            }
            Console.WriteLine();
        }
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Task 4: Arrays and Matrices\n");

        // Bubble Sort
        Console.WriteLine("Enter integers for bubble sort (space-separated):");
        int[] arr = ReadIntArray();
        ArrayAlgorithms.BubbleSort(arr);
        Console.WriteLine("Sorted: " + string.Join(" ", arr));

        // 2D -> 1D (Row-major / Column-major)
        Console.WriteLine("\nDemo 2D flattening using sample matrix [[1,2,3],[4,5,6]]:");
        int[,] sample = new int[,] { { 1, 2, 3 }, { 4, 5, 6 } };
        Console.WriteLine("Sample Matrix:");
        MatrixAlgorithms.Print(sample);
        int[] rowMajor = ArrayAlgorithms.FlattenRowMajor(sample);
        int[] colMajor = ArrayAlgorithms.FlattenColMajor(sample);
        Console.WriteLine("Row-major:    " + string.Join(" ", rowMajor));
        Console.WriteLine("Column-major: " + string.Join(" ", colMajor));

        // Matrix Multiplication
        Console.WriteLine("\nMatrix Multiplication Demo (using small sample matrices)");
        int[,] A = new int[,] { { 1, 2, 3 }, { 4, 5, 6 } }; // 2x3
        int[,] B = new int[,] { { 7, 8 }, { 9, 10 }, { 11, 12 } }; // 3x2
        int[,] C = MatrixAlgorithms.Multiply(A, B); // 2x2
        Console.WriteLine("Matrix A:");
        MatrixAlgorithms.Print(A);
        Console.WriteLine("Matrix B:");
        MatrixAlgorithms.Print(B);
        Console.WriteLine("A x B = ");
        MatrixAlgorithms.Print(C);
    }

    private static int[] ReadIntArray()
    {
        while (true)
        {
            Console.Write("> ");
            string? line = Console.ReadLine();
            if (string.IsNullOrWhiteSpace(line))
            {
                Console.WriteLine("Please enter at least one integer.");
                continue;
            }
            string[] parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
            int[] arr = new int[parts.Length];
            bool ok = true;
            for (int i = 0; i < parts.Length; i++)
            {
                if (!int.TryParse(parts[i], out arr[i]))
                {
                    Console.WriteLine($"'{parts[i]}' is not an integer. Try again.");
                    ok = false; break;
                }
            }
            if (ok) return arr;
        }
    }
}
