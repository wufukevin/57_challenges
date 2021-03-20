using System;

namespace zoe_3_8
{
    class Program
    {
        static void Main()
        {
            var peopleQuestion = "How many people?";
            var pizzaQuestion = "How many pizzas do you have?";

            int people;
            int pizza;
            try
            {
                do
                {
                    people = askForInput(peopleQuestion);
                } while (people <= 0);
                
                pizza = askForInput(pizzaQuestion);
            }
            catch
            {
                Console.WriteLine("Cannot parse");
                return;
            }

            int slicePerPizza = 8;
            int totalSlice = pizza * slicePerPizza;

            int slicePerPerson = totalSlice / people;
            int sliceLeftover = totalSlice % people;


            var answer = $"{people} people with {pizza} {checkPluralNoun("pizza", pizza)}\nEach person gets {slicePerPerson} {checkPluralNoun("piece", slicePerPerson)} of pizza.\nThere are {sliceLeftover} leftover {checkPluralNoun("piece", sliceLeftover)}.";

            Console.WriteLine(answer);
        }

        private static int askForInput(string question)
        {
            Console.Write(question);

            return Convert.ToInt32(Console.ReadLine());
        }

        private static string checkPluralNoun(string noun, int amount)
        {
            return amount > 1 ? $"{noun}s" : noun;
        }
    }
}
