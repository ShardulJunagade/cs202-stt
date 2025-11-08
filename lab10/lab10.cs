using System;

namespace Lab10
{
    class Program
    {
        private int data;
        private static int liveCount =0;

        public Program()
        {
            liveCount++;
            Console.WriteLine("Constructor Called");
            Console.WriteLine($"Active objects: {liveCount}");
        }

        ~Program()
        {
            liveCount--;
            Console.WriteLine("Object Destroyed");
            Console.WriteLine($"Active objects: {liveCount}");
        }

        public void set_data(int x)
        {
            data = x;
        }

        public void show_data()
        {
            Console.WriteLine($"data = {data}");
        }

        static void Main(string[] args)
        {
            Console.WriteLine("-- Constructors, Data Control and Destructors Demo --");

            // Create and use Program objects inside a separate method so locals go out of scope
            CreateAndUseProgramObjects();

            // Force garbage collection now that the local variables in CreateAndUseProgramObjects are out of scope
            GC.Collect();
            GC.WaitForPendingFinalizers();

            Console.WriteLine();
            Console.WriteLine("-- Inheritance and Polymorphism Demo --");

            // Create one object of each class and store in Vehicle[]
            Vehicle[] vehicles = new Vehicle[3];
            vehicles[0] = new Vehicle(50,100);
            vehicles[1] = new Car(80,60,4);
            vehicles[2] = new Truck(40,200,1500);

            // Loop through the array and call Drive() and ShowInfo()
            foreach (var veh in vehicles)
            {
                veh.Drive();
                veh.ShowInfo();
                Console.WriteLine();
            }

            Console.WriteLine("Program finished. Press Enter to exit.");
            Console.ReadLine();
        }

        // Separated method to ensure local variables go out of scope when the method returns
        static void CreateAndUseProgramObjects()
        {
            // Dynamically create three Program objects
            Program p1 = new Program();
            Program p2 = new Program();
            Program p3 = new Program();

            // Assign values
            p1.set_data(10);
            p2.set_data(20);
            p3.set_data(30);

            // Display values in sequential order
            p1.show_data();
            p2.show_data();
            p3.show_data();

            // When this method returns, p1/p2/p3 go out of scope and can be collected
        }
    }

    // Base class Vehicle
    public class Vehicle
    {
        protected int speed;
        protected int fuel;

        public Vehicle(int speed =0, int fuel =0)
        {
            this.speed = speed;
            this.fuel = fuel;
        }

        public virtual void ShowInfo()
        {
            Console.WriteLine($"Vehicle Info - Speed: {speed}, Fuel: {fuel}");
        }

        public virtual void Drive()
        {
            fuel -=5;
            Console.WriteLine("Vehicle is moving...");
        }
    }

    // Derived class Car
    public class Car : Vehicle
    {
        public int passengers;

        public Car(int speed =0, int fuel =0, int passengers =0) : base(speed, fuel)
        {
            this.passengers = passengers;
        }

        public override void Drive()
        {
            fuel -=10;
            Console.WriteLine("Car is moving with passenger");
        }

        public override void ShowInfo()
        {
            Console.WriteLine($"Car Info - Speed: {speed}, Fuel: {fuel}, Passengers: {passengers}");
        }
    }

    // Derived class Truck
    public class Truck : Vehicle
    {
        public int cargoWeight;

        public Truck(int speed =0, int fuel =0, int cargoWeight =0) : base(speed, fuel)
        {
            this.cargoWeight = cargoWeight;
        }

        public override void Drive()
        {
            fuel -=15;
            Console.WriteLine("Truck is moving with cargo");
        }

        public override void ShowInfo()
        {
            Console.WriteLine($"Truck Info - Speed: {speed}, Fuel: {fuel}, CargoWeight: {cargoWeight}");
        }
    }
}
