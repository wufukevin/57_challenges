using System;
using System.Collections.Generic;
namespace zoe_4_17
{
  class Option
  {
    public string Name;
    public string Value;
    public bool IsStrict;
    public List<string> AcceptedValues;

    public Option(string name, string value = null, List<string> acceptedValues = null)
    {
      Name = name;
      Value = value ?? name;
      IsStrict = acceptedValues == null;
      AcceptedValues = acceptedValues ?? new List<string>();
    }
  }
}