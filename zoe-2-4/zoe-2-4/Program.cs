using System;

namespace zoe_2_4
{
    class Program
    {
        static void Main(string[] args)
        {
            string nounQuestion = "Enter a noun:";
            string verbQuestion = "Enter a verb:";
            string adjectiveQuestion = "Enter a adjective:";
            string adverbQuestion = "Enter a adverb:";

            string noun = askForInput(nounQuestion);
            string verb = askForInput(verbQuestion);
            string adjective = askForInput(adjectiveQuestion);
            string adverb = askForInput(adverbQuestion);

            string sentence = $"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!";

            Console.Write(sentence);

        }

        private static string askForInput(string question)
        {
            Console.Write(question);

            return Console.ReadLine();
        }

    }
}
