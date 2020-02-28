import Tarea1Funciones


def test_func1():
    assert Tarea1Funciones.func1("abcdefghijk") == "ABCDEFGHIJK"


def test_func2():
    assert Tarea1Funciones.func2("asdw") == "Se encontró el string 'w'"


def test_func3():
    assert Tarea1Funciones.func3(5, 3) == 2


def test_func1error():
    assert Tarea1Funciones.func1("abcdefghijK") == "ABCDEFGHIJK"


def test_func2error():
    assert Tarea1Funciones.func2("asd") == "Se encontró el string 'w'"


def test_func3error():
    assert Tarea1Funciones.func3(5, 3) == 1
