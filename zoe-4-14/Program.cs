using System;

namespace zoe_4_14
{
  class Program
  {
    static readonly double wiTaxRate = 5.5 * 0.01;
    static void Main()
    {
      var amountQuestion = "What is the order amount ? ";
      var stateQuestion = "What is the state ? ";

      var amount = Utils.RoundUpPlaces(Utils.AskForInputDouble(amountQuestion), 2);
      var state = Utils.AskForInputString(stateQuestion);
      var isWi = state.ToLower() == "wi" || state.ToLower() == "Wisconsin";

      var subtotal = amount;
      var taxTate = state.ToLower() == "wi" ? wiTaxRate : 0;
      var tax = Utils.RoundUpPlaces(amount * wiTaxRate);
      var total = subtotal + tax;

      if (isWi)
      {
        Utils.ConsoleAnswer($"The subtotal is {subtotal:C2}.");
        Utils.ConsoleAnswer($"The tax is {tax:C2}.");
      }

      Utils.ConsoleAnswer($"The total is {total:C2}.");
    }
  }
}
