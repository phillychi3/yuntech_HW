using static Wow;

public class Program
{
    public static void Main()
    {
        Wow employee1 = new Wow();
        employee1.ID = "A0023";
        employee1.Name = "林婉兒";
        employee1.Salary = 37000;

        Wow employee2 = new Wow();
        employee2.ID = "B0104";
        employee2.Name = "王柏仁";
        employee2.Salary = 19000;

        employee1.showinfo();
        employee2.showinfo();
    }
}