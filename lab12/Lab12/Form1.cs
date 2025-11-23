using System;
using System.Windows.Forms;
using System.Drawing.Drawing2D; // added for rounded corners

namespace lab12
{
    public partial class Form1 : Form
    {
        // Custom EventArgs for order lifecycle
        public class OrderEventArgs : EventArgs
        {
            public string Customer { get; }
            public string Product { get; }
            public int Quantity { get; }
            public OrderEventArgs(string cust, string prod, int qty) => (Customer, Product, Quantity) = (cust, prod, qty);
        }

        // Custom EventArgs for shipping
        public class ShipEventArgs : EventArgs
        {
            public string Product { get; }
            public bool Express { get; }
            public ShipEventArgs(string p, bool ex) => (Product, Express) = (p, ex);
        }

        // Events
        public event EventHandler<OrderEventArgs>? OrderCreated;
        public event EventHandler<OrderEventArgs>? OrderRejected;
        public event EventHandler<OrderEventArgs>? OrderConfirmed;
        public event EventHandler<ShipEventArgs>? OrderShipped;

        private bool orderIsConfirmed;

        public Form1()
        {
            InitializeComponent();
            // Subscribe base handlers
            OrderCreated += ValidateOrder;
            OrderCreated += DisplayOrderInfo;
            OrderRejected += ShowRejection;
            OrderConfirmed += ShowConfirmation;
            // Hook layout events
            Load += Form1_Load;
            Resize += Form1_Resize;
        }

        // User initiates order processing
        private void btnProcessOrder_Click(object? sender, EventArgs e)
        {
            var customer = txtCustomer.Text.Trim();
            var product = cmbProduct.SelectedItem?.ToString() ?? string.Empty;
            int quantity = (int)numQuantity.Value;
            var args = new OrderEventArgs(customer, product, quantity);
            lblStatus.Text = "Status: Order Created";
            OrderCreated?.Invoke(this, args); // multicast invokes validation + info display
        }

        // Validate then chain confirmation or rejection
        private void ValidateOrder(object? sender, OrderEventArgs e)
        {
            if (e.Quantity <= 0 || string.IsNullOrWhiteSpace(e.Customer) || string.IsNullOrWhiteSpace(e.Product))
            {
                OrderRejected?.Invoke(this, e);
                return;
            }
            lblStatus.Text = "Status: Validated";
            OrderConfirmed?.Invoke(this, e); // event chaining
        }

        // Second subscriber to OrderCreated
        private void DisplayOrderInfo(object? sender, OrderEventArgs e)
        {
            if (string.IsNullOrWhiteSpace(e.Customer) || string.IsNullOrWhiteSpace(e.Product)) return;
            MessageBox.Show($"Order Summary:\nCustomer: {e.Customer}\nProduct: {e.Product}\nQuantity: {e.Quantity}", "Order Info");
        }

        private void ShowRejection(object? sender, OrderEventArgs e)
        {
            orderIsConfirmed = false;
            lblStatus.Text = "Order Invalid – Please retry";
        }

        private void ShowConfirmation(object? sender, OrderEventArgs e)
        {
            orderIsConfirmed = true;
            lblStatus.Text = $"Order Processed Successfully for {e.Customer}";
        }

        // Shipping with dynamic filtering of subscribers
        private void btnShipOrder_Click(object? sender, EventArgs e)
        {
            if (!orderIsConfirmed)
            {
                MessageBox.Show("Cannot ship. Confirm an order first.", "Warning");
                return;
            }
            // Ensure base dispatch subscriber present exactly once
            OrderShipped -= ShowDispatch;
            OrderShipped += ShowDispatch;
            // Dynamic express courier notification
            if (chkExpress.Checked)
            {
                OrderShipped -= NotifyCourier; // prevent duplicates
                OrderShipped += NotifyCourier;
            }
            else
            {
                OrderShipped -= NotifyCourier; // remove if not express
            }
            var product = cmbProduct.SelectedItem?.ToString() ?? string.Empty;
            var shipArgs = new ShipEventArgs(product, chkExpress.Checked);
            OrderShipped?.Invoke(this, shipArgs);
        }

        private void ShowDispatch(object? sender, ShipEventArgs e)
        {
            lblStatus.Text = $"Product dispatched: {e.Product} (Express: {e.Express})";
        }

        private void NotifyCourier(object? sender, ShipEventArgs e)
        {
            if (e.Express)
            {
                MessageBox.Show("Express delivery initiated!", "Courier Notification");
            }
        }

        private void txtCustomer_TextChanged(object sender, EventArgs e)
        {
        }

        // ===== UI Enhancement Methods =====
        private void Form1_Load(object? sender, EventArgs e)
        {
            AdjustLayout();
            ApplyRoundedCorners(24); // initial radius
        }

        private void Form1_Resize(object? sender, EventArgs e)
        {
            AdjustLayout();
            ApplyRoundedCorners(24); // keep radius on resize
        }

        private void AdjustLayout()
        {
            int margin =30; // outer margin
            int gap =20; // gap between product and quantity controls
            int qtyWidth =130; // fixed width for quantity control
            // Customer textbox full width
            txtCustomer.Left = margin;
            txtCustomer.Top = margin;
            txtCustomer.Width = ClientSize.Width - margin *2;
            // Product + Quantity row
            int productTop = txtCustomer.Bottom + gap;
            int quantityLeft = ClientSize.Width - margin - qtyWidth; // align right edge
            numQuantity.Top = productTop;
            numQuantity.Left = quantityLeft;
            numQuantity.Width = qtyWidth;
            // Product width fills remaining space to left of quantity with gap
            cmbProduct.Top = productTop;
            cmbProduct.Left = margin;
            cmbProduct.Width = quantityLeft - gap - margin; // leave gap before quantity
            // Process button full width
            btnProcessOrder.Top = cmbProduct.Bottom + gap;
            btnProcessOrder.Left = margin;
            btnProcessOrder.Width = ClientSize.Width - margin *2;
            // Express checkbox
            chkExpress.Top = btnProcessOrder.Bottom + gap /2;
            chkExpress.Left = margin;
            // Ship button full width
            btnShipOrder.Top = chkExpress.Bottom + gap;
            btnShipOrder.Left = margin;
            btnShipOrder.Width = ClientSize.Width - margin *2;
            // Status label
            lblStatus.Top = btnShipOrder.Bottom + gap;
            lblStatus.Left = margin;
            lblStatus.Width = ClientSize.Width - margin *2;
        }

        private void ApplyRoundedCorners(int radius)
        {
            if (radius <=0) { Region = null; return; }
            if (WindowState == FormWindowState.Maximized)
            {
                Region = null; // avoid visual artifacts when maximized
                return;
            }
            var path = new GraphicsPath();
            int w = Width;
            int h = Height;
            int d = radius *2;
            path.AddArc(0,0, d, d,180,90);
            path.AddArc(w - d,0, d, d,270,90);
            path.AddArc(w - d, h - d, d, d,0,90);
            path.AddArc(0, h - d, d, d,90,90);
            path.CloseFigure();
            Region = new System.Drawing.Region(path);
        }
    }
}
