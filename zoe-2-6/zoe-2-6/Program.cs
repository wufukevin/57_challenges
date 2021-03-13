using System;

namespace zoe_2_6
{
    class Program
    {
        static void Main()
        {
            string ageQuestion = "What is your current age ?";
            string retirementAgeQuestion = "At what age would you like to retire ?";

            int age = askForInput(ageQuestion);
            int retirementAge = askForInput(retirementAgeQuestion);

            DateTime localDate = DateTime.Now;

            int thisYear = localDate.Year;
            int remainingYear = retirementAge - age;
            int retirementYear = thisYear + remainingYear;

            
            if(age >= retirementAge)
            {
                Console.WriteLine("Wow! you have been retired!");
            } else { 

                string answer = $"You have {remainingYear} years left until you can retire.\nIt's {thisYear}, so you can retire in {retirementYear}.";

                Console.WriteLine(answer);

            }
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
