namespace week903
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            typeof(Color).GetProperties().ToList().ForEach(p => comboBox1.Items.Add(p.Name));
            typeof(Color).GetProperties().ToList().ForEach(p => comboBox2.Items.Add(p.Name));
            for (int i = 0; i < 100; i++)
            {
                comboBox3.Items.Add(i);
            }
            FontFamily.GetFamilies(richTextBox1.CreateGraphics()).ToList().ForEach(p => comboBox4.Items.Add(p.Name));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // when press button than open a window to select a file ,and show the file context in the richtextbox
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.InitialDirectory = "c:\\";
            openFileDialog.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
            openFileDialog.FilterIndex = 2;
            openFileDialog.RestoreDirectory = true;
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                string filePath = openFileDialog.FileName;
                string fileText = File.ReadAllText(filePath);
                richTextBox1.Text = fileText;
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //show a save success message box
            MessageBox.Show("Save Success");

        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = "";
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.SelectionColor = Color.FromName(comboBox1.SelectedItem.ToString());
        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.SelectionBackColor = Color.FromName(comboBox2.SelectedItem.ToString());
        }

        private void comboBox3_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.SelectionFont = new Font(richTextBox1.SelectionFont.FontFamily, Convert.ToInt32(comboBox3.SelectedItem));
        }

        private void comboBox4_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.SelectionFont = new Font(comboBox4.SelectedItem.ToString(), richTextBox1.SelectionFont.Size);
        }
    }
}
