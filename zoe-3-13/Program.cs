using System;

namespace zoe_3_13
{
  class Program
  {
    static void Main()
    {
      var principalQuestion = "What is the principal amount ? ";
      var rateQuestion = "What is the rate ? ";
      var yearQuestion = "What is the number of years ? ";
      var timesQuestion = "What is the number of times the interest is compounded per year ? ";

      var principal = Util.AskForInputDouble(principalQuestion);
      var rate = Util.AskForInputDouble(rateQuestion);
      var year = Util.AskForInputDouble(yearQuestion);
      var times = Util.AskForInputDouble(timesQuestion);

      var result = calculateCompoundInterest(principal, rate, year, times);

      var answer = $"${principal} invested at {rate}% for {year} years compounded {times} times per year is ${result}.";

      Util.ConsoleAnswer(answer);

    }

    static double calculateCompoundInterest(double principal, double rate, double year, double times)
    {
      var ratio = (1 + rate * 0.01 / times);
      var total = principal * Math.Pow(ratio, times * year);
      return Util.RoundUpPlaces(total, 2);
    }
  }
}
