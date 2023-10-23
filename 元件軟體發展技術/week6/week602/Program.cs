

double Computer(int llong)
{
    return 4 * Math.PI * Math.Pow(llong, 3)/3;
}

int longball;
System.Console.WriteLine("請輸入球體半徑:");
longball = int.Parse(System.Console.ReadLine());
System.Console.WriteLine($"球體半徑= {longball}");
System.Console.WriteLine($"球體體積= {Computer(longball)}");
