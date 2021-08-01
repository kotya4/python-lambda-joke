# brainfuck interpreter on λ ( as i call my python-lambda dialect )

( lambda s, sp, case : (

__ module('functools').reduce ( lambda a, c : (
____ # a packed as ( s, sp )
____ [ ( s, sp ) for ( condition, ( s, sp ) ) in case ( c,
______ (                       ( False, ( s, sp ) ) ),
______ ( lambda c : c == '+',  ( True, ( a[0][:a[1]] + [(a[0][a[1]]+1)%256] + a[0][a[1]+1:], a[1] ) ) ),
______ ( lambda c : c == '-',  ( True, ( a[0][:a[1]] + [(a[0][a[1]]-1 if a[0][a[1]] > 0 else 255)] + a[0][a[1]+1:], a[1] ) ) ),
______ ( lambda c : c == '>',  ( True, ( a[0]+[0]*(len(a[0])-a[1]), a[1]+1 ) ) ),
______ ( lambda c : c == '<',  ( True, ( [0]*(0 if a[1] else 1)+a[0], a[1]-1 if a[1] else 0 ) ) ),
______ ) if condition ][ 0 ]
______ # phuh... 4 commands is enough for today
__ ), '+++>++>+<-<-', ( s, sp ) )

,

# ( lambda ssp : enter_the_loop if ssp[0][ssp[1]] else go_to_cicle_end )

# ss+[[0]]*(len(ss)-pp)

( lambda self, ps, pp, s, sp, p : ( ( ps+[[0]]*(len(ps)-pp), pp+1 ) if s[sp] else ( ps, pp ) ) if c == '[' else ( ps[pp-1], pp-1 ) if c == ']' else ( ps[pp] .... ) for c in p )( None, '++[++]++' )

)

) (
__ # initial stack and stack pointer
__ [ 0 ], 0,
__ # case :
__ ( lambda value, default, *states : (
________ result
______ if condition ( value ) == True else
________ default
____ for ( condition, result ) in states
__ ) ) ,
)
