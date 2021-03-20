using System;

namespace zoe_3_8
{
    class Program
    {
        static void Main()
        {
            var actionQuestion = "please choose mode\n1) divide pizza\n2) purchase pizza";

            string action;
            do
            {
                action = askForInputString(actionQuestion);
            } while (action != "1" && action != "2");

            Boolean isDividePizzas = action == "1";

            if (isDividePizzas)
            {
                dividePizza();
            } else
            {
                purchasePizza();
            }
        }

        private static int askForInput(string question)
        {
            Console.Write(question);

            return Convert.ToInt32(Console.ReadLine());
        }

        private static string askForInputString(string question)
        {
            Console.Write(question);

            return Console.ReadLine();
        }
        
        private static string checkPluralNoun(string noun, int amount)
        {
            return amount > 1 ? $"{noun}s" : noun;
        }

        private static void dividePizza()
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

        private static void purchasePizza()
        {
            var peopleQuestion = "How many people?";
            var sliceQuestion = "How many slices each person wants?";

            int people;
            int slice;

            try
            {
                people = askForInput(peopleQuestion);
                slice = askForInput(sliceQuestion);
            }
            catch
            {
                Console.WriteLine("Cannot parse");
                return;
            }

            int totalSlice = people * slice;
            int slicePerPizza = 8;

            int pizza = (int)Math.Ceiling((double)totalSlice / (double)slicePerPizza);

            var answer = $"{people} people X {slice} {checkPluralNoun("piece", slice)} = {pizza} {checkPluralNoun("pizza", pizza)}";

            Console.WriteLine("");
            Console.WriteLine(answer);


        }
    }
}
