namespace zoe_3_8.PizzaCounters
{
  public interface IPizzaCounter
  {
    const int slicePerPizza = 8;
    void GetOrder();
    void Counting();
    void Print();

    void ServingClient()
    {
      GetOrder();
      Counting();
      Print();
    }
  }
}
