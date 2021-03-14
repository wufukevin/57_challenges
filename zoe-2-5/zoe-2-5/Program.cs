using System;
using System.Data;

namespace zoe_2_5
{
    class Program
    {
        static void Main()
        {
            int sum;
            int difference;
            int product;
            int quotient;
            string resultString = string.Empty;

            string number1Question = "What is the first number?";
            string number2Question = "What is the second number?";

            int number1;
            int number2;

            try { 
                number1 = askForInput(number1Question);
                number2 = askForInput(number2Question);
            }
            catch (FormatException)
            {
                Console.WriteLine("Unable to parse");
                return;
            }

            //sum = number1 + number2;
            //difference = number1 - number2;
            //product = number1 * number2;
            //quotient = number1 / number2;

            //resultString = $"{number1} + {number2} = {sum}\n{number1} - {number2} = {difference}\n{number1} * {number2} = {product}\n{number1} / {number2} = {quotient}";

            string numbers = $"{number1} + {number2}, {number1} - {number2}, {number1} * {number2}, {number1} / {number2}";
            string[] equations = numbers.Split(',');

            foreach (string equation in equations)
            {
                DataTable dt = new DataTable();
                object result = dt.Compute(equation, "");
                resultString += $"{equation} = {result} \n";
            }

            Console.WriteLine(resultString);
            
        }

        private static int askForInput(string question)
        {
            Console.Write(question);

            return Int32.Parse(Console.ReadLine());
        }
    }
}
