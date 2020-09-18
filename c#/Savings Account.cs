using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*
Brian Shukwit
Savings Account Program
*/

namespace programAssignmen4_brianShukwit
{
	// Create Savings Account class
    public class SavingsAccount
    {
        private static double annualInterestRate;
        private double savingsBalance;
        static double holder = 0
		
		// User enters name for account
		Console.WriteLine("Enter Account Name: ");
		string savingsAccountName = Console.ReadLine();

        protected SavingsAccount()
        {
            savingsBalance = 0;
            annualInterestRate = 0;

        }

        public SavingsAccount(double balance)
        {
            savingsBalance = balance;
            annualInterestRate = 0;
        }
	// print out information
        public void calculateMonthlyInterest()
        {
            Console.WriteLine("Current savings balance: " + savingsBalance "for account: " + savingsAccountName);
            double monthlyInterest;
            monthlyInterest = (savingsBalance * annualInterestRate) / 12;
            savingsBalance += monthlyInterest;
            Console.WriteLine("New savings balance: " + savingsBalance "for account: " + savingsAccountName);
        }

        protected double getBalance()
        {
            return savingsBalance;
        }

        protected void setHolder()
        {
            holder = savingsBalance;
        }

        protected static double retHolder()
        {
            return holder;
        }

        public void modifyInterestRate(double newInterestRate)
        {
            annualInterestRate = newInterestRate;
        }
    }
 public class SpecialSavings : SavingsAccount
{
        protected void modifyInterestRate()
    {
        if (SavingsAccount.retHolder()>10000)
        {
            modifyInterestRate(.1);
        }
    }
}
    // Create Program Class for Savers.
    class Program
    {
        static void Main(string[] args)
        {
            SavingsAccount saver1 = new SavingsAccount(2000);
            SavingsAccount saver2 = new SavingsAccount(3000);

            saver1.modifyInterestRate(.04);
            saver1.calculateMonthlyInterest();
			Console.WriteLine(saver1);	
			
            saver2.modifyInterestRate(.04);
            saver2.calculateMonthlyInterest();
			Console.WriteLine(saver2);

            saver1.modifyInterestRate(.05);
            saver1.calculateMonthlyInterest();
			Console.WriteLine(saver1);
			
            saver2.modifyInterestRate(.05);
            saver2.calculateMonthlyInterest();
			Console.WriteLine(saver2);
        }
    }
}