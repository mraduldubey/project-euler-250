# "Super" Experiment over the original problem
Code: [src/problem-002/problem-002-super.py](problem-002-experiment-code)
Funny stuff happened. 
I was trying to compare the performace of the original code & there problem limit of 4 Million was too low to get reasonable performance values. 
So, I tweaked the problem to be in terms of number of fib numbers instead.
The performance of both approaches in any sense of real world is perfect.
But, theoratically, I believe the mathematical approach was more efficient for the original problem.

Having said, a programmer can not rely on the mathematical approach for the following reasons:
1. We run out of precision for decent machines: 
   1. decimal.getcontext().prec yeiled 28 on my machine, while the max value can be 999999999999999999
2. So, I went ahead and used float values, but the precision error started accumulating and results in a incorrect answer. 
```
> python .\problem-002.py
DP Solution
 Real time: 0.0001617000 seconds
 CPU time: 0.0000000000 seconds

148962109254071680168441409990815950457836565271909879516389086720268361095244452260017254081923172769527548266942971621407489234521415208793130179723057622817334196605096178709616914155239613991163034834334126
----------------
Mathematical Solution
 Real time: -0.0002483001 seconds
 CPU time: 0.0000000000 seconds

148962109263169798384784866638946023883647467803016243638511791548510821724322997410047974404431366141113947810101597398326787311490622832015231199990016924881013460098549050318075252088367679191536593723719680.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
----------------
```

# Conclusion (for now)

**One can use the mathematical approach till 50th fibonnaci number safely (aka 12586269025). This number can very well be machine dependent.**

**I am sure there is more to dig here, both in Python & computer orgamization & precision etc.**


Go crazy.