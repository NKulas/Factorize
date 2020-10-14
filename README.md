# Factorize

The goal of this project is just some experimenting with ways to factor numbers.

The BruteForce file tries every possible factor.
The TensBruteForce file determines what numbers the last digit of the factor must be based on the last digit of the number. This means that only every tenth number must be tried.
The HundredsBruteForce file extends this by using the last two digits and tries only every hundreth number. It can not find single digit factors. Interestingly, I have noticed that the decrease in operation from tens is not very significant. 
The StepUpBruteForce file futher extends what I am doing with tens and hundreds. In the first round, one digit is used to detremine the possible last digits of each factor. In the next round two digits are used, and so on. 
The Diophantine file is for working with Diophantine equations. It may become part of another factoring method that I am still working on.
