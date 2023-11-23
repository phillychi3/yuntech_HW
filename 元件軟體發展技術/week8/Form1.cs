using System.Diagnostics;
using System.Security.Policy;

namespace week8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int errortime = 0;
        string username = "google";
        string password = "1688";
        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == username && textBox2.Text == password)
            {
                Process.Start("explorer", "https://google.com");
                MessageBox.Show("welcome to googole lol");
            }
            else
            {
                errortime++;
                MessageBox.Show($"you only left {3 - errortime} times");
                if (errortime >= 3)
                {
                    MessageBox.Show("wow looks you error times over 3");
                    Close();
                }
            }

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}