System.Console.WriteLine("請輸入要顯示到第幾個的斐波那契數列:");

System.Console.WriteLine("== 輸出:");

int reme(int input)
{
    if(input == 1 || input == 2)
    {
        return 1;
    }
    else
    {
        return reme(input - 1) + reme(input - 2);
    }

}


int input = int.Parse(System.Console.ReadLine());

for(int i = 1; i <= input; i++)
{
    System.Console.Write($"{reme(i)} ");
}