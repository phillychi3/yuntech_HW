namespace week1001
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != textBox1.Text.ToLower())
            {
                MessageBox.Show("Please input lower case");
                return;
            }if(textBox1.Text != "good")
            {
                MessageBox.Show("not a correct account or password");
                return;
            }
            if (int.TryParse(textBox2.Text, out int result))
            {
                if (result != 123)
                {
                    MessageBox.Show("not a correct account or password");
                    return;
                }
            }
            else
            {
                MessageBox.Show("shoule be int");
                return;
            }
            MessageBox.Show("Login Success");
        }
    }
}