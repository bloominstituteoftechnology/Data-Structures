Analysis of Algorithms
Exercise I: Give an analysis of the running time of each snippet of pseudocode with respect to the input size n of each of the following:

a)  a = 0
    while (a < n * n * n) 
      a = a + n * n

 - 0(n)
b)  sum = 0
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++

 - O(n^4)

c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
  -  0(1)
Exercise II: Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped eggs is minimized.
- implement binary search - O(log n)