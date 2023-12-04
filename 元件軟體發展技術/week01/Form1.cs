namespace week01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int select_class = 0;
        string sizetext = "";
        string drink = "";
        string other1 = "";
        string other2 = "";
        string other3 = "";

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                other1 = "加冰";
            }
            else
            {
                other1 = "";
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            select_class = 1;
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int dollor = 0;
            if(sizetext=="小杯")
            {
                dollor += 30;
            }
            else if(sizetext=="大杯")
            {
                dollor += 35;
            }
            if(other2!="")
            {
                dollor += 2;
            }
            if(other3!="")
            {
                dollor -= 5;
            }
            label2.Text = sizetext + drink + other1 + other2 + other3 + "總共" + dollor.ToString() + "元";
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            select_class = 2;
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            select_class = 3;
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox2.Checked == true)
            {
                other2 = "塑膠袋";
            }
            else
            {
                other2 = "";
            }
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox3.Checked == true)
            {
                other3 = "自備容器";
            }
            else
            {
                other3 = "";
            }
        }

        private void radioButton6_CheckedChanged(object sender, EventArgs e)
        {
            sizetext = "小杯";
        }

        private void radioButton5_CheckedChanged(object sender, EventArgs e)
        {
            sizetext = "大杯";
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}