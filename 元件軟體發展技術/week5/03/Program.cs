var list = new[] {22,33,50,99,11};
var name = new[] {"John", "Mary", "Bob", "Anna", "Peter"};

System.Console.WriteLine("before");
for (int i = 0; i < 5; i++)
{
    System.Console.WriteLine($"name[{i}]={name[i]} list[{i}]={list[i]}");
}

Array.Sort(list, name);
Array.Reverse(list);
Array.Reverse(name);
System.Console.WriteLine("==================after=================");
System.Console.WriteLine("      name      成績     名次");

for (int i = 0; i < 5; i++)
{
    System.Console.WriteLine($"name[{i}] = {name[i]} list[{i}] = {list[i]}     {i+1}");
}