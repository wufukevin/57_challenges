using System;
using System.Collections.Generic;

namespace zoe_4_17
{

  class BloodAlcoholCalculator
  {
    private readonly double LegalLimit = 0.08;

    public double BAC;
    public bool IsOverLimit;

    readonly Dictionary<string, double> AlcoholDistributionRatio = new()
    {
      { "men", 0.73 },
      { "women", 0.66 }
    };

    public BloodAlcoholCalculator SetInfo(BloodAlcoholCalculatorParam param)
    {
      BAC = GetBAC(param.Weight, param.Hour, param.Volumn, param.Gender);
      IsOverLimit = BAC >= LegalLimit;

      return this;
    }

    private double GetBAC(double weight, double hour, double volumn, string gender)
    {
      // BAC = (Volume × 5.14 / weight × alcoholDistributionRatio) − 0.015 × hours
      return (volumn * 5.14 / weight * AlcoholDistributionRatio[gender]) - 0.015 * hour;
    }
  }
}