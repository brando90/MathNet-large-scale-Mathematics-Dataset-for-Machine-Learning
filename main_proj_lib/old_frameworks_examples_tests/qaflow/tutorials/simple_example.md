In this document we will explain how to construct an example problem with the framework. We will try to make variations of the following question and answer:

question:
> solve x,  a = b,  x = 2*b, a = 8, can you do it?
answer:
> x = 2*8 = 16

The framework will have two main ways to express questions:

* seqg - which will be used to sequentially attach fragments of questions (or answers). We will use this to force the order of sentences that have to be in a specific order.
* perg - which will be used to attach fragments of questions (or answers) and permute them randomly. We will use this to vary the order of sentences to give variety and have equivalent questions.

to express the question above we do:

    question = seqg('solve x ,', perg( 'a = b, ' , 'x = 2*b, ' , 'x = 8, ' ),'can you do it?')

Note that the middle part `perg( 'a = b, ' , 'x = 2*b, ' , 'x = 8, ' )` encodes that we can write any of those three sentences in any order and have the equivalent question.

to express the answer we will use:

* choiceg - which will chose one of its arguments randomly as a question. We will use this to vary the type of valid answer.

to express the answer above we do:

```
answer = choiceg( 'x = 2*8', 'x = 16', 'x = 2*8 = 16' )
```

Now we can test if the question worked by generating the string and displaying it:

    q,a = make_qa_pair(question,answer,assignments)
    print('question: %s \nanswer %s'%(q,a))


should print something like:

    solve x,  a = b,  x = 2*b, a = 8, can you do it?


Now if you want to generate the same question/answer provide a specific seed that makes the generators deterministic:

    q,a = make_qa_pair(question,answer,assignments,3)
    print('question: %s \nanswer %s'%(q,a))

should display:

    question: solve x , a = b,  x = 8,  x = 2*b,  can you do it?
    answer x = 2*8 = 16
