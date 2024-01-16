using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _1204
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void noneToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void 開啟ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.URL = "C:\\Users\\phill\\Videos\\2023 Arknights Ambience 明日方舟音律联觉专场演出-愚夜密函 2023 [KCenkcbT7XA].mkv";
            axWindowsMediaPlayer1.Ctlcontrols.play();
        }

        private void 結束ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.stop();
        }

        private void fullToolStripMenuItem_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.fullScreen = true;
        }

        private void miniToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void axWindowsMediaPlayer1_Enter(object sender, EventArgs e)
        {

        }
    }
}
