using System;

namespace zoe_4_19
{
  class Program
  {
    static void Main()
    {
      // chois unit system
      var ruleDescription = BMICalculator.ListSupportSystem();

      Console.WriteLine(ruleDescription);

      var unitSystem = String.Empty;

      do
      {
        Console.Write("please choise: ");
        unitSystem = Console.ReadLine();
      } while (!BMICalculator.ExitSystem(unitSystem));

      // input information
      Console.Write("your height is: ");
      var height = Convert.ToDouble(Console.ReadLine());

       Console.Write("your weight is: ");
      var weight = Convert.ToDouble(Console.ReadLine());

      
      // 1.6 47 ~ 62 under weight
      BMICalculator.Run(height, weight, unitSystem);
    }
  }

  class BMICalculator
  {
    public enum UnitSystemEnum
    {
      Metric,
      Imperial
    }

    public static string ListSupportSystem()
    {
      var unitSystems = Enum.GetNames(typeof(UnitSystemEnum));

      var index = 0;

      var description = String.Empty;

      Array.ForEach(unitSystems, system =>
      {
        Console.WriteLine(system);
        description += $"{index}) {system} \n";
        index++;
      });

      return description;
    }

    public static bool ExitSystem(string index){
        var allSystem = Enum.GetValues(typeof(UnitSystemEnum));

        var isExit = false;

        foreach (int i in allSystem)
        {
          if(i.ToString() == index){
            isExit = true;
            break;
          }
        }

        // Array.Exists(allSystem, (value) => {
        //   return true;
        // });

        return isExit;
    }
    public static void Run(double height, double weight, string unitSystem)
    {
      var unitRatio = UnitSystemEnum.Metric.ToString() == unitSystem ? 703 :1;
      var BMI = weight / Math.Pow(height, 2) * unitRatio;
      var result = String.Empty;

      // underWeight
      if (BMI < 18.5)
      {
        result = "You are underweight. You should see your doctor.";
      }
      // normal
      else if (BMI < 24)
      {
        result = "You are within the ideal weight range.";
      }
      //overWeight
      else
      {
        result = "You are overweight. You should see your doctor.";
      }

      Console.WriteLine(result);
    }
  }
}
