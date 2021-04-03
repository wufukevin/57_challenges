using System;
using zoe_3_9.ShapeSizes;

namespace zoe_3_9.ShapeCounters
{
  class RoundCounter : IShapeCounter
  {
    public ShapeSize CheckSize()
    {
      double radius;

      try
      {
        radius = ConsoleUtil.AskForInputDouble("What is the radius of the room in feet? ");
      }
      catch
      {
        Console.WriteLine("Cannot parse");
        throw;
      }

      return new RadiusSize()
      {
        Radius = radius,
      };
    }
    public double CountArea(ShapeSize shapeSize)
    {
      RadiusSize size;
      if (shapeSize is RadiusSize)
        size = (RadiusSize)shapeSize;
      else
        throw new ArgumentException("shapeSize s not a RadiusSize");

      return Math.PI * size.Radius * size.Radius;
    }
  }

}
