using System;

namespace zoe_3_8.PizzaCounters
{
  public class PurchasePizzaCounter : IPizzaCounter
  {
    const string peopleQuestion = "How many people?";
    const string sliceQuestion = "How many slices each person wants?";
    int people;
    int slice;

    string answer;
    public void GetOrder()
    {
      people = ConsoleUtil.AskForInputNumber(peopleQuestion);
      slice = ConsoleUtil.AskForInputNumber(sliceQuestion);
    }
    public void Counting()
    {
      int totalSlice = people * slice;

      int pizza = (int)Math.Ceiling(totalSlice / (double)IPizzaCounter.slicePerPizza);

      answer = $"{people} people X {slice} {ConsoleUtil.CheckPluralNoun("piece", slice)} = {totalSlice} {ConsoleUtil.CheckPluralNoun("slice", totalSlice)} <= {pizza} {ConsoleUtil.CheckPluralNoun("pizza", pizza)}";
    }

    public void Print()
    {
      ConsoleUtil.ConsoleAnswer(answer);
    }
  }
}
