# Token 类型
#
# EOF (end-of-file) 输入结束的标志
INTEGER, EOF, DIV, MUL = 'INTEGER', 'EOF', 'DIV', 'MUL'


class Token(object):
    def __init__(self, type, value):
        # token 类型: INTEGER, PLUS, or EOF
        self.type = type
        # token 值: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """可视化 Token

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # 要解释的内容，源代码，例如："3+5"
        self.text = text
        # self.pos 表示指向当前字符的位置。
        self.pos = 0
        # 当前的 Token
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        """修改 pos 的指向，并设置 current_char """
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """根据输入返回一个多位整数"""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """词法分析器（也叫扫描器或者标记器）

        这个方法负责将句子拆分成 Token
        一次一个 Token 。
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)

    def eat(self, token_type):
        # 比较当前的 token 类型和已经扫描过的 token 类型，
        # 如果二者类型一致，那么 "eat" 当前的 token 。
        # 并下一个 token 赋给当前 token 。
        # 否则返回 token 。
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        """返回一个 INTEGER token 的值"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        """Parser / Interpreter """
        # 将输入的第一个 token 设置为当前的 token 。
        self.current_token = self.get_next_token()

        # 当前的 token 是一个一位数的整数。
        result = self.term()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result += result * self.term()
            elif token.type == DIV:
                self.eat(DIV)
                result += result // self.term()

        return result


def main():
    while True:
        try:
            # 如果在 Python3 下运行，
            # 需要将 'raw_input' 替换为 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()