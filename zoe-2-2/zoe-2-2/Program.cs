using System;

namespace zoe_2_2
{
    class Program
    {
        static void Main(string[] args)
        {
            string question = "What is the input string?";

            Console.WriteLine(question);

            string inputString = Console.ReadLine();

            string resultString = $"{inputString} has {inputString.Length} characters.";

            Console.WriteLine(resultString);

        }
    }
}
