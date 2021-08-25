the evil python3-lambda evaluator for natsuki ( https://vk.com/public206129973 )

lambda.py -- λ evaluator ( python3 needed )

*.λ -- program written in λ ( python )

this is NOT a dialect of python tho
λ can interpret any lambda expression written using python's lambda syntax
but λ has some restrictions ( because of this runs on my server ) :
  any sequense of double-underscore __ will be removed from code before evaluation,
  listed number of python modules can be imported using "module" function,
  python __builtins__ is also modified.
  all of this done to provide some """"safetyness""""

more about safetyness of python "eval" discussed by me in safetyness.txt

featured additions in syntax:
  ununpackable arguments in lambda definitions must become unpackable ( python forbits u from unpacking values and actually makes life harder, idk y )







if u wonder what the fuck is going on here, here is my explanation:
  i was high and discovered that lambda-expressions in python are actually functionally-full;
  so i tried to write brainfuck interpreter ( almost succeeded ), and some other stuff using ONLY python lambda expressions;
  and if u think "meh, this must be as easy as writing in pure python" ur wrong, ok? behavior of lambdas is far more complicated tho;
  that's all.
