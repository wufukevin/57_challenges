using System;
using System.Collections.Generic;

namespace zoe_4_18
{
 
  class TemperatureConverter
  {
  
    public double Run(string fromUnit, string toUnit, double fromAmount)
    {
      var convertFunctions = new Dictionary<string, Func<double,double>>()
      {
        {"CToF", CToF},
        {"FToC", FToC},
        {"CToK", CToK},
        {"FToK", FToK},
      };

      var formulaName = $"{fromUnit}To{toUnit}";

      double result = convertFunctions[formulaName](fromAmount);

      return result;
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
