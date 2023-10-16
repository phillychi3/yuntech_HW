var worldslsit = new List<string> {"coconut", "tomato", "mango", "lime", "wow", "apple", "banana", "conan"};
worldslsit.Sort();

for (int i = 0; i < 8; i++)
{
    System.Console.WriteLine($"{i+1}.word[{i}] = {worldslsit[i]}");
}

System.Console.WriteLine("===================================");
System.Console.WriteLine("請輸入要查詢的字串");
var input = Console.ReadLine();
int index = worldslsit.IndexOf(input);
System.Console.WriteLine("===================================");
System.Console.WriteLine("result: ");

if(index==-1){
    System.Console.WriteLine("查無此字串");
}else{
    System.Console.WriteLine($"該資料位於 word[{index}] = {worldslsit[index]}");
}
