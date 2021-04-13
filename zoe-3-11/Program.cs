using System;

namespace zoe_3_11
{
  class Program
  {
    static void Main()
    {
      var amountQuestion = "How many euros are you exchanging ? ";
      var exchangeRateQuestion = "What is the exchange rate ? ";

      var amountFrom = ConsoleUtil.AskForInputDouble(amountQuestion);
      var exchangeRate = ConsoleUtil.AskForInputDouble(exchangeRateQuestion);

      var result = amountFrom * exchangeRate;
      var roundUpResult = RoundUpPlaces(result, 2);

      var answer = $"{amountFrom} EUR X {exchangeRate} = {roundUpResult} USD ({result})";

      ConsoleUtil.ConsoleAnswer(answer);

    }

    static double RoundUpPlaces(double value, int places)
    {
      var baseNumber = Math.Pow(10, places);
      return Math.Floor(value * baseNumber) / baseNumber;
    }
  }
}
