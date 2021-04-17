using System;

namespace zoe_3_13
{
  class Program
  {
    static void Main()
    {
    //   var principalQuestion = "What is the principal amount ? ";
      var rateQuestion = "What is the rate ? ";
      var yearQuestion = "What is the number of years ? ";
      var timesQuestion = "What is the number of times the interest is compounded per year ? ";
      var goalQuestion = "What is the goal ? ";

    //   var principal = Util.AskForInputDouble(principalQuestion);
      var rate = Util.AskForInputDouble(rateQuestion);
      var year = Util.AskForInputDouble(yearQuestion);
      var times = Util.AskForInputDouble(timesQuestion);
      var goal = Util.AskForInputDouble(goalQuestion);

    //   var result = calculateCompoundInterest(principal, rate, year, times);

    //   var answer = $"${principal} invested at {rate}% for {year} years compounded {times} times per year is ${result}.";


    var result = calculatePrincipal(goal, rate, year, times);

    var answer = $"you need to invest ${result} for {year} years at {rate}% compounded {times} times per year to meet ${goal}";

      Util.ConsoleAnswer(answer);

    }

    static double calculateCompoundInterest(double principal, double rate, double year, double times)
    {
      var baseNumber = 1 + rate * 0.01 / times;
      var power = times * year;
      var total = principal * Math.Pow(baseNumber, power);
      return Util.RoundUpPlaces(total, 2);
    }

    static double calculatePrincipal(double goal, double rate, double year, double times)
    {
      var baseNumber = 1 + rate * 0.01 / times;
      var power = times * year;
      var principal = goal / Math.Pow(baseNumber, power);
      return Util.RoundUpPlaces(principal, 2);
    }
  }
}
