using System;
using System.Collections.Generic;
namespace zoe_4_17
{
  class Program
  {
    static void Main()
    {
      // var weight = 0.0;
      // var gender = ""; // F/M
      // var volumn = 0.0;
      // var hour = 0.0;

      // BloodAlcoholCalculator Calculator = new(weight, hour, volumn, gender);

      // var BAC = Calculator.GetBloodAlcoholContent();

      // string[] femaleValues = {"f", "femal"};

      List<string> femaleValues = new();
      femaleValues.Add("f");
      femaleValues.Add("female");

      List<string> maleValues = new();
      femaleValues.Add("m");
      femaleValues.Add("male");

      var genderOptions = new List<Option>(new Option[] {
        new Option("F", acceptedValues: femaleValues),
        new Option("M", acceptedValues: maleValues),
      });

      var chooseMode = new ChooseMode();
      var gender = chooseMode.Ask(genderOptions, isPrintOption: false, question: "Gender ? (F/M) ");

      Console.WriteLine(gender);
    }
  }

  // class InputMode
  // {
  //   public T Ask(string question)
  //   {
  //     Console.WriteLine(question);

  //     string input = Console.ReadLine();

  //     return input;
  //   }
  // }
}