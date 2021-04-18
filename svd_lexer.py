from sly import Lexer

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, PRINT, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ, COMMENT }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    PRINT = r'TAMPIL'
    IF = r'JIKA'
    THEN = r'MAKA'
    ELSE = r'LAIN'
    FOR = r'UNTUK'
    FUN = r'FUNGSI'
    TO = r'SAMPAI'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')



if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('svd > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)