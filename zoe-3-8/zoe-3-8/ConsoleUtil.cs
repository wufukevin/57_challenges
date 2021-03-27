using System;

namespace zoe_3_8
{
  public class ConsoleUtil
  {
    public static int AskForInputNumber(string question)
    {
      ConsoleQuestion(question);

      try
      {
        return Convert.ToInt32(Console.ReadLine());
      }
      catch
      {
        Console.WriteLine("Cannot parse");
        throw;
      }
    }

    public static string AskForInputString(string question)
    {
      ConsoleQuestion(question);

      return Console.ReadLine();
    }

    public static string CheckPluralNoun(string noun, int amount)
    {
      return amount > 1 ? $"{noun}s" : noun;
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

  }
}
