using System.ComponentModel.DataAnnotations;

List<int> f1 = new List<int>();
List<int> f2 = new List<int>();
List<int> f3 = new List<int>();


for (int i = 0; i < 3; i++)
{
    System.Console.WriteLine($"第 {i+1} 林各候選人得票數");
    System.Console.Write("1. wow");
    f1.Add(int.Parse(Console.ReadLine()));
    System.Console.Write("2. 030");
    f2.Add(int.Parse(Console.ReadLine()));
    System.Console.Write("3. .w.");
    f3.Add(int.Parse(Console.ReadLine()));
    System.Console.WriteLine("===================================");
}
System.Console.WriteLine("===================================");
System.Console.WriteLine("候選人  第一林   第二林   第三林  得票數");
System.Console.WriteLine("===================================");
System.Console.WriteLine($"wow      {f1[0]}       {f1[1]}       {f1[2]}       {f1.Sum()}");
System.Console.WriteLine($"030      {f2[0]}       {f2[1]}       {f2[2]}       {f2.Sum()}");
System.Console.WriteLine($".w.      {f3[0]}       {f3[1]}       {f3[2]}       {f3.Sum()}");

var maxxxxx = new List<int> {f1.Sum(), f2.Sum(), f3.Sum()}.Max();

if (maxxxxx == f1.Sum())
{
    System.Console.WriteLine($"wow 當選 綜計: {maxxxxx}");
}
else if (maxxxxx == f2.Sum())
{
    System.Console.WriteLine($"030 當選 綜計: {maxxxxx}");
}
else
{
    System.Console.WriteLine($".w. 當選 綜計: {maxxxxx}");
}