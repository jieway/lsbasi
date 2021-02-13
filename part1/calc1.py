EOF, INTEGER, PLUS = 'EOF', 'INTEGER', 'PLUS'

class Token(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token({type},{value})".format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        return Exception('Error parsing input')

    def get_next_token(self):

        if self.pos > len(self.text) - 1:
            return Token(EOF,None)

        current_char = self.text[self.pos]

        if current_char.isdigit():
            self.pos += 1
            return Token(INTEGER,int(current_char))

        if current_char == '+':
            self.pos += 1
            return Token(PLUS, '+')

        self.error()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            return self.error()

    def expr(self):

        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        return left.value + right.value

def main():

    while True:
        text = input("calc1> ")
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == "__main__":
    main()