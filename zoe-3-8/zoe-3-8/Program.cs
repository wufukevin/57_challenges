using System;

namespace zoe_3_8
{
  class Program
  {
    static void Main()
    {

      var modeQuestion = "please choose mode\n1) divide pizza\n2) purchase pizza";
      var console = new ConsoleUtil();

      string mode;
      do
      {
        mode = console.AskForInputString(modeQuestion);
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

      pizzaCounter.ReceivingClient();
    }

    public interface IPizzaCounter
    {

      public void GetOrder();
      public void Counting();
      public void Print();

      void ReceivingClient()
      {
        GetOrder();
        Counting();
        Print();
      }
    }

    class ConsoleUtil
    {
      public int AskForInputNumber(string question)
      {
        ConsoleQuestion(question);

        return Convert.ToInt32(Console.ReadLine());
      }

      public string AskForInputString(string question)
      {
        ConsoleQuestion(question);

        return Console.ReadLine();
      }

      public string CheckPluralNoun(string noun, int amount)
      {
        return amount > 1 ? $"{noun}s" : noun;
      }

      public void ConsoleQuestion(string question)
      {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine(question);
        Console.ResetColor();
      }

      public void ConsoleAnswer(string answer)
      {
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("");
        Console.WriteLine(answer);
        Console.ResetColor();
      }

    }

    class DividePizzaCounter : ConsoleUtil, IPizzaCounter
    {
      readonly string peopleQuestion = "How many people?";
      readonly string pizzaQuestion = "How many pizzas do you have?";

      int people;
      int pizza;

      string answer;

      public void GetOrder()
      {
        try
        {
          do
          {
            people = AskForInputNumber(peopleQuestion);
          } while (people <= 0);

          pizza = AskForInputNumber(pizzaQuestion);
        }
        catch
        {
          Console.WriteLine("Cannot parse");
          return;
        }
      }

      public void Counting()
      {
        int slicePerPizza = 8;
        int totalSlice = pizza * slicePerPizza;

        int slicePerPerson = totalSlice / people;
        int sliceLeftover = totalSlice % people;

        answer = $"{people} people with {pizza} {CheckPluralNoun("pizza", pizza)}\nEach person gets {slicePerPerson} {CheckPluralNoun("piece", slicePerPerson)} of pizza.\nThere are {sliceLeftover} leftover {CheckPluralNoun("piece", sliceLeftover)}.";
      }

      public void Print()
      {
        ConsoleAnswer(answer);
      }
    }

    class PurchasePizzaCounter : ConsoleUtil, IPizzaCounter
    {
      readonly string peopleQuestion = "How many people?";
      readonly string sliceQuestion = "How many slices each person wants?";
      int people;
      int slice;

      string answer;
      public void GetOrder()
      {
        try
        {
          people = AskForInputNumber(peopleQuestion);
          slice = AskForInputNumber(sliceQuestion);
        }
        catch
        {
          Console.WriteLine("Cannot parse");
          return;
        }
      }
      public void Counting()
      {
        int totalSlice = people * slice;
        int slicePerPizza = 8;

        int pizza = (int)Math.Ceiling((double)totalSlice / (double)slicePerPizza);

        answer = $"{people} people X {slice} {CheckPluralNoun("piece", slice)} = {totalSlice} {CheckPluralNoun("slice", totalSlice)} <= {pizza} {CheckPluralNoun("pizza", pizza)}";
      }

      public void Print()
      {
        ConsoleAnswer(answer);
      }
    }
  }
}
