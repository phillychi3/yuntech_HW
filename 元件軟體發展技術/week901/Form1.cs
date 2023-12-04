namespace week901
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime dateTime = dateTimePicker1.Value;
            DateTime livetimest = monthCalendar1.SelectionStart;
            DateTime livetimeed = monthCalendar1.SelectionEnd;
            TimeSpan ts = livetimeed - livetimest;
            int days = ts.Days;
            int price = 3000;
            int total = price * days;
            label2.Text = "入住房型為: 標準雙人房\n";

            if(dateTime.Month == livetimest.Month)
            {
                label2.Text += "生日優惠: 享有九折優惠\n";
                total = (int)(total *  0.9);
        }
            label2.Text += "入住天數: " + days + "天\n";
            label2.Text += "總金額: " + total + "元\n";







        }

        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {

        }
    }
}