## Lambda function equivalent to 
# Anonymous functions
# Lambda functions
# Lambda expressions
# Lambda abstractions
# Lambda form
# Function literals

def increment(x):
    return x+1

# single argument lambda, 
# lambda bound_var:body
incr_lambda = lambda x:x+1
print(incr_lambda(2))


# multiargument lambda
greetings = lambda first, second: print("Hi {} and {}".format(first, second))
greetings("Rifat", "masud")

# immediatly invoked function expression (iffy)
# format (lambda_func) (passed_value/s)
retval = (lambda x: x**x) (3)
print(retval)


# example -> lambda sort
lambda_sort = lambda unsorted:sorted(unsorted)
var= lambda_sort([42,3,23,2,1,1])
print(var)