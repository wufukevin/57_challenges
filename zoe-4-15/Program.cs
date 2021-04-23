using System;

namespace zoe_4_15
{
  class Program
  {
    static readonly string password = "abc$123";
    static void Main()
    {
      var inputPassword = Utils.AskForInputString("What is the password ? ");
      var isPass = password == inputPassword;

      if (isPass)
        Utils.ConsoleAnswer("Welcome!");
      else
        Utils.ConsoleAnswer("I don't know you.");
    }
  }
}
