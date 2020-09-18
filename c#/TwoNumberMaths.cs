using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProgramAssign1_BrianShukwit
{
    class Program
    {
        static void Main(string[] args)
        {
            
{
                int first, second, add, difference, product;
                float quotent, modulus;

                Console.WriteLine("Enter two integers\n");
                first = Convert.ToInt32(Console.ReadLine());
                second = Convert.ToInt32(Console.ReadLine());


                add = first + second;
                difference = first - second;
                product = first * second;
                quotent = first / (float)second;
                modulus = first % second;

                Console.WriteLine("The Sum of the two numbers is {0}\n", add);
                Console.WriteLine("The Difference of the two numbers is {0}\n", difference);
                Console.WriteLine("The Multiplication of the two numbers is {0}\n", product);
                Console.WriteLine("The Division of the two numbers is {0}.2f\n", quotent);
                Console.WriteLine("The Remainder of the two numbers is {0}\n", modulus);

                if (first < second)
                    Console.WriteLine("{0} is less than {1}\n", first, second);

                if (first == second)
                    Console.WriteLine("{0} is equal to {1}\n", first, second);

                if (first > second)
                    Console.WriteLine("{0} is greater than {1}\n", first, second);


                Console.WriteLine("Press Enter to Continue");
                Console.ReadLine();
            }


        }
        }
    }

