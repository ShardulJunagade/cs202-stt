using System;
using System.Windows.Forms;

namespace EventPlayground
{
    public partial class Form1 : Form
    {
        // Custom delegates
        public delegate void ColorChangedHandler(object sender, ColorEventArgs e);
        public delegate void TextChangedHandler(string newText);

        // Events based on those delegates
        public event ColorChangedHandler ColorChangedEvent;
        public event TextChangedHandler TextChangedEvent;

        // This will be called when ColorChangedEvent is raised
        private void UpdateLabelColor(object sender, ColorEventArgs e)
        {
            // Convert color name from EventArgs to actual Color
            System.Drawing.Color newColor;

            switch (e.ColorName)
            {
                case "Red":
                    newColor = System.Drawing.Color.Red;
                    break;
                case "Green":
                    newColor = System.Drawing.Color.Green;
                    break;
                case "Blue":
                    newColor = System.Drawing.Color.Blue;
                    break;
                default:
                    newColor = System.Drawing.Color.Black;
                    break;
            }

            lblMessage.ForeColor = newColor;
        }

        // This will be called when TextChangedEvent is raised
        private void UpdateLabelText(string newText)
        {
            lblMessage.Text = newText;
        }

        private void ShowNotification(object sender, ColorEventArgs e)
        {
            MessageBox.Show($"Selected colour: {e.ColorName}", "Colour Changed");
        }

        public Form1()
        {
            InitializeComponent();

            // ColorChangedEvent now has 2 subscribers (multicast)
            ColorChangedEvent += UpdateLabelColor;
            ColorChangedEvent += ShowNotification;

            // TextChangedEvent still has one
            TextChangedEvent += UpdateLabelText;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnChangeColor_Click(object sender, EventArgs e)
        {
            string? selectedColorName = cmbColors.SelectedItem?.ToString();

            if (string.IsNullOrEmpty(selectedColorName))
            {
                MessageBox.Show("Please select a colour from the list.");
                return;
            }

            // Create EventArgs with the selected colour name
            ColorEventArgs args = new ColorEventArgs(selectedColorName);

            // Raise the custom event with (sender, args)
            ColorChangedEvent?.Invoke(this, args);
        }

        private void btnChangeText_Click(object sender, EventArgs e)
        {
            // build a new text with current date & time
            string newText = "Current date and time: " + DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss");

            // raise custom event
            TextChangedEvent?.Invoke(newText);
        }

        private void cmbColors_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
