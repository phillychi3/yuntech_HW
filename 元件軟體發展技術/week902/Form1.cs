using week902.Properties;

namespace week902
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        List<Bitmap> Bitmaps = new List<Bitmap>() { Resources._2020_12_24_20_25_09, Resources._2020_12_24_20_26_14, Resources._2020_12_21_00_25_17, Resources._2020_12_11_17_35_26, Resources._2020_12_11_17_35_26, Resources._2020_12_21_00_25_17, Resources._2020_12_24_20_25_09 };
        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            pictureBox1.Image = Bitmaps[trackBar1.Value];
        }

        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            pictureBox1.Width = hScrollBar1.Value*5;
        }

        private void vScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            pictureBox1.Height = vScrollBar1.Value * 5;
        }
    }
}