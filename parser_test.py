import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 51.2)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(51.2))

    def test_single_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(27), NumberNode(14)))
        
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(27), NumberNode(14)))
            
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(27), NumberNode(14)))
            
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 14),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(27), NumberNode(14)))

    def test_full_expression(self):
        tokens = [
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
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(
            NumberNode(27),
            MultiplyNode(
                SubtractNode(
                    DivideNode(
                        NumberNode(43),
                        NumberNode(36)
                    ),
                    NumberNode(48)
                ),
                NumberNode(51)
            )
        ))

    def test_bool_more_expression(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.MORE),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 4),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 2),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, MoreNode(
            AddNode(
                NumberNode(27),
                NumberNode(43),
            ),
            MultiplyNode(
                SubtractNode(
                    NumberNode(12),
                    NumberNode(4),
                ),
                NumberNode(2),
            )
        ))

    def test_bool_more_equal_expression(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.MOREEQUAL),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 4),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 2),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, MoreEqualNode(
            AddNode(
                NumberNode(27),
                NumberNode(43),
            ),
            MultiplyNode(
                SubtractNode(
                    NumberNode(12),
                    NumberNode(4),
                ),
                NumberNode(2),
            )
        ))

    def test_bool_less_expression(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.LESS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 4),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 2),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, LessNode(
            AddNode(
                NumberNode(27),
                NumberNode(43),
            ),
            MultiplyNode(
                SubtractNode(
                    NumberNode(12),
                    NumberNode(4),
                ),
                NumberNode(2),
            )
        ))

    def test_bool_less_equal_expression(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.LESSEQUAL),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 4),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 2),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, LessEqualNode(
            AddNode(
                NumberNode(27),
                NumberNode(43),
            ),
            MultiplyNode(
                SubtractNode(
                    NumberNode(12),
                    NumberNode(4),
                ),
                NumberNode(2),
            )
        ))

    def test_bool_equal_expression(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.EQUAL),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 4),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 2),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, EqualNode(
            AddNode(
                NumberNode(27),
                NumberNode(43),
            ),
            MultiplyNode(
                SubtractNode(
                    NumberNode(12),
                    NumberNode(4),
                ),
                NumberNode(2),
            )
        ))
