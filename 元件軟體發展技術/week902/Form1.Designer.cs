namespace week902
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            pictureBox1 = new PictureBox();
            hScrollBar1 = new HScrollBar();
            vScrollBar1 = new VScrollBar();
            trackBar1 = new TrackBar();
            label1 = new Label();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)trackBar1).BeginInit();
            SuspendLayout();
            // 
            // pictureBox1
            // 
            pictureBox1.Image = Properties.Resources._2020_12_11_17_35_26;
            pictureBox1.Location = new Point(50, 29);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(442, 269);
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            pictureBox1.TabIndex = 0;
            pictureBox1.TabStop = false;
            // 
            // hScrollBar1
            // 
            hScrollBar1.Location = new Point(50, 316);
            hScrollBar1.Name = "hScrollBar1";
            hScrollBar1.Size = new Size(431, 17);
            hScrollBar1.TabIndex = 1;
            hScrollBar1.Scroll += hScrollBar1_Scroll;
            // 
            // vScrollBar1
            // 
            vScrollBar1.Location = new Point(527, 9);
            vScrollBar1.Name = "vScrollBar1";
            vScrollBar1.Size = new Size(17, 324);
            vScrollBar1.TabIndex = 2;
            vScrollBar1.Scroll += vScrollBar1_Scroll;
            // 
            // trackBar1
            // 
            trackBar1.Location = new Point(50, 362);
            trackBar1.Name = "trackBar1";
            trackBar1.Size = new Size(431, 45);
            trackBar1.TabIndex = 3;
            trackBar1.Scroll += trackBar1_Scroll;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(502, 378);
            label1.Name = "label1";
            label1.Size = new Size(42, 15);
            label1.TabIndex = 4;
            label1.Text = "label1";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(567, 432);
            Controls.Add(label1);
            Controls.Add(trackBar1);
            Controls.Add(vScrollBar1);
            Controls.Add(hScrollBar1);
            Controls.Add(pictureBox1);
            Name = "Form1";
            Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ((System.ComponentModel.ISupportInitialize)trackBar1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private PictureBox pictureBox1;
        private HScrollBar hScrollBar1;
        private VScrollBar vScrollBar1;
        private TrackBar trackBar1;
        private Label label1;
    }
}