using System;

namespace zoe_4_18
{
  class TemperatureConverter
  {
    public double Run(string fromUnit, string toUnit, double fromAmount)
    {
      var formulaName = fromUnit + "To" + toUnit;

      string result = GetType().GetMethod(formulaName).Invoke(this, new object[] { fromAmount }).ToString();

      return Convert.ToDouble(result);
    }

    public double CToF(double C)
    {
      return C * 9 / 5 + 32;
    }

    public double FToC(double F)
    {
      return (F - 32) * 5 / 9;
    }

    public double CToK(double C)
    {
      return C + 273.15;
    }

    public double FToK(double F)
    {
      return (F + 459.67) * 5 / 9;
    }

  }
}
