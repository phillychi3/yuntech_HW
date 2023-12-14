namespace week1003
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            pictureBox1.MouseWheel += PictureBox1_MouseWheel;
        }

        private void PictureBox1_MouseWheel(object? sender, MouseEventArgs e)
        {
            pictureBox1.Width += e.Delta / 10;
            pictureBox1.Height += e.Delta / 10;

        }

        bool isdoen = false;

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            isdoen = true;
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            isdoen = false;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            Point pp = PointToClient(Cursor.Position);
            if (isdoen)
            {
                pictureBox1.Location = pp;
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {

        }
    }
}