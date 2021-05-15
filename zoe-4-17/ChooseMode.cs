using System;
using System.Collections.Generic;

namespace zoe_4_17
{
  class ChooseMode
  {
    private static List<Option> Options;

    public static string  Ask(List<Option> options, string question = "please choise: ", bool isPrintOption = true)
    {
      Options = options;

      if (isPrintOption)
      {
        PrintOptions();
      }

      return InputToChoose(question);
    }

    public static string GetSelecectOptionValue(string inputValue)
    {

      try
      {
        return Options.Find(option =>
          {
            if (option.IsStrict)
            {
              return inputValue.ToLower() == option.Value.ToLower();
            }
            else
            {
              return option.AcceptedValues.Exists(acceptedValue => acceptedValue.ToLower() == inputValue.ToLower());
            }
          }).Value;
      }
      catch
      {
        return null;
      }
    }

    public static string InputToChoose(string question)
    {
      string inputValue;
      string? value;

      do
      {
        Console.Write(question);
        inputValue = Console.ReadLine();
        value = GetSelecectOptionValue(inputValue);
      } while (value == null);

      return value;
    }

    // hint: use List no more Array
    static void PrintOptions()
    {
      Options.ForEach(option =>
      {
        Console.WriteLine($"{option.Value}) {option.Name}");
      });
    }
  }
}