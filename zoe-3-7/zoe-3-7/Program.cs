using System;

namespace zoe_3_7
{
    class Program
    {
        static void Main()
        {
            var versionQuestion = "please choose convertion mode\n1) feet to meter\n2) meter to feet";

            string conversionMode;
            do
            {
                conversionMode = askForInputString(versionQuestion);
            } while (conversionMode != "1" && conversionMode != "2");

            Boolean isInputFeet = conversionMode == "1";
            string inputUnit = isInputFeet ? "feet" : "meter";
            string outputUnit = isInputFeet ? "meter" : "feet";
            double feetToMeterRatio = 0.09290304;
            double conversionRatio = Math.Pow(feetToMeterRatio, isInputFeet ? 1 : -1);

            calculateArea(inputUnit, outputUnit, conversionRatio);
        }

        private static double askForInputNumber(string question)
        {
            Console.Write(question);

            return Convert.ToDouble(Console.ReadLine());
        }

        private static string askForInputString(string question)
        {
            Console.Write(question);

            return Console.ReadLine();
        }

        private static void calculateArea(string inputUnit, string outputUnit, double conversionRatio)
        {
            var lengthQuestion = $"What is the length of the room in {inputUnit} ?";
            var widthQuestion = $"What is the width of the room in {inputUnit} ?";

            double length;
            double width;
            
            try
            {
                length = askForInputNumber(lengthQuestion);
                width = askForInputNumber(widthQuestion);
            }
            catch
            {
                Console.WriteLine("Cannot parse");
                return;
            }

            var area = length * width;
            var areaConvertTo = Math.Round(area * conversionRatio, 3);

            var answer = $"You entered dimensions of {length} {inputUnit} by {width} {inputUnit}.\nThe area is\n{area} square {inputUnit}\n{areaConvertTo} square {outputUnit}";

            Console.WriteLine(answer);
        }
    }
}
