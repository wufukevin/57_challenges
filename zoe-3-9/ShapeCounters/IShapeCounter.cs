using zoe_3_9.ShapeSizes;

namespace zoe_3_9.ShapeCounters
{
  interface IShapeCounter
  {

    public ShapeSize CheckSize();
    public double CountArea(ShapeSize shapeSize);
    public double getArea()
    {
      ShapeSize shapeSize = CheckSize();

      double area = CountArea(shapeSize);

      return area;
    }
  }

}
