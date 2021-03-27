using System;
using zoe_3_8.PizzaCounters;

namespace zoe_3_8
{
  partial class Program
  {
    static void Main()
    {

      var modeQuestion = "please choose mode\n1) divide pizza\n2) purchase pizza";

      string mode;
      do
      {
        mode = ConsoleUtil.AskForInputString(modeQuestion);
      } while (mode != "1" && mode != "2");


      bool isDividePizza = mode == "1";

      IPizzaCounter pizzaCounter;

      if (isDividePizza)
      {
        pizzaCounter = new DividePizzaCounter();
      }
      else
      {
        pizzaCounter = new PurchasePizzaCounter();
      }

      try
      {
        pizzaCounter.ServingClient();
      }
      catch
      {
        return;
      }

    }
  }
}
