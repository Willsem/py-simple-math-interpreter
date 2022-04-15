from nodes import *
from values import Number, Bool

class Interpreter:
    def __init__(self):
        pass

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
        
    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def visit_MoreNode(self, node):
        return Bool(self.visit(node.node_a).value > self.visit(node.node_b).value)

    def visit_MoreEqualNode(self, node):
        return Bool(self.visit(node.node_a).value >= self.visit(node.node_b).value)

    def visit_LessNode(self, node):
        return Bool(self.visit(node.node_a).value < self.visit(node.node_b).value)

    def visit_LessEqualNode(self, node):
        return Bool(self.visit(node.node_a).value <= self.visit(node.node_b).value)

    def visit_EqualNode(self, node):
        return Bool(self.visit(node.node_a).value == self.visit(node.node_b).value)
