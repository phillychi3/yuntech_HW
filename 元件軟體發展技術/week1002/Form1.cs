namespace week1002
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

        }
        int mouseX = 0;
        int mouseY = 0;
        bool isMouseDown = false;

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Text = "moving...";
        }

        private void button1_MouseUp(object sender, MouseEventArgs e)
        {
            button1.BackColor = Color.Wheat;
            isMouseDown = false;
        }

        private void button1_MouseDown(object sender, MouseEventArgs e)
        {
            button1.BackColor = Color.Blue;
            isMouseDown = true;
        }

        private void button1_MouseMove(object sender, MouseEventArgs e)
        {
            if(isMouseDown)
            {
                mouseX = Cursor.Position.X;
                mouseY = Cursor.Position.Y;
                button1.Location = new Point(mouseX, mouseY);
            }
        }
    }
}