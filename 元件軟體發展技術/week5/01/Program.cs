Console.WriteLine("=== 由鍵盤輸入連續整數直到myary");

var ary = new int [5];
for(int i=0;i<5;i++){
    Console.Write("請輸入第"+(i+1)+$"個元素: ary=[{i}]");
    ary[i] = int.Parse(Console.ReadLine());

}
Console.WriteLine("陣列的元素內容");
foreach (var items in ary)
{
    Console.Write(items+" ");
}
System.Console.WriteLine("ary的總和: "+ary.Sum());
Console.Read();