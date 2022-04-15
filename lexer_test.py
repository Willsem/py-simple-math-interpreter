import unittest
from tokens import Token, TokenType
from lexer import Lexer

class TestLexer(unittest.TestCase):
    
    def test_empty(self):
        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])
    
    def test_whitespace(self):
        tokens = list(Lexer(" \t\n  \t\t\n\n").generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = list(Lexer("123 123.456 123. .456 .").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 123.456),
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 000.456),
            Token(TokenType.NUMBER, 000.000),
        ])
    
    def test_operators(self):
        tokens = list(Lexer("+-*/").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.PLUS),
            Token(TokenType.MINUS),
            Token(TokenType.MULTIPLY),
            Token(TokenType.DIVIDE),
        ])

    def test_parens(self):
        tokens = list(Lexer("()").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.LPAREN),
            Token(TokenType.RPAREN),
        ])
    
    def test_all(self):
        tokens = list(Lexer("27 + (43 / 36 - 48) * 51").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 36),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 48),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 51),
        ])

    def test_less(self):
        tokens = list(Lexer("12 < 45").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.LESS),
            Token(TokenType.NUMBER, 45),
        ])

    def test_less_equal(self):
        tokens = list(Lexer("12 <= 45").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.LESSEQUAL),
            Token(TokenType.NUMBER, 45),
        ])

    def test_more(self):
        tokens = list(Lexer("12 > 45").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MORE),
            Token(TokenType.NUMBER, 45),
        ])

    def test_more_equal(self):
        tokens = list(Lexer("12 >= 45").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MOREEQUAL),
            Token(TokenType.NUMBER, 45),
        ])

    def test_equal(self):
        tokens = list(Lexer("12 == 45").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.EQUAL),
            Token(TokenType.NUMBER, 45),
        ])

    def test_less_complex(self):
        tokens = list(Lexer("12 + 56 < 45 * 1").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 56),
            Token(TokenType.LESS),
            Token(TokenType.NUMBER, 45),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 1),
        ])

    def test_less_equal_complex(self):
        tokens = list(Lexer("12 + 56 <= 45 * 1").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 56),
            Token(TokenType.LESSEQUAL),
            Token(TokenType.NUMBER, 45),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 1),
        ])

    def test_more_complex(self):
        tokens = list(Lexer("12 + 56 > 45 * 1").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 56),
            Token(TokenType.MORE),
            Token(TokenType.NUMBER, 45),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 1),
        ])

    def test_more_equal_complex(self):
        tokens = list(Lexer("12 + 56 >= 45 * 1").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 56),
            Token(TokenType.MOREEQUAL),
            Token(TokenType.NUMBER, 45),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 1),
        ])

    def test_equal_complex(self):
        tokens = list(Lexer("12 + 56 == 45 * 1").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 12),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 56),
            Token(TokenType.EQUAL),
            Token(TokenType.NUMBER, 45),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 1),
        ])
