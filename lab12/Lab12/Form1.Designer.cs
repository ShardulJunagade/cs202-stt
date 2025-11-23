namespace lab12
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        // UI Controls
        private TextBox txtCustomer;
        private ComboBox cmbProduct;
        private NumericUpDown numQuantity;
        private Button btnProcessOrder;
        private Label lblStatus;
        private CheckBox chkExpress;
        private Button btnShipOrder;

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
            txtCustomer = new TextBox();
            cmbProduct = new ComboBox();
            numQuantity = new NumericUpDown();
            btnProcessOrder = new Button();
            lblStatus = new Label();
            chkExpress = new CheckBox();
            btnShipOrder = new Button();
            ((System.ComponentModel.ISupportInitialize)numQuantity).BeginInit();
            SuspendLayout();
            // 
            // txtCustomer
            // 
            txtCustomer.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            txtCustomer.Location = new Point(30, 30);
            txtCustomer.Name = "txtCustomer";
            txtCustomer.PlaceholderText = "Customer Name";
            txtCustomer.Size = new Size(740, 40);
            txtCustomer.TabIndex = 0;
            txtCustomer.TextChanged += txtCustomer_TextChanged;
            // 
            // cmbProduct
            // 
            cmbProduct.DropDownStyle = ComboBoxStyle.DropDownList;
            cmbProduct.FormattingEnabled = true;
            cmbProduct.Items.AddRange(new object[] { "Laptop", "Mouse", "Keyboard" });
            cmbProduct.Location = new Point(30, 90);
            cmbProduct.Name = "cmbProduct";
            cmbProduct.Size = new Size(500, 40);
            cmbProduct.TabIndex = 1;
            // 
            // numQuantity
            // 
            numQuantity.Location = new Point(540, 90);
            numQuantity.Maximum = new decimal(new int[] { 1000, 0, 0, 0 });
            numQuantity.Name = "numQuantity";
            numQuantity.Size = new Size(120, 40);
            numQuantity.TabIndex = 2;
            // 
            // btnProcessOrder
            // 
            btnProcessOrder.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            btnProcessOrder.Location = new Point(30, 150);
            btnProcessOrder.Name = "btnProcessOrder";
            btnProcessOrder.Size = new Size(740, 44);
            btnProcessOrder.TabIndex = 3;
            btnProcessOrder.Text = "Process Order";
            btnProcessOrder.UseVisualStyleBackColor = true;
            btnProcessOrder.Click += btnProcessOrder_Click;
            // 
            // lblStatus
            // 
            lblStatus.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            lblStatus.Location = new Point(30, 300);
            lblStatus.Name = "lblStatus";
            lblStatus.Size = new Size(740, 30);
            lblStatus.TabIndex = 6;
            lblStatus.Text = "Status: Ready";
            // 
            // chkExpress
            // 
            chkExpress.AutoSize = true;
            chkExpress.Location = new Point(30, 204);
            chkExpress.Name = "chkExpress";
            chkExpress.Size = new Size(90, 24);
            chkExpress.TabIndex = 4;
            chkExpress.Text = "Express";
            chkExpress.UseVisualStyleBackColor = true;
            // 
            // btnShipOrder
            // 
            btnShipOrder.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            btnShipOrder.Location = new Point(30, 240);
            btnShipOrder.Name = "btnShipOrder";
            btnShipOrder.Size = new Size(740, 44);
            btnShipOrder.TabIndex = 5;
            btnShipOrder.Text = "Ship Order";
            btnShipOrder.UseVisualStyleBackColor = true;
            btnShipOrder.Click += btnShipOrder_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 360);
            Controls.Add(btnShipOrder);
            Controls.Add(chkExpress);
            Controls.Add(lblStatus);
            Controls.Add(btnProcessOrder);
            Controls.Add(numQuantity);
            Controls.Add(cmbProduct);
            Controls.Add(txtCustomer);
            Name = "Form1";
            Text = "OrderPipeline";
            ((System.ComponentModel.ISupportInitialize)numQuantity).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
    }
}
