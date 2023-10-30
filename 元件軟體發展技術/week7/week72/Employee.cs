
using System.Dynamic;

public class Wow
{
    private int SalaryP;
    public string ID ;
    public string Name ;

    public int testsalary
    {
        get {return SalaryP;}
        set
        {
            if(value < 23800)
            {
                SalaryP = 23800;
            }
            else
            {
                SalaryP = value;
            }
        }
    }

    public void showinfo(){
        Console.WriteLine("ID:{0}",ID);
        Console.WriteLine("Name:{0}",Name);
        Console.WriteLine("Salary:{0}",testsalary);
    }
}