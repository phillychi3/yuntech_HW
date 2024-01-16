namespace _1202
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

        private void button1_Click(object sender, EventArgs e)
        {   //如果textbox1 或者textbox2 文字轉int大於50 ，發生警告聲音
            if(Convert.ToInt32(textBox1.Text) > 50 || Convert.ToInt32(textBox2.Text) > 50)
            {
                System.Media.SystemSounds.Exclamation.Play();
                MessageBox.Show("請輸入小於50的數字");
            }
            label2.Text = Convert.ToString(Convert.ToInt32(textBox1.Text) + Convert.ToInt32(textBox2.Text));
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}