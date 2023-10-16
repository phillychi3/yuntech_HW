var llist = new string[][] {
    new string[] { "people1", "反映", "熱音", "表現"},
    new string[] { "people2", "反映", "熱音", "表現","wow","wow2"},
    new string[] { "people3", "反映", "熱音"},

};


for (int i = 0; i < 3; i++)
{
    var allstr = "";
    for (int j = 0; j < llist[i].Length; j++)
    {
        allstr += llist[i][j] + " ";
    }
    System.Console.WriteLine($"第{i}列: {allstr}");
}