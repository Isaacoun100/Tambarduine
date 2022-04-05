#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.
from compiler.AST import AbstractSyntaxTree
from compiler.AST import Node

indent_spaces = 4
indent = indent_spaces * " "
import_source = "import Firmata.Instructions as f" + "\n" + "T=1"


# Para el metodo SET
class CodeGenerator:
    '''
    Metodos para convertir cada uno de los nodos a string, se usara la recursividad
    '''
    __methods = {}

    # Para el metodo SET
    def __translate_set(self, node: Node.Set):
        children = node.getChildren()

        variable = children[0]
        expression = children[1]

        return (self.translate_node(variable) + " = " + self.translate_node(expression))

    # Para el metodo Assignment
    def __translate_assign(self, node: Node.Assignment):
        children = node.getChildren()

        variable = children[0]
        expression = children[1]

        return (self.translate_node(variable) + " = " + self.translate_node(expression))

    # Para el metodo IF
    def __translate_if(self, node: Node.If):
        children = node.getChildren()

        condition = children[0]
        statements = children[1]
        if len(children) == 2:
            return "if " + self.translate_node(condition) + ": \n" + indent + self.translate_node(
                statements)

        Else = children[2]
        return "if " + self.translate_node(condition) + ": \n" + indent + self.translate_node(
            statements) + "\n" + self.translate_node(Else)

        return "if " + self.translate_node(condition) + ": \n" + indent + self.translate_node(
            statements) + "\n" + self.translate_node(Else)

    # Para el metodo ELSE
    def __translate_Else(self, node: Node.Else):
        children = node.getChildren()

        statements = children[0]

        return "else: \n" + indent + self.translate_node(statements)

    # Para el metodo For
    def __translate_For(self, node: Node.For):
        pass

    # Para el metodo DEF
    def __translate_def(self, node: Node.Def):
        children = node.getChildren()

        name = children[0]
        name_str = name[1:len(name)]
        statements = children[1]

        self.__methods[name] = statements
        return "def " + name + "(): \n" + indent + self.translate_node(statements)

    # Para el metodo en caso
    def __translate_EnCaso(self, node: Node.En_Caso):
        pass

    # Para el Cuando
    def __translate_cuando(self, node: Node.Cuando_statement):
        pass

    # Para el Sino
    def __translate_sino(self, node: Node.Sino_statement):
        pass

    # Para el EnTons
    def __trannslate_EnTons(self, node: Node.EnTons_statement):
        pass

    # Abanico
    def __translate_abanico(self, node: Node.Abanico):
        children = node.getChildren()
        children = node.getChildren()

        param = children[0]

        param_str = '"' + param + '"'
        return "f.Abanico(" + param_str + ", T)"

    # Vertical
    def __translate_vertical(self, node: Node.Vertical):
        children = node.getChildren()

        param = children[0]
        param_str = '"' + param + '"'

        return "f.Vertical(" + param_str + ", T)"

    # Percutor
    def __translate_percutor(self, node: Node.Percutor):
        children = node.getChildren()

        param = children[0]

        param_str = '"' + param + '"'

        return "f.Percutor(" + param_str + ", T)"

        # Golpe

    def __translate_golpe(self, node: Node.Golpe):

        return "f.Golpe(T)"

    # Vibrato
    def __translate_vibrato(self, node: Node.Vibrato):
        children = node.getChildren()

        param = children[0]
        param_str = '"' + param + '"'

        return "f.Vibrato(" + param_str + ", T" + ")"

    # Metronomo
    def __translate_metronomo(self, node: Node.Metronomo):
        children = node.getChildren()
        state = children[0]
        time = children[1]

        # return "Metronomo(" + state + ", " + time + ")"
        return "f.T = " + time

    # Print
    def __translate_print(self, node: Node.Print):
        children = node.getChildren()

        param = children[0]
        return "print(" + '"' + self.translate_node(param) + ")"

    # Negation
    def __translate_negation(self, node: Node.Negation):
        children = node.getChildren()
        variable = children[0]
        return "not " + variable

    # Bool Operator
    def __translate_boolOp(self, node: Node.BoolOp):
        children = node.getChildren()
        var = children[0]
        value = children[1]

        result = ""

        if value:
            result = "= True"
        else:
            result = "= False"
        return var + result

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

        if isinstance(node, Node.Assignment): return self.__translate_assign(node)

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
        if isinstance(node, str):
            return node[1:len(node)]
        else:

            return str(node)

    def compile(self, ast: AbstractSyntaxTree.AST):

        result = import_source + "\n" + self.translate_node(ast.getRoot())

        # file.write(result)
        return result
