using System;

namespace zoe_4_16
{
  class Program
  {
    static readonly int drivingLegalAge = 16;
    static void Main()
    {
      var retry = true;
      int age = 0;

      do
      {
        try
        {
          retry = false;
          age = Utils.AskForInputInt("What is your age ? ");
        }
        catch (AgeException)
        {
          Utils.ConsoleAnswer("invalid input, please try again");
          retry = true;
        }
      } while (retry);


      var reuslt = age < drivingLegalAge ? "You are not old enough to legally drive." : "You are old enough to legally drive.";
      Utils.ConsoleAnswer(reuslt);
    }
  }
}
