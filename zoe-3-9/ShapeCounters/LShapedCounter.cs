using System;
using zoe_3_9.ShapeSizes;

namespace zoe_3_9.ShapeCounters
{
  class LShapedCounter : IShapeCounter
  {
    public ShapeSize CheckSize()
    {
      double outerWidth;
      double outerLenght;
      double innterWidth;
      double innterLenght;

      try
      {
        outerWidth = ConsoleUtil.AskForInputDouble("What is the length of the room in feet? ");
        outerLenght = ConsoleUtil.AskForInputDouble("What is the width of the room in feet? ");

        innterWidth = ConsoleUtil.AskForInputDouble("What is the inner width of the room in feet? ");
        innterLenght = ConsoleUtil.AskForInputDouble("What is the inner length of the room in feet? ");
      }
      catch
      {
        Console.WriteLine("Cannot parse");
        throw;
      }

      return new LShapeSize()
      {
        OuterWidth = outerWidth,
        OuterLenght = outerLenght,
        InnterWidth = innterWidth,
        InnterLenght = innterLenght
      };
    }
    public double CountArea(ShapeSize shapeSize)
    {
      LShapeSize size;
      if (shapeSize is LShapeSize)
        size = (LShapeSize)shapeSize;
      else
        throw new ArgumentException("shapeSize s not a LShapeSize");

      return (size.OuterWidth * size.OuterLenght) - (size.InnterWidth * size.InnterLenght);
    }
  }

}
