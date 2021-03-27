using System;

namespace zoe_3_9
{
  class Program
  {
    static void Main()
    {
      ConsoleUtil console = new ConsoleUtil();

      string mode = checkShape();

      IShapeCounter shapeAreaCounter = new RectangleCounter();

      switch (mode)
      {
        case "1":
          shapeAreaCounter = new RectangleCounter();
          break;
        case "2":
          shapeAreaCounter = new RoundCounter();
          break;
        case "3":
          shapeAreaCounter = new LShapedCounter();
          break;
        default:
          return;
      }

      double area;
      try
      {
        area = shapeAreaCounter.getArea();
      }
      catch
      {
        return;
      }

      string answer = countingPaint(area);

      console.ConsoleAnswer(answer);

    }

    private static string checkShape()
    {
      string modeQuestion = "please choose shape\n1) a rectangle room \n2) a round room. \n3) an L-shaped room ";

      ConsoleUtil console = new ConsoleUtil();

      string mode;

      do
      {
        mode = console.AskForInputString(modeQuestion);
      } while (mode != "1" && mode != "2" && mode != "3");

      return mode;
    }

    private static string countingPaint(double area)
    {
      int coverAreaPerGallon = 350;
      int amount = (int)Math.Ceiling((double)area / (double)coverAreaPerGallon);

      return $"You will need to purchase {amount} gallons of paint to cover {area} square feet.";
    }

    interface IShapeCounter
    {
      public double[] checkSize();
      public double countArea(double[] size);
      public double getArea()
      {
        double[] size = checkSize();

        double area = countArea(size);

        return area;
      }
    }

    class RectangleCounter : ConsoleUtil, IShapeCounter
    {
      ConsoleUtil console = new ConsoleUtil();
      public double[] checkSize()
      {
        double width;
        double length;

        try
        {
          width = console.AskForInputDouble("What is the length of the room in feet? ");
          length = console.AskForInputDouble("What is the width of the room in feet? ");
        }
        catch
        {
          Console.WriteLine("Cannot parse");
          throw;
        }

        double[] size = { width, length };
        return size;
      }
      public double countArea(double[] size)
      {
        double width = size[0];
        double length = size[1];

        return width * length;
      }
    }

    class RoundCounter : ConsoleUtil, IShapeCounter
    {
      ConsoleUtil console = new ConsoleUtil();
      public double[] checkSize()
      {
        double radius;

        try
        {
          radius = console.AskForInputDouble("What is the radius of the room in feet? ");
        }
        catch
        {
          Console.WriteLine("Cannot parse");
          throw;
        }

        double[] size = { radius };
        return size;
      }
      public double countArea(double[] size)
      {
        double radius = size[0];

        return Math.PI * radius * radius;
      }
    }

    class LShapedCounter : ConsoleUtil, IShapeCounter
    {
      ConsoleUtil console = new ConsoleUtil();
      public double[] checkSize()
      {
        double width;
        double length;
        double inner_width;
        double inner_length;

        try
        {
          width = console.AskForInputDouble("What is the length of the room in feet? ");
          length = console.AskForInputDouble("What is the width of the room in feet? ");
          inner_width = console.AskForInputDouble("What is the inner length of the room in feet? ");
          inner_length = console.AskForInputDouble("What is the inner length of the room in feet? ");
        }
        catch
        {
          Console.WriteLine("Cannot parse");
          throw;
        }

        double[] size = { width, length, inner_width, inner_length };
        return size;
      }
      public double countArea(double[] size)
      {
        double width = size[0];
        double length = size[1];
        double inner_width = size[2];
        double inner_length = size[3];

        return (width * length) - (inner_width * inner_length);
      }
    }

    class ConsoleUtil
    {
      public double AskForInputDouble(string question)
      {
        ConsoleQuestion(question);

        return Convert.ToDouble(Console.ReadLine());
      }
      public int AskForInputNumber(string question)
      {
        ConsoleQuestion(question);

        return Convert.ToInt32(Console.ReadLine());
      }

      public string AskForInputString(string question)
      {
        ConsoleQuestion(question);

        return Console.ReadLine();
      }

      public string CheckPluralNoun(string noun, int amount)
      {
        return amount > 1 ? $"{noun}s" : noun;
      }

      public void ConsoleQuestion(string question)
      {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine(question);
        Console.ResetColor();
      }

      public void ConsoleAnswer(string answer)
      {
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("");
        Console.WriteLine(answer);
        Console.ResetColor();
      }
    }

  }
}
