using System;
using zoe_3_9.ShapeCounters;

namespace zoe_3_9
{
  partial class Program
  {
    class ShapeAreaCounter
    {
      public static IShapeCounter GetCounter(string mode)
      {
        switch (mode)
        {
          case "2":
            return new RoundCounter();
          case "3":
            return new LShapedCounter();
          case "1":
          default:
            return new RectangleCounter(); ;
        }
      }
    }

    static void Main()
    {
      string mode = checkShape();

      IShapeCounter shapeAreaCounter = ShapeAreaCounter.GetCounter(mode);

      double area;
      try
      {
        area = shapeAreaCounter.getArea();
      }
      catch
      {
        return;
      }

      string answer = CountingPaint(area);

      ConsoleUtil.ConsoleAnswer(answer);

    }

    private static string checkShape()
    {
      string modeQuestion = "please choose shape\n1) a rectangle room \n2) a round room. \n3) an L-shaped room ";

      string mode;

      do
      {
        mode = ConsoleUtil.AskForInputString(modeQuestion);
      } while (mode != "1" && mode != "2" && mode != "3");

      return mode;
    }

    private static string CountingPaint(double area)
    {
      int coverAreaPerGallon = 350;
      int amount = (int)Math.Ceiling((double)area / (double)coverAreaPerGallon);

      return $"You will need to purchase {amount} gallons of paint to cover {area} square feet.";
    }

  }
}
