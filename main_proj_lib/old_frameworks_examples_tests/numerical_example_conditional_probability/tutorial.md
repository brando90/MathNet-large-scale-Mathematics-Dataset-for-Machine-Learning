In this document we will explain how to construct an example problem with the framework.

Consider the following probability problem:

> Mathphobia is a rare disease in which the victim has the delusion that he or she is being subjected to intense examination. A person with Mathphobia has shaky arm with probability 0.360095. A person selected uniformly at random has Mathphobia with probability 0.573072. A person without Mathphobia has shaky arm with probability 0.138142. What is the probability that a person selected uniformly at random has has Mathphobia, given that he or she has shaky arm?

The goal will be to create a problem class with the framework so that the problem can be generated with many variations (both different numbers and having some sentences be permutable).

The first thing we will do is create a function that generates the string for each of the sentences.

```
def intro_sent(g):
    sentence = '%s is a rare disease in which the victim has the delusion that he or she is being subjected to intense examination. '%(g.disease_name)
    return sentence

def prob_disease_sent(g):
    sentence = 'A person selected uniformly at random has %s with probability %f. '%(g.disease_name,g.p_f)
    return sentence

def prob_shaky_given_disease_sent(g):
    sentence = 'A person with %s has %s with probability %f. '%(g.disease_name,g.symptom,g.p_s_f)
    return sentence

def prob_shaky_given_no_disease_sent(g):
    sentence = 'A person without %s has %s with probability %f. '%(g.disease_name,g.symptom,g.p_s_nf)
    return sentence

def question(g):
    sentence = 'What is the probability that a person selected uniformly at random has has %s, given that he or she has %s? '%(g.disease_name,g.symptom)
    return sentence
```

notice that each function has the argument `g` passed to the function. This will be used to keep track of the global variables for your problem. With this you can create any variable that you wish to access. For example, the first sentence talks about a disease. The name of the disease will be tracked with the variable `g.disease_name` the framework will help you be able to generate various variations of the problem and having these things that vary as variables will help the framework know what it should vary instead of having the programmer hard code it.

To tell the framework which variables are global create functions that populate the global variables each time a problem is created:

```
def get_disease_names():
    diseases = ['CSphobia','Biophobia','Mathphobia'] #TODO: re-think
    #
    rand_i = random.randint(a=0,b=len(diseases)-1) # Return a random integer N such that a <= N <= b.
    disease_name = diseases[rand_i]
    return disease_name

def get_symptom_names():
    diseases = ['shaky arm','soft teeth','strident attitude'] #TODO: re-think
    #
    rand_i = random.randint(a=0,b=len(diseases)-1) # Return a random integer N such that a <= N <= b.
    disease_name = diseases[rand_i]
    return disease_name

def get_p_f():
    return random.uniform(a=0, b=1) # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

def get_p_s_f():
    return random.uniform(a=0, b=1) # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

def get_p_s_nf():
    return random.uniform(a=0, b=1) # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
```

Now create a dictionary that will eventually be passed to the problem framework which will tell which variables are global (i.e. reachable through `g.var_name`) with its corresponding functions that (ideally randomly) populate them (or populates them to give some degree of variety to the problems).

Now that we have the sentences and its variables, lets tell the framework which sentences from the ones we created can be permuted and which can not. Group the functions that are sequential (i.e. cannot be permuted) in an list and the ones that are permutable in its own list:

    # functions for generator
    first_seq_gen = [intro_sent]
    permutation_gen = [prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent]
    last_seq_gen = [question]

However, the framework doesn't know which are sequential or permutable sentences just from lists. Thus, wrap them in the Generator classes (sequential generator or permutation generator) to tell the framework what is allowed to permute and what now:

    first_seq_gen = SeqGen([intro_sent])
    permutation_gen = PerGen([prob_disease_sent,prob_shaky_given_disease_sent,prob_shaky_given_no_disease_sent])
    last_seq_gen = SeqGen([question])

Then don't forget to create a way to generate a solution to the problem! (notice that you will have to know how to generate solutions and have the framework output numerical ways to compute them). For this problem using standard probability rules the solution can be programmed to be:

```
def solution_creater(g):
    p_f = g.p_f
    p_s_f = g.p_s_f
    p_s_nf = g.p_s_nf
    p_nf = 1 - p_f
    # total probability rule p(s) = p(s|f)p(f) + p(s|~f)p(~f)
    p_s = p_s_f*p_f + p_s_nf*p_nf
    # bayes theorem p(f|s) = p(s|f)p(f) / p(s)
    p_f_s = (p_s_f * p_f)/p_s
    return p_f_s
```

Now that we have everything we can just pass everything to the `Problem` class framework:

    # create problem class to automatically generate varied questions/problems and answers/solution
    generators = [first_seq_gen,permutation_gen,last_seq_gen]
    problem = Problem(array_generators=generators,key_words_values=key_words_values,solution_creater=soln_creater)

Finally create one question and solution and make sure that the answer is what you expected (it might be useful to create something that doesn't vary once so that you know your problem and solutions are being generated correctly. i.e. unit test your code!):

    one_question = problem.generate_problem_statement()
    one_soln = problem.generate_solution()


To find this example all in one file go to:
