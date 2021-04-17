using System;
using System.Collections.Generic;
using System.Net.Http;

namespace zoe_3_11
{
  class Program
  {
    static void Main()
    {

      Dictionary<string, double> USDExchangeRate = new()
      {
        { "USD (US)", 1 },
        { "NTD (Taiwan)", 28.317289 },
        { "JPY (Japen)", 108.752661 },
        { "EUR (Euro)", 0.834641 },
      };

      var currcyList = new List<string>(USDExchangeRate.Keys);
      int countryIndex = 0;

      foreach (var country in currcyList)
      {
        ConsoleUtil.ConsoleQuestion($"{countryIndex}) {country}");
        countryIndex++;
      }

      CallExchangApi();

      // ask currency
      var rateFromQuestion = "what currency you want to exchange ? ";
      var rateToQuestion = "what currency you want to exchange for ? ";

      var currencyFrom = currcyList[ConsoleUtil.AskForInputInt(rateFromQuestion)];
      var currencyTo = currcyList[ConsoleUtil.AskForInputInt(rateToQuestion)];

      var rateFrom = USDExchangeRate[currencyFrom];
      var rateTo = USDExchangeRate[currencyTo];

      // ask amount
      var amountQuestion = $"How much {currencyFrom} would you like to change ? ";
      // var exchangeRateQuestion = "What is the exchange rate ? ";

      var amountFrom = ConsoleUtil.AskForInputDouble(amountQuestion);
      // var exchangeRate = ConsoleUtil.AskForInputDouble(exchangeRateQuestion);

      // var result = amountFrom * exchangeRate;
      var result = amountFrom * rateTo / rateFrom;
      var roundUpResult = RoundUpPlaces(result, 2);

      // var answer = $"{amountFrom} EUR X {exchangeRate} = {roundUpResult} USD ({result})";
      var answer = $"{amountFrom} {currencyFrom} X {rateTo / rateFrom} = {roundUpResult} {currencyTo}";

      ConsoleUtil.ConsoleAnswer(answer);

    }

    static readonly HttpClient client = new();

    static async void CallExchangApi()
    {
      try
      {
        HttpResponseMessage response = await client.GetAsync("https://api.exchangerate-api.com/v4/latest/USD");
        response.EnsureSuccessStatusCode();
        string responseBody = await response.Content.ReadAsStringAsync();

        Console.WriteLine(responseBody);
      }
      catch (HttpRequestException e)
      {
        Console.WriteLine("\nException Caught!");
        Console.WriteLine("Message :{0} ", e.Message);
      }
    }

    static double RoundUpPlaces(double value, int places)
    {
      var baseNumber = Math.Pow(10, places);
      return Math.Floor(value * baseNumber) / baseNumber;
    }
  }
}
