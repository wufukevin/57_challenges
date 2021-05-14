using System.Collections.Generic;

namespace zoe_4_17
{
  public class BloodAlcoholCalculator
  {
    public double Weight, Hour, Volume;
    public string Gender;

    readonly Dictionary<string, double> AlcoholDistributionRatio = new()
    {
      { "M", 0.73 },
      { "F", 0.66 }
    };

    public BloodAlcoholCalculator(double weight, double hour, double volumn, string gender)
    {
      Weight = weight;
      Hour = hour;
      Gender = gender;
      Volume = volumn;
    }

    public double GetBloodAlcoholContent()
    {
      // BAC = (Volume × 5.14 / weight × alcoholDistributionRatio) − 0.015 × hours
      return (Volume * 5.14 / Weight * AlcoholDistributionRatio[Gender]) - 0.015 * Hour;
    }
  }
}