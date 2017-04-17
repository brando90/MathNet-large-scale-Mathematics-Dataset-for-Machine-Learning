We will expand on the examples on tutorial: https://github.com/brando90/eit_proj1/wiki/Tutorial-1:-Simple-example-for-QA-generation

We want to be able to solve the same question even the variables or numerical values change. There might even be equivalent mathematical expressions for an answer, so we want to be able to provide that variety. For that we will use an assignment dictionary that will tell our QA generator what it should substitute and for what.

Recall the previous question:

> solve x, a = b, x = 2b, a = 8, can you do it?

>x = 28 = 16

what if we want different variables and numerical values?

For that we can create some sympy variables:

    x,y,a,b, X = symbols('x y a b X')
    e,f,g,h = symbols('e f g h')

then we create the question as in the old example but use the sympy symbols:

    question = seqg(seqg('solve ',x,', '), seqg( seqg(Eq(a,b),', ') , seqg(Eq(x,2*b),', ') , seqg(Eq(a,8),', ') ), 'can you do it?')

Now that we have symbols attached to the variables we can tell the framework how to substitute them when generating a question:

    ## pssible alternative assignments for symbols
    assignments = {}
    assignments[a] = [a,e,f,g,h]
    assignments[x] = [x,X]

one can even tell it which numerical values (like ints floats etc) to substitute randomly in the QA generation:

    assignments[8] = [random.randint(0,200) for i in range(100)]


As usual we provide the answer some choices:

    ## generator for a choice of answer
    ans1 = seqg(x,' = ',2,'*',8)
    ans2 = seqg(x,'=',2,'*',8)
    answer = choiceg( ans1,ans2 )
    q,a = make_qa_pair(question,answer,assignments,seed=4)
    print('question: %s \nanswer: %s'%(q,a))

and now the QA generator will be able to substitute whatever was given in the assignment as it generates questions. Note that the framework doesn't actually know how to do maths so make sure you debug and print your answers and questions so that things are substituted correctly!
