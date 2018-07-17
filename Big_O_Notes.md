# Big O
- alias for time complexity
- in addition to time complexity there is space complexity

Even though the term is called time complexity, the term has very little to do with real time.

* an objective way to measure different functions or programs. 
* a methodology figuring out some sort of classification for programs or functions or things of that nature.

Big O does have roots in Math. 

------
These are the main Big O time complexity:

`O(1)`
* constant time
    - entirely independent of any sort of input

    ```
    def print_first_item(items):
        print(items[0])
    ```
    - we talk about complexity in relation to the size of the input. Because this is hard-coded to look for `items[0]`, it will take the same amount of time no matter what....and no matter how large the `list` or `array` is.
    - this particular function or operation is completely independent of the size of the input. No dependence at all on the size of the `list` or `array`
    - this is the outlier. Every other one has reliance how much input we have3 3 3 


`O(n)`
* linear time
    - it does have a dependence on the size of the input

    ```
    def print_all_items(items):
        for item in items:
            print(item)
    ```
    - if we increase the number of items in the input, the number of operations (the number of times that the for loop runs `here` for instance) that needs to be done increases with each additional item that's added to the input. 
    
    `100 items == 100 operations`
    
    `25 items == 25 operations` ...etc

    - It's not concerned with real time. Forget about time complexity dealing with real time. It has everything to do with the number of operations that is performed. 



`O(nˆ2)`
* Quadratic time

    - number of operations is squared when we do nested loops
    ```
    items = [1, 2, 3]
    def print_all_possible_ordered_pairs(items):
        for first_item in items:
            for second items in items:
                print(first_item, second_item)

    ```
    Here we are nesting two loops. If out list has `n` items, our outer loop runs `n` times. Our inner loop runs `n times for each iteration of the outer loop`, giving us `n^2` total prints.

    If the list has ten items, we have to print 100 times. If it has 1,000 items, we have to print 1,000,000 times


`O(log n)`
* logarithimic time


#### ** `n` could be the actual input, or the size of the input**

Both of these functions have O(n) runtime, even though one takes an integer as its input and the other takes a list:

```
def say_hi_n_times(n):
    for time in xrange(n):
        print("Hi")

def print_all_items(items):
    for item in items:
        print(item)
```

So sometimes `n` is an actual number that's an input to our function, and other times `n` is the number of items in an input list (or an input map, or an input object, etc.).

----
### Drop the constants
When you're calculating the big O complexity of something, you just throw out the contants. So if something is `O(2n)`, it's just considered `O(n)`

```
def print_all_the_items_twice(items):
    for item in items:
        print(item)

    #once more with feeling!!

    for item in items:
        print(item)
```
This is O(2n)...which we just consider O(n)

```
def print_first_time_then_first_half_then_say_hi_100_times(items):
    print(items[0])  
    *** O(1) constant time ***

    middle_index = len(items)/2 (length is still constant time)
    index = 0
    while index < middle_index: 
    ***O(n/2)....O(n)...coefficients don't matter here***
        print(items[index])
        index +=1

    for time in xrange(100): 
        ***O(100)...again coefficients don't matter.... O(1)***
        print("hi!")

```

**O(1 + n/2 + 100)....just O(n)**
- Why can we get away with this? Remember, for big O notation we're looking at what happens as n gets arbitrarily large. As n gets really big, adding 100 or dividing by 2 has a decreasingly significant effect.
----
## O(log n)
* what does logarithim even mean?
    - Here's what a logarithim is asking:
        - "What power must we raise this base to in order to get this answer?"
    
    so if we say `log(10) 100`

    the 10 is called the base(makes sense - it's on the bottom). Think of the 100 as the "answer".
    It's what we are taking the log `of`. So this expression would be "log base 10 of 100"

    And all it means is, "What power do we need to tause this base(10) to, to get this answer(100)?

    10ˆx = 100

    What `x` gets us our result of 100? 

    √10ˆx = √100

    x = 2



* What are logarithims used for?
    - The main thing we use logarithims for is **solving for x when x is an exponent**
    - So if we wanted to solve this:

```10^x = 100 

We need to bring the x down from the exponent somehow. And logarithms give us a trick for doing that.

We take the log​10
​​  of both sides (we can do this—the two sides of the equation are still equal):

log(10)10^x = log(10)100 

Now the left-hand side is asking, "what power must we raise 10 to in order to get 10^x​ ?" The answer, of course, is xx. So we can simplify that whole left side to just "x":

x = log(10)100 

We've pulled the x down from the exponent!

Now we just have to evaluate the right side. What power do we have to raise 10 to do get 100? 
The answer is still 2.

x = 2 
That's how we use logarithms to pull a variable down from an exponent
```
