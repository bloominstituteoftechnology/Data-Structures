# Runtime Complexity

commands = ['n', 's', 'e', 'w']

# Runtime Complexity: A way to objectively compare the efficiency
# of two alogorithm's approaches

# Complexity Classes:
    # Constant Time: This is the most efficient run time.
        # the efficiency of the code does not depend on the size of the input.
        # Example of constant time operation:,
commands[3]
            # Doesn't matter if there are 4 elements or 100, this happens just as quickly.
            # this operation has an efficiency which doesnt depend on the size of the input.
            # constant time efficiency doesn't grow at all because it is not dependent on input size

    # Linear Time: The efficiency of the code does depend on the size of input.
    # example:
for command in commands:
    print(command)
        # This operation has a linear relation to the size of the input.
        # as the input grows, the number of operations grows in a linear proportion,
        # thus decreasing efficiency. As the input grows, the runtime grows in a linear relation.
        # for loops efficiency absolutely dependant on the input

        # Constant is less complex than Linear
        # Constant < Linear in terms of complexity

        # What's being compared is how quickly the efficiency grows as a result of the input size
        
        # The number of for loop iterations grows in proportion to input size in a linear fashion.

# Big O Notation:
    # Constant Time : O(1) - the efficiency doesnt depend on the size of the input
    # Linear Time : O(n) - The efficiency does depend on the size of the input

# Define Efficiency:
    # The purpose of Big O is separate from time. You can actually measure code 
    # based on time, but that's different than Big O and efficiency. These different 
    # ways of measurement are complimentary but different. Time based measurements have
    # a lot to do with hardware differences. Efficiency is the mathematical difference
    # of complexity within the code. Runtime is abstract and mathematical because it aims
    # to discount all of the hardware limitations as much as possible . We're working to
    # examine the algorithm itsself. Examining just the code itsself is a contrast from
    # timing the code on some physical hardware. The way Sean Chen puts it... 
        #-"Each iteration is an operation. If we are counting number of operations, we can
        # divorce that concept from the idea of time. The thing that runtime complexity measures
        #  is the number of operations a computer has to chew through as the input size grows. 
        #  Maximum efficiency is when the computer does not increase in operation size at all
        # regardless of input size. This maximum efficiency scenario can be examined through 
        # constant time"

# Note: As far as calculating big O , we are allowed to drop constants.
# This is because we only care about the "dominating" contributor to growth.
# In other terms, the "dominating" factor. This is referring to the highest found factor of N.

# S.C -"Big O is not real math."

# Big O ("order of") - Big O is worst case situation that the algorithm in examination deals with

# Big Theta - Average Case

# Big Omega - Best Case

# We typically work with big O because worst case is easier to target and work with.

