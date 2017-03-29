% approach 1: we can trace function calls to visualize
seqg(' solve x, ', perg( ' a = b, ', seqg( ' x = 2*', 'b,' ), ' a = 8,' ), ' can you do it? ')
seqg(' solve x, ', func1() , ' can you do it? ')

% approach 2: use function handles to delay function calling, so that we can do visualization
seqg(' solve x, ', @()perg( ' a = b, ', @()seqg( ' x = 2*', 'b,' ), ' a = 8,' ), ' can you do it? ')


%% but it's best to trace the function calls, since there is no guarantee that student will strictly use approach 2
%% so we should always use approach 1 to be consistent











