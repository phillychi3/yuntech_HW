

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Hello, World!");
            System.Console.WriteLine(GetMax(5, 7));
            System.Console.WriteLine(GetMax(20, -53, 9));
            System.Console.WriteLine(GetMax(new[] { 34, -66, 19, 48, 1 }));



        }
        static int GetMax(int num1, int num2)
        {
            if (num1 > num2)
            {
                return num1;
            }
            else
            {
                return num2;
            }
        }


        static int GetMax(int num1, int num2, int num3)
        {
            int[] test = { num1, num2, num3 };
            return test.Max();
        }

        static int GetMax(int[] numlist)
        {
            return numlist.Max();
        }
    }
}