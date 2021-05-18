using System;
using System.Collections.Generic;
namespace zoe_4_17
{
  class Program
  {
    static void Main()
    {
      List<string> femaleValues = new();
      femaleValues.Add("men");
      femaleValues.Add("M");

      List<string> maleValues = new();
      femaleValues.Add("Women");
      femaleValues.Add("W");

      var genderOptions = new List<Option>(new Option[] {
        new Option("men", acceptedValues: femaleValues),
        new Option("women", acceptedValues: maleValues),
      });

      // TODO:
      // var weight = Input.Ask("weight? ").AddRule<double>(value => value > 0).ToDouble().start();
      // lazy computation
      // Builder  

      var weight = Utils.AskForInputDouble("weight = ");
      var gender = ChooseMode.Ask(genderOptions, isPrintOption: false, question: "Gender ? (men/women) ");
      var volumn = Utils.AskForInputDouble("volumn = ");
      var hour = Utils.AskForInputDouble("hour = ");

      BloodAlcoholCalculator Calculator = new();

      var param = new BloodAlcoholCalculatorParam()
      {
        Weight = weight,
        Hour = hour,
        Volumn = volumn,
        Gender = gender
      };

      var UserBAC = Calculator.SetInfo(param);

      var BAC = UserBAC.BAC;
      var IsOverLimit = UserBAC.IsOverLimit;
      var safeMassage = "It is legal for you to drive.";
      var warningMessage = "It is not legal for you to drive.";

      Console.WriteLine($"Yout BAC is {BAC}.");
      Console.WriteLine(IsOverLimit ? warningMessage  : safeMassage);
    }
  }

  
}