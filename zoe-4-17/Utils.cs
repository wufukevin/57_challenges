using System;

namespace zoe_4_17
{
  class Utils
  {
    public static double AskForInputDouble(string question)
    {
      ConsoleQuestion(question);
      string input = Console.ReadLine();

      try
      {
        return Convert.ToDouble(input);
      }
      catch
      {
        throw;
      }
    }
    public static int AskForInputInt(string question)
    {
      ConsoleQuestion(question);

      // try
      // {
        var input = Convert.ToInt32(Console.ReadLine());

        // if (input < 0)
        // {
        //   throw new AgeException();
        // }

        return input;
      // }
      // catch
      // {
      //   throw new AgeException();
      // }
    }

    public static string AskForInputString(string question)
    {
      ConsoleQuestion(question);

      return Console.ReadLine();
    }

    public static void ConsoleQuestion(string question)
    {
      Console.ForegroundColor = ConsoleColor.Yellow;
      Console.WriteLine(question);
      Console.ResetColor();
    }

    public static void ConsoleAnswer(string answer)
    {
      Console.ForegroundColor = ConsoleColor.Cyan;
      Console.WriteLine("");
      Console.WriteLine(answer);
      Console.ResetColor();
    }

    public static double RoundDownPlaces(double value, int places)
    {
      return Math.Round(value, places, MidpointRounding.ToNegativeInfinity);
    }

    public static double RoundUpPlaces(double value, int places)
    {
      return Math.Round(value, places, MidpointRounding.ToPositiveInfinity);
    }

    public static string CheckPluralNoun(string noun, int amount)
    {
      return amount > 1 ? $"{noun}s" : noun;
    }

  }

}