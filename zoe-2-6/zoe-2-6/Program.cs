using System;

namespace zoe_2_6
{
    class Program
    {
        static void Main()
        {
            string ageQuestion = "What is your current age ?";
            string retirementAgeQuestion = "At what age would you like to retire ?";

            int age;
            int retirementAge;

            try
            {
                age = askForInput(ageQuestion);
                retirementAge = askForInput(retirementAgeQuestion);
            }
            catch
            {
                Console.WriteLine("Cannot parse");
                return;
            }

            DateTime localDate = DateTime.Now;

            int thisYear = localDate.Year;
            int remainingYear = retirementAge - age;
            int retirementYear = thisYear + remainingYear;

            if(remainingYear <= 0)
            {
                Console.WriteLine("Wow! you have been retired!");
            }
            else
            { 
                string answer = $"You have {remainingYear} years left until you can retire.\nIt's {thisYear}, so you can retire in {retirementYear}.";

                Console.WriteLine(answer);
            }
        }

        private static int askForInput(string question)
        {
            Console.Write(question);

            return Int32.Parse(Console.ReadLine());
        }
    }
}
