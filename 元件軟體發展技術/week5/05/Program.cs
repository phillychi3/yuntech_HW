int[] array01 = new int[] {10, 20, 30, 40, 50,60};
int[] array02 = new int[] {0,1,2,3,4,5,6,7,8,9,10};
Array.Copy(array01, 2, array02, 5, 3);
System.Console.WriteLine("來源陣列           目的陣列");
var space = "               ";
for (int i = 0; i < 11; i++)
{
    try
    {
        System.Console.WriteLine($"{array01[i]}{space}{array02[i]}");
    }
    catch (System.Exception)
    {
        System.Console.WriteLine($"{space}{array02[i]}");
    }

}