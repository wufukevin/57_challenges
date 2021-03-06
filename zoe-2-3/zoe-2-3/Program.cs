using System;

namespace zoe_2_3
{
    class Program
    {
        static void Main(string[] args)
        {
            string quoteQuestion = "What is the quote ?";

            string quote = askForInput(quoteQuestion);

            string speakerQuestion = "Who said it ?";

            string speaker = askForInput(speakerQuestion);


            Console.WriteLine($"{speaker} says, \"{quote}\"");

        }

        private static string askForInput(string question)
        {
            Console.Write(question);

            return Console.ReadLine();
        }
    }
}
