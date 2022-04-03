#  Copyright (c) 2022.
#  Code made by Eduardo Zumbado Granados.

from unittest import TestCase
from compiler.Compiler import *
from CodeGenerator import *


class TestCompiler(TestCase):
    __compiler = Comp()

    def test_compile(self):
        pass

    def test_Assignment(self):
        print(" -------------------- Assignment test --------------------"),
        text = '@var = 2 + 2 + 5*3;'
        ast = self.__compiler.compile(text)
        ast.print()

        node = ast.getRoot()
        cg = CodeGenerator()
        result = cg.translate_node(node)
        print("Result of compiling: ", result)

    def test_Set(self):
        print(" -------------------- SET test --------------------")

        text = 'SET @var2, 20 ; '
        ast = self.__compiler.compile(text)
        ast.print()

    def test_if(self):
        print(" -------------------- IF test --------------------")
        text = 'IF ( 2 < 23) { SET @var2, 20 ;} ELSE {SET @var2, 30 ;}'

        ast = self.__compiler.compile(text)
        ast.print()

        node = ast.getRoot()
        cg = CodeGenerator()
        result = cg.translate_node(node)
        print("Result of compiling:\n", result)

    def test_for_1(self):
        print(" -------------------- FOR (1) test --------------------")
        text = 'FOR (0) TO (100) STEP (1) { Percutor(A); }'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_for_2(self):
        print(" -------------------- FOR (2) test --------------------")
        text = 'FOR (1) TO (100){ @var =  1; }'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_en_caso(self):
        print(" -------------------- En Caso (1) test --------------------")
        text = 'EN_CASO  @var \n' \
               'CUANDO < 2  EN_TONS { \n' \
               'DEF @metodo(){\n' \
               '@var1 = 666;\n' \
               '} \n' \
               '} \n' \
               'CUANDO < 5  EN_TONS {\n' \
               ' @var2 = 2; \n' \
               '} \n' \
               'SI_NO{\n ' \
               '@var3 = 5; \n' \
               '} \n' \
               'FIN_EN_CASO '

        ast = self.__compiler.compile(text)
        ast.print()

    def test_DEF(self):
        print(" -------------------- DEF  test --------------------")
        text = 'DEF @method(){\n' \
               '@var1 = 666;\n' \
               '}'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_abanico(self):
        print(" -------------------- Abanico test --------------------")
        text = 'Abanico(B);'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_vertical(self):
        print(" -------------------- Vertical test --------------------")
        text = 'Vertical(D);'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_percutor(self):
        print(" -------------------- Percutor test --------------------")
        text = 'Percutor(AB);'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_golpe(self):
        print(" -------------------- Golpe test --------------------")
        text = 'Golpe();'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_vibrato(self):
        print(" -------------------- Vibrato test --------------------")
        text = 'Vibrato(343);'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_metronomo(self):
        print(" -------------------- Metronomo test --------------------")
        text = 'Metronomo(A, 1);'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_print(self):
        print(" -------------------- Print test --------------------")
        text = 'println!("Hola Mundo");'

        ast = self.__compiler.compile(text)
        ast.print()

    def test_binary_Ops(self):
        print(" -------------------- .F  test --------------------")
        text = '@var.F;'
        ast = self.__compiler.compile(text)
        ast.print()
        print(" -------------------- .T test --------------------")
        text = '@var.T;'
        ast = self.__compiler.compile(text)
        ast.print()
        print(" -------------------- Negation  test --------------------")
        text = '@var.Neg;'
        ast = self.__compiler.compile(text)
        ast.print()
