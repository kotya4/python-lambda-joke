def kill_me ( a, b ) :
    from random import choice
    return choice ( [ [ a, b ], [ b, a ] ] )

def devil ( s ) :
    return s.replace ( * ( '__', '' ) ).replace ( '\'\n\'', '\'\\n\'' )



def evil ( s, itsme=False ) :
    s = devil ( s )

    class Message :
        """ Interface for giving visuals thru evil """
        def __init__ ( self, textual, visual ) :
            self.value = ( textual, visual )


    safe_funcs = [ 'Exception', 'None', 'True', 'False', 'abs', 'all', 'any', 'ascii', 'bin', 'callable', 'chr', 'delattr', 'dir', 'divmod', 'format', 'globals', 'hasattr', 'hash', 'hex', 'id', 'isinstance', 'issubclass', 'iter', 'len', 'locals', 'max', 'min', 'next', 'oct', 'ord', 'pow', 'repr', 'round', 'setattr', 'sorted', 'sum', 'bool', 'memoryview', 'bytearray', 'bytes', 'classmethod', 'complex', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 'property', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'staticmethod', 'str', 'super', 'tuple', 'type', 'zip' ]
    # unfase_funcs = [ key for key in __builtins__ if not ( key in safe_funcs ) ]


    class HackedHelper :
        """ Rewrited helper """

        # >>>help
        # will print out the string below
        def __repr__ ( self ) :
            return 'Ты взаимодействуешь с модифицированным eval из python3, на котором я написана. Попробуешь эксплоитнуть меня? :з Чтобы узнать о всех переменных среды, тайпни dir()'

        def __call__ ( self, safe_func ) :
            if type ( safe_func ) != str : raise Exception ( 'Ah, you must provide a string~~ very sorry >_<' )
            from pydoc import render_doc
            if safe_func in safe_funcs : return render_doc ( safe_func )
            raise Exception ( 'No documentation for this function~~ sorry >_< All available functions listed as "safe"' )

    hacked_help = HackedHelper ()

    # def hacked_exec ( s ) :
    #     return Message ( None, choice ( constants.photos_hacker ) )


    def hacked_import ( s ) :
        safe = [ 'math', 'random', 'functools' ]
        if not ( s in safe ) : raise Exception ( 'Cannot import unsafe module sorry~~ >.<' )
        try : return __import__ ( s )
        except : raise Exception ( 'Available imports are ' + ', '.join ( safe ) )


    locals = {
        # 'exec' : exec if itsme else hacked_exec,
        # 'constants': constants, # need for calling Message with photos (can be omited using dictionaries)
        'message' : Message,
        'safe' : safe_funcs,
        'module' : hacked_import,
        'help' : hacked_help,
    }


    globals = { '__builtins__' : {
        **locals,
        **{ key : vars(__builtins__)[ key ] for key in vars(__builtins__) if key in safe_funcs } }
    }


    r = eval ( s, globals, locals )


    if type ( r ) == Message : return r.value
    return ( str ( r ), None )



if __name__ == '__main__' :
    from sys import argv
    filemane = argv[ 1 ]
    if filemane.find ( '.py' ) < 0 :
        if filemane.find ( '.' ) < 0 : filemane += '.λ'
    with open ( filemane, 'r', encoding='utf-8' ) as f :
        program = f.read ()
    print ( evil ( program )[ 0 ].replace ( '\'\n\'', '\n' ) )


