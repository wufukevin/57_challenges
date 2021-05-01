using System;
using System.Collections.Generic;
using System.Reflection;

namespace zoe_4_18
{

  class Program
  {
    static void Main()
    {
      Console.WriteLine("Press C to convert from Fahrenheit to Celsius. \nPress F to convert from Celsius to Fahrenheit.\nPress K to convert from Celsius to Kelvin.");

      string toUnit;

      do
      {
        Console.Write("Your choice: ");
        toUnit = Console.ReadLine().ToUpper();
      } while (toUnit != "C" && toUnit != "F" && toUnit != "K");

      // C => FToC
      // F => CToF
      // K => CToK
      Dictionary<string, string> convertFromType = new()
      {
        { "C", "F" },
        { "F", "K" },
        { "K", "C" },
      };

      Dictionary<string, string> temperatureUnitName = new()
      {
        { "C", "Celsius" },
        { "F", "Fahrenheit" },
        { "K", "Kelvin" },
      };

      var fromUnit = convertFromType[toUnit];

      Console.Write($"Please enter the temperature in {temperatureUnitName[fromUnit]}: ");
      var FromAmount = Convert.ToDouble(Console.ReadLine());


      TemperatureConverter converter = new();

      var result = converter.Run(fromUnit, toUnit, FromAmount);

      Console.WriteLine($"The temperature in {temperatureUnitName[toUnit]} is {result}");
    }
  }
}
