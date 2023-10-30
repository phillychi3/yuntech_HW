



using System.Diagnostics.Contracts;
namespace rfjweihjtif4wei;

public class Rectangle
{
    protected static int num=0;
    public int Width=0;
    public int Height=0;



    public Rectangle()
    {
        num++;
    }

    public int getArea()
    {
        return Width * Height;
    }
    public static void ShowNum()
    {
        Console.WriteLine("num={0}",num);
    }
}



public class Triangle : Rectangle
{
    public void Showdata()
    {
        System.Console.WriteLine("Width={0}",Width);
        System.Console.WriteLine("Height={0}",Height);
    }

    public new int getArea()
    {
        return Width * Height / 2;
    }
}

public static class Program
{
    public static void Main()
    {
        Rectangle test1 = new Rectangle();
        test1.Width=10;
        test1.Height=5;
        Triangle test2 = new Triangle();
        test2.Width=10;
        test2.Height=5;
        Console.WriteLine(test1.getArea());
        Console.WriteLine(test2.getArea());
        

        Rectangle.ShowNum();
    }


}


