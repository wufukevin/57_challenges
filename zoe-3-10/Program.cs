using System;
using System.Collections.Generic;

namespace zoe_3_10
{
  partial class Program
  {
    static void Main()
    {
      // repeat 3 times
      int times = 1;
      List<ProductDetail> allProduct = new();

      do
      {
        allProduct.Add(ScanProduct(times));
        times++;
      } while (times < 4);


      PrintReciept(allProduct);
    }

    public static ProductDetail ScanProduct(int index)
    {
      var priceQuestion = $"Enter the price: ";
      var quantityQuestion = $"Enter the quantity: ";

      Console.WriteLine($"------ item {index} ------");
      var price = ConsoleUtil.AskForInputDouble(priceQuestion);
      var quantity = ConsoleUtil.AskForInputDouble(quantityQuestion);

      return new ProductDetail()
      {
        Price = price,
        Quantity = quantity
      };
    }

    public static void PrintReciept(List<ProductDetail> allProduct)
    {
      double taxRate = 5.5;
      double subTotal = 0.0;

      foreach (var prodcut in allProduct)
      {
        subTotal += prodcut.Price * prodcut.Quantity;
      }

      double tax = subTotal * taxRate * 0.01;

      double Total = subTotal + tax;

      ConsoleUtil.ConsoleAnswer($"Subtotal: ${subTotal}");
      ConsoleUtil.ConsoleAnswer($"Tax: ${tax}");
      ConsoleUtil.ConsoleAnswer($"Total: ${Total}");
    }
  }
}
