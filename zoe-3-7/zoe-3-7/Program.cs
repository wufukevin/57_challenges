using System;

namespace zoe_3_7
{
  class Program
  {
    static void Main()
    {
      var conversionQuestion = "please choose convertion mode\n1) feet to meter\n2) meter to feet ";

      var conversionMode = string.Empty; // magic string

      do
      {
        conversionMode = askForInputString(conversionQuestion);
      } while (conversionMode != "1" && conversionMode != "2");

      var isInputFeet = conversionMode == "1";
      var inputUnit = isInputFeet ? "feet" : "meter";
      var outputUnit = isInputFeet ? "meter" : "feet";
      var feetToMeterRatio = 0.09290304;
      var conversionRatio = Math.Pow(feetToMeterRatio, isInputFeet ? 1 : -1);

      calculateArea(inputUnit, outputUnit, conversionRatio);
    }

    private static double askForInputNumber(string question)
    {
      Console.ForegroundColor = ConsoleColor.Yellow;
      Console.Write(question);
      Console.ResetColor();

      return Convert.ToDouble(Console.ReadLine());
    }

    private static string askForInputString(string question)
    {
      Console.ForegroundColor = ConsoleColor.Yellow;
      Console.Write(question);
      Console.ResetColor();

      return Console.ReadLine();
    }

    private static void calculateArea(string inputUnit, string outputUnit, double conversionRatio)
    {
      var lengthQuestion = $"What is the length of the room in {inputUnit} ? ";
      var widthQuestion = $"What is the width of the room in {inputUnit} ? ";

      var length = 0.0;
      var width = 0.0;

      try
      {
        length = askForInputNumber(lengthQuestion);
        width = askForInputNumber(widthQuestion);
      }
      catch
      {
        Console.WriteLine("Cannot parse");
        return;
      }

      var area = length * width;
      var areaConvertTo = Math.Round(area * conversionRatio, 3);

      var answer = $"You entered dimensions of {length} {inputUnit} by {width} {inputUnit}.\nThe area is\n{area} square {inputUnit}\n{areaConvertTo} square {outputUnit}";

      Console.ForegroundColor = ConsoleColor.Cyan;
      Console.WriteLine(answer);
      Console.ResetColor();
    }
  }
}
