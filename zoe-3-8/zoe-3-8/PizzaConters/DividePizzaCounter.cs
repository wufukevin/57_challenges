using System;

namespace zoe_3_8.PizzaCounters
{
  public class DividePizzaCounter : IPizzaCounter
  {
    readonly string peopleQuestion = "How many people?";
    readonly string pizzaQuestion = "How many pizzas do you have?";

    int people;
    int pizza;

    string answer;

    public void GetOrder()
    {
      do
      {
        people = ConsoleUtil.AskForInputNumber(peopleQuestion);
      } while (people <= 0);

      pizza = ConsoleUtil.AskForInputNumber(pizzaQuestion);
    }

    public void Counting()
    {
      
      int totalSlice = pizza * IPizzaCounter.slicePerPizza;

      int slicePerPerson = totalSlice / people;
      int sliceLeftover = totalSlice % people;

      answer = $"{people} people with {pizza} {ConsoleUtil.CheckPluralNoun("pizza", pizza)}\nEach person gets {slicePerPerson} {ConsoleUtil.CheckPluralNoun("piece", slicePerPerson)} of pizza.\nThere are {sliceLeftover} leftover {ConsoleUtil.CheckPluralNoun("piece", sliceLeftover)}.";
    }

    public void Print()
    {
      ConsoleUtil.ConsoleAnswer(answer);
    }
  }
}
