using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EventPlayground
{
    public class ColorEventArgs : EventArgs
    {
        public string ColorName { get; }

        public ColorEventArgs(string colorName)
        {
            ColorName = colorName;
        }
    }
}
