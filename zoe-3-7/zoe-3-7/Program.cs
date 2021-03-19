using System;

namespace zoe_3_7
{
    class Program
    {
        static void Main(string[] args)
        {
            var lengthQuestion = "What is the length of the room in feet ?";
            var widthQuestion = "What is the width of the room in feet ?";

            double length;
            double width;

            double conversionRatio = 0.09290304;

            try
            {
                length = askForInput(lengthQuestion);
                width = askForInput(widthQuestion);
            }
            catch
            {
                Console.WriteLine("Cannot parse");
                return;
            }

            var areaInFeet = length * width;
            var areaInMeter = Math.Round(areaInFeet * conversionRatio, 3);

            var answer = $"You entered dimensions of {length} feet by {width} feet.\nThe area is\n{areaInFeet} square feet\n{areaInMeter} square meters";

            Console.WriteLine(answer);
        }

        private static double askForInput(string question)
        {
            Console.Write(question);

            return Convert.ToDouble(Console.ReadLine());
        }
    }
}
