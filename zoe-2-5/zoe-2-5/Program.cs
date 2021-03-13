using System;
using System.Data;

namespace zoe_2_5
{
    class Program
    {
        static void Main(string[] args)
        {
            string sum;
            string difference;
            string product;
            string quotient;
            string resultString = string.Empty;

            string number1Question = "What is the first number?";
            string number2Question = "What is the second number?";

            int number1 = askForInput(number1Question);
            int number2 = askForInput(number2Question);

            sum = Convert.ToString(number1 + number2);
            difference = Convert.ToString(number1 - number2);
            product = Convert.ToString(number1 * number2);
            quotient = Convert.ToString(number1 / number2);

            resultString = $"{number1} + {number2} = {sum}\n{number1} - {number2} = {difference}\n{number1} * {number2} = {product}\n{number1} / {number2} = {quotient}";


            //string numbers = $"{number1} + {number2}, {number1} - {number2}, {number1} * {number2}, {number1} / {number2}";
            //string[] equations = numbers.Split(',');

            //foreach(string equation in equations)
            //{
            //    Console.WriteLine(equation);
            //    DataTable dt = new DataTable();
            //    object result = dt.Compute(equation, "");
            //    resultString += $"{equation} = {result} \n";
            //}

            Console.WriteLine(resultString);



        }

        private static int askForInput(string question)
        {
            int number = 0;

            Console.Write(question);

            string input = Console.ReadLine();

            try
            {
                number = Int32.Parse(input);
            }
            catch (FormatException)
            {
                Console.WriteLine($"Unable to parse '{input}'");
            }

            return number;
        }

    }
}
