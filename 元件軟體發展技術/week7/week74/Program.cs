using static Employee;

System.Console.WriteLine("要輸入多少員工紀錄");
int numEmployees = int.Parse(Console.ReadLine());

Employee[] employees = new Employee[numEmployees];

// 讓使用者逐一輸入員工資訊
for (int i = 0; i < numEmployees; i++)
{
    employees[i] = new Employee();
    // 輸入編號
    Console.WriteLine("請輸入第 {0} 位員工的編號：", i + 1);
    employees[i].EmpID = Console.ReadLine();

    // 輸入姓名
    Console.WriteLine("請輸入第 {0} 位員工的姓名：", i + 1);
    employees[i].EmpName = Console.ReadLine();

    // 輸入薪資
    Console.WriteLine("請輸入第 {0} 位員工的薪資：", i + 1);
    employees[i].EmpSalary = int.Parse(Console.ReadLine());
}

// 顯示所有員工的資訊
foreach (Employee employee in employees)
{
    employee.ShowInfo();
}
