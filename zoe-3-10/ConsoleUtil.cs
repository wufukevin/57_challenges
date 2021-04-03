using System;

namespace zoe_3_10
{
  class ConsoleUtil
  {
    public static double AskForInputDouble(string question)
    {
      ConsoleQuestion(question);

      try
      {
        return Convert.ToDouble(Console.ReadLine());
      }
      catch
      {
        throw;
      }
    }
    public static int AskForInputNumber(string question)
    {
      ConsoleQuestion(question);

      try
      {
        return Convert.ToInt32(Console.ReadLine());
      }
      catch
      {
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
