using System;

namespace zoe_2_1
{
    class Program
    {
        static void Main(string[] args)
        {
            string welcomeWord = "What is your name?";

            Console.WriteLine(welcomeWord);

            string userName = Console.ReadLine();

            string greetingWord = $"Hello, {userName}, nice to meet you!";


            // Challenge 1
            //string greetingWord = $"Hello, {Console.ReadLine()}, nice to meet you!";

            Console.WriteLine(greetingWord);

        }
    }
}
