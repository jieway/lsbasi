# Token 类型
#
# EOF (end-of-file) 输入结束的标志
INTEGER, PLUS, EOF, MINUS = 'INTEGER', 'PLUS', 'EOF', 'MINUS'


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

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """词法分析器（也叫扫描器或者标记器）

        这个方法负责将句子拆分成 Token
        一次一个 Token 。
        """
        text = self.text

        # 如果 self.pos 索引到了 self.text 的末尾
        # 返回 EOF 表示输入字符均被转换成了 Tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # 获取当前位置的字符串，基于当前的单个字符来创建 Token
        current_char = text[self.pos]

        # 扫描到空格了，直接略过。
        # 改成循环是因为存在多个空格的情况。
        while current_char == ' ':
            self.pos += 1
            # 需要重置当前字符，因为略过了。
            current_char = text[self.pos]

        # 如果当前字符是数字，那么将其转换为整数，创建 INTEGER token
        # 然后 self.pos 索引自增，指向下一个字符，并返回创建好的 token。
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        # 比较当前的 token 类型和已经扫描过的 token 类型，
        # 如果二者类型一致，那么 "eat" 当前的 token 。
        # 并下一个 token 赋给当前 token 。
        # 否则返回 token 。
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER

        expr -> INTEGER PLUS INTEGER
        expr -> INTEGER MINUS INTEGER
        """
        # 将输入的第一个 token 设置为当前的 token 。
        self.current_token = self.get_next_token()

        # 当前的 token 是一个一位数的整数。
        left = self.current_token
        self.eat(INTEGER)

        # 当前的 token 是一个 “+” 号。
        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)

        # 当前的 token 是一个一位数的整数。
        right = self.current_token
        self.eat(INTEGER)
        # 上述内容被调用后，
        # self.current_token 被设置为 EOF token

        # 此时，整数加整数的 token 序列已经成功的被识别到，
        # 该方法可以成功返回两个整数相加后的结果，
        # 从而有效的解释输入。
        if op.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
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