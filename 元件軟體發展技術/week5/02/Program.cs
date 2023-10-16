
var list = new List<int> { 11111, 22, 34, 45, 23425 };
System.Console.WriteLine("before");
foreach (var item in list)
{
    Console.WriteLine(item + " ");
}

list.Sort();
System.Console.WriteLine("===================================after");

foreach (var item in list)
{
    Console.WriteLine(item + " ");
}