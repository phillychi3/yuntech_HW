public class employee1{
    public string ID ;
    public string Name ;
    public string Tel ;
    public string Add ;
    private int empSalary;
    public int Salary
    {
        get {return empSalary;}
        set
        {
            if(value < 23800) empSalary = 23800;
            else empSalary = value;
        }
    }

    public void showinfo(){
        Console.WriteLine("ID:{0}",ID);
        Console.WriteLine("Name:{0}",Name);
        Console.WriteLine("Salary:{0}",Salary);
        Console.WriteLine("Tel:{0}",Tel);
        Console.WriteLine("Add:{0}",Add);
    }

}