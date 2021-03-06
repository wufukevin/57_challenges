using System;

namespace zoe_2_3
{
    class Program
    {
        static void Main(string[] args)
        {
            string quoteQuestion = "What is the quote ?";

            string quote = askAndAnswer(quoteQuestion);

            string manQuestion = "Who said it ?";

            string man = askAndAnswer(manQuestion);


            string result = $"{man} says, \"{quote}\"";

            Console.WriteLine(result);

        }

        private static string askAndAnswer(string question)
        {
            Console.WriteLine(question);

            string answer = Console.ReadLine();

            return answer;
        }
    }
}
