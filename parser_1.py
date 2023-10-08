from grammar import *

def parser(lista_tokens):  # la lista de tokens viene del lexer
    datos_parser = {
        'tokens': lista_tokens + [('#', '#')],
        'posicion_indice': 0,
        'error': False,
    }

    def principal():
        print(datos_parser['tokens'])
        pni('Program')
        token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        if token_actual != '#' or datos_parser['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        else:
            print('La cadena pertenece al lenguaje')

    def pni(no_terminal):
        terminal = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        parteDerecha = SD[no_terminal][terminal]  # no terminal es el tope de la pila, terminal es donde apunta el puntero en la cadena
        print(f'Derivando {no_terminal} -> {" ".join(parteDerecha)}')
        procesar(parteDerecha)

    def procesar(cuerpo_produccion):  # ingresa una producción
        for simbolo in cuerpo_produccion:
            token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
            datos_parser['error'] = False
            print(f'Procesando Producción: {simbolo}')
            if simbolo in VT:
                if simbolo == token_actual:
                    datos_parser['posicion_indice'] += 1
                else:
                    datos_parser['error'] = True
                    break

            elif simbolo in VN:
                pni(simbolo)
                if datos_parser['error']:
                    break

    return principal()
                 

parser(lexer("si 6 > 7 entonces var equal 8"))
parser(lexer("leer vauxi ; vauxi equal 5"))
parser(lexer('mostrar 3 * 2 > 5 * 6'))
parser(lexer("si 4 > 3 entonces repetir leer id hasta 3 sino mostrar 4 finsi"))
parser(lexer("si 6>7 entonces leer id finsi"))