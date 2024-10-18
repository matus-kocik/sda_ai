Organising Operations (Python)

Open repository
More options
Waiting for review
Ratings (13)
Difficulty:
3.2
Usefulness:
3.5
Fun:
3.2
Materials:
3.8
Duration:
 76 min
This is a guided project
To learn the most, try and implement it on your own first, and check the solution only when you feel necessary. However, if you feel completely stuck, feel free to check the step-by-step solution guide
You've already grasped the fundamentals of data structures and basic logical operations. Yet, another essential coding concept awaits: functions.

Functions simplify coding by grouping operations, allowing for code reuse with varying data. Consider a basic addition example:

a = 3
b = 4
result = a + b
To add different numbers, you'd typically rewrite these lines:

c = 9
d = 7
another_result = c + d
With functions, the process is streamlined:

def add(a, b):
    return a + b

result = add(3, 4)
another_result = add(9, 7)
Next, you'll explore various function aspects and their applications.

Tasks
SHOW ALL CRITERIA
Simple function
First, let's examine a simple function that utilizes an external variable:

Create a this_text variable with a string value. Then, define a function named log_into_terminal that prints this variable's value to the terminal. Remember to invoke log_into_terminal.

A global variable this_text is displayed in the terminal by the log_into_terminal function.

CRITERIA
Local variables
Now, work with local variables, defined within functions. Inside log_into_terminal, declare a local_text variable and display it. Note: Local variables cannot be accessed outside their function.

A local variable local_text inside log_into_terminal is shown in the terminal.

CRITERIA
Multiple functions
Functions can invoke other functions. Define a new function another_function that calls log_into_terminal.

another_function triggers log_into_terminal, which then prints this_text and local_text to the terminal.

CRITERIA
Assign a function
Functions can be assigned to variables. Define a variable third_function as a function that also calls log_into_terminal. Execute third_function.

third_function calls log_into_terminal, displaying this_text and local_text in the terminal.

CRITERIA
Funception
Define a function within log_into_terminal. Name it fourth_function and have it log a string. Call fourth_function within log_into_terminal.

fourth_function is defined and executed inside log_into_terminal.

CRITERIA
Arguments and Parameters
Pass data into log_into_terminal from another_function. Inside log_into_terminal, log this passed-in data.

log_into_terminal receives and prints a string argument from another_function.

CRITERIA
Undefined
You might see undefined in the terminal. Provide arguments to all calls of log_into_terminal to fix this.

Every call to log_into_terminal includes an argument.

CRITERIA
Multiple arguments
Enhance log_into_terminal to accept and display a second parameter. Define variables before each call to log_into_terminal, passing these as arguments.

log_into_terminal now accepts a second parameter, second_to_log.

Each log_into_terminal invocation includes a second argument.

Different variables are passed as the second argument in each log_into_terminal call.

CRITERIA
The big return
Create a greetings function that returns a greeting string using the passed-in name. Call greetings within console.log() five times, each with a different name.

greetings is invoked five times, each call passing a unique name and returning a personalized greeting.

CRITERIA


