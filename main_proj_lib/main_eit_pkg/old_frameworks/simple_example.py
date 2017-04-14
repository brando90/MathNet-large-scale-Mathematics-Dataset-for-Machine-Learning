
##
question = seqg('solve x, ', seqg( ' a = b, ', seqg( ' x = 2*', 'b,' ), ' a = 8,' ), ' can you do it?')
question = seqg('solve x, ', x, seqg( Eq(a,a), ',', seqg( Eq(x,2*b), ',',Eq(a,8) ), ' can you do it?') )
##
sq = seqg( Eq(x,2*b), ',', Eq(a,8) )
sq = seqg( Eq(a,a), ',', sq )
sq = seqg('solve x, ', x, sq,' can you do it?')
