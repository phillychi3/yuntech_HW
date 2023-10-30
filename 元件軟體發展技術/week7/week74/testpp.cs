public class Employee
{
    private int EmpSalaryField;

    public string EmpID { get; set; }
    public string EmpName { get; set; }

    public int EmpSalary
    {
        get { return EmpSalaryField; }
        set
        {
            // 檢查薪資是否小於勞工基本薪資
            if (value < 23800)
            {
                // 若是，則設定薪資為勞工基本薪資
                value = 23800;
            }

            // 將薪資設定給私有欄位
            EmpSalaryField = value;
        }
    }

    public void ShowInfo()
    {
        Console.WriteLine("編號：{0}", EmpID);
        Console.WriteLine("姓名：{0}", EmpName);
        Console.WriteLine("薪資：{0}", EmpSalary);
    }
}