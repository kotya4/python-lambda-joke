the evil python3-lambda evaluator for natsuki ( https://vk.com/public206129973 )

lambda.py -- λ interpreter ( python3 needed )

*.λ -- program written in λ

this is actually is dialect of python,
λ can interpret any lambda expression written in python
but λ has some sintactic sugar:
any sequense of double-underscore __ will be removed,
listed number of python modules can be imported using "module" function,
python __builtins__ is modified to provide some safetyness.

more about safetyness written in "safetyness.txt"

featured: unpackable arguments in lambda definitions ( python forbits u from unpacking values and actually makes life harder )
