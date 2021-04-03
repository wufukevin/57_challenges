using System;
using zoe_3_9.ShapeSizes;

namespace zoe_3_9.ShapeCounters
{
  class RectangleCounter : IShapeCounter
  {

    public ShapeSize CheckSize()
    {
      double width;
      double length;

      try
      {
        width = ConsoleUtil.AskForInputDouble("What is the length of the room in feet? ");
        length = ConsoleUtil.AskForInputDouble("What is the width of the room in feet? ");
      }
      catch
      {
        Console.WriteLine("Cannot parse");
        throw;
      }

      return new WidthLengthSize()
      {
        Width = width,
        Length = length
      };
    }
    public double CountArea(ShapeSize shapeSize)
    {
      WidthLengthSize size;
      if (shapeSize is WidthLengthSize)
        size = (WidthLengthSize)shapeSize;
      else
        throw new ArgumentException("shapeSize s not a WidthLengthSize");

      return size.Width * size.Length;
    }
  }

}
