the evil python3-lambda evaluator for natsuki ( https://vk.com/public206129973 )

lambda.py -- python λ evaluator

*.λ -- one big λ expression evaluated by python's builtin "eval"

this is NOT a dialect of python tho
λ can interpret any lambda expression written using python's lambda syntax
but λ has some restrictions ( because this dangerous injection-vulnarable piece of garbaje also runs on my server ):
  any sequence of double-underscore ( i.e. __ ) will be removed from code before evaluation,
  listed number of python modules ( safe ones ) can be imported using custom "module" function,
  python __builtins__ is modified.
  
  all of this done to provide some """"safetyness""""


more about safetyness of python "eval" discussed in safetyness.txt


addition in syntax unforgivenessness:
  ununpackable arguments in lambda definitions must become unpackable ( python forbits u from unpacking
  values and actually makes life harder, idk y ), here is why, f.e.:
    u cannot do things such "( lambda ( a, *b ), c : ( a, b, c ) ) ( ( 'a', 'b1', 'b2', 'b3' ), 'c' )"
    where ( 'a', 'b1', 'b2', 'b3' ) is a tuple and a, b, c are unpacked values of 'a', ( 'b1', 'b2', 'b3' ) and 'c' respectively.
    instead ull do something like "( lambda ab, c : ( ab[ 0 ], ab[ :-1 ], c ) ) ( [ 'a', 'b1', 'b2', 'b3' ], 'c' )"
    and this is unconvinient as fuck. very usual case tho.
  

if u still wonder what the fuck is going on, here is lil' preambule:
  i was high and discovered that lambda-expressions in python are actually functionally-full ( such wow! ) ;
  so i tried to write brainfuck interpreter ( almost succeeded, see bf.py ), and some other stuff using ONLY python lambda expressions ;
  and if u think "meh, this must be as easy as writing in pure python" ur wrong, ok? behavior of lambdas is far more complicated ;
  that's all.
