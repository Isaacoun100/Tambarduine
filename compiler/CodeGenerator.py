#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.
from AST import AbstractSyntaxTree
from AST import Node

indent_spaces = 4
indent = indent_spaces * "-"


# Para el metodo SET
class CodeGenerator:
    '''
    Metodos para convertir cada uno de los nodos a string, se usara la recursividad
    '''

    # Para el metodo SET
    def __translate_set(self, node):
        children = node.getChildren()

        variable = children[0]
        expression = children[1]

        return (variable + " = " + self.translate_node(expression))

    # Para el metodo Assignment
    def __translate_assign(self, node: Node.Assignment):
        children = node.getChildren()

        variable = children[0]
        expression = children[1]

        return (variable + " = " + self.translate_node(expression))

    # Para el metodo IF
    def __translate_if(self, node: Node.If):
        children = node.getChildren()

        condition = children[0]
        statements = children[1]
        Else = children[2]

        return "if " + self.translate_node(condition) + ": \n" + indent + self.translate_node(
            statements) + "\n" + self.translate_node(Else)

    # Para el metodo ELSE
    def __translate_Else(self, node):
        children = node.getChildren()

        statements = children[0]

        return "else: \n" + indent + self.translate_node(statements)

    # Para el metodo For
    def __translate_For(self):
        pass

    # Para el metodo DEF
    def __translate_def(self):
        pass

    # Para el metodo en caso
    def __translate_EnCaso(self):
        pass

    # Para el Cuando
    def __translate_cuando(self):
        pass

    # Para el Sino
    def __translate_sino(self):
        pass

    # Para el EnTons
    def __trannslate_EnTons(self):
        pass

    # Abanico
    def __translate_abanico(self):
        pass

    # Vertical
    def __translate_vertical(self):
        pass

    # Percutor
    def __translate_percutor(self):
        pass

    # Golpe
    def __translate_golpe(self):
        pass

    # Vibrato
    def __translate_vibrato(self):
        pass

    # Metronomo
    def __translate_metronomo(self):
        pass

    # Print
    def __translate_print(self):
        pass

    # Negation
    def __translate_negation(self):
        pass

    # Bool Operator
    def __translate_boolOp(self):
        pass

    # Binary Op
    def __translate_binaryOP(self):
        pass

    # Conditional Exp
    def __translate_Condition_expr(self):
        pass

    # Expression
    def __translate_expression(self, node: Node.Expression):
        children = node.getChildren()
        operator = node.getOperator()

        factor1 = children[0]
        factor2 = children[1]
        return self.__translate_node(factor1) + str(operator) + self.__translate_node(factor2)

    # Input method

    def translate_node(self, node):

        '''
        Revisar que tipo de nodo es y aplicar el metodo correcto
        '''
        if isinstance(node, Node.Set): return self.__translate_set(node)

        if isinstance(node, Node.Assignment): return self.translate_assign(node)

        if isinstance(node, Node.If): return self.__translate_if(node)

        if isinstance(node, Node.Else): return self.__translate_Else(node)

        if isinstance(node, Node.For): return self.__translate_For(node)

        if isinstance(node, Node.Def): return self.__translate_def(node)

        if isinstance(node, Node.En_Caso): return self.__translate_EnCaso(node)
        if isinstance(node, Node.Cuando_statement): return self.__translate_cuando(node)
        if isinstance(node, Node.Sino_statement): return self.__translate_sino(node)
        if isinstance(node, Node.EnTons_statement): return self.__trannslate_EnTons(node)

        if isinstance(node, Node.Abanico): return self.__translate_abanico(node)

        if isinstance(node, Node.Vertical): return self.__translate_vertical(node)

        if isinstance(node, Node.Percutor): return self.__translate_percutor(node)

        if isinstance(node, Node.Golpe): return self.__translate_golpe(node)

        if isinstance(node, Node.Vibrato): return self.__translate_vibrato(node)

        if isinstance(node, Node.Metronomo): return self.__translate_metronomo(node)

        if isinstance(node, Node.Metronomo): return self.__translate_metronomo(node)

        if isinstance(node, Node.Print): return self.__translate_print(node)

        if isinstance(node, Node.Negation): return self.__translate_negation(node)

        if isinstance(node, Node.BoolOp):
            return self.__translate_boolOp(node)

        if isinstance(node, Node.Expression):
            children = node.getChildren()

            operator = node.getOperator()
            factor1 = children[0]
            factor2 = children[1]
            # todo: caso cuando estan agrupados con parentesis
            return self.translate_node(factor1) + operator + self.translate_node(factor2)

        # is an terminal type

        else:
            return str(node)
