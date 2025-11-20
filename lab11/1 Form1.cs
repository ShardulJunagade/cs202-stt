namespace EventPlayground
{
    public partial class Form1 : Form
    {
        // Custom delegates
        public delegate void ColorChangedHandler(System.Drawing.Color newColor);
        public delegate void TextChangedHandler(string newText);

        // Events based on those delegates
        public event ColorChangedHandler ColorChangedEvent;
        public event TextChangedHandler TextChangedEvent;

        // This will be called when ColorChangedEvent is raised
        private void UpdateLabelColor(System.Drawing.Color newColor)
        {
            lblMessage.ForeColor = newColor;
        }

        // This will be called when TextChangedEvent is raised
        private void UpdateLabelText(string newText)
        {
            lblMessage.Text = newText;
        }

        public Form1()
        {
            InitializeComponent();
            // Subscribe methods to our custom events
            ColorChangedEvent += UpdateLabelColor;
            TextChangedEvent += UpdateLabelText;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnChangeColor_Click(object sender, EventArgs e)
        {
            // Get selected colour name from ComboBox
            string? selectedColorName = cmbColors.SelectedItem?.ToString();

            if (string.IsNullOrEmpty(selectedColorName))
            {
                MessageBox.Show("Please select a colour from the list.");
                return;
            }

            // Convert name to actual Color
            System.Drawing.Color selectedColor;

            switch (selectedColorName)
            {
                case "Red":
                    selectedColor = System.Drawing.Color.Red;
                    break;
                case "Green":
                    selectedColor = System.Drawing.Color.Green;
                    break;
                case "Blue":
                    selectedColor = System.Drawing.Color.Blue;
                    break;
                default:
                    // fallback
                    selectedColor = System.Drawing.Color.Black;
                    break;
            }

            // Raise the custom event (if there are subscribers)
            ColorChangedEvent?.Invoke(selectedColor);
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
