from grammar import *

def parser(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente + [('EOF','EOF')],
        'index': 0,
        'error': False,
    }   
    def principal():
        pni('Program')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0] # se obtiene token de [('Token','Lexema')]
        if caracter_actual != 'EOF' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True   
           
    def pni(no_terminal):
        terminal = datos_locales['lista_tokens'][datos_locales['index']][0]
        if terminal in SD[no_terminal]:
            procesar(SD[no_terminal][terminal])

    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1                        
                else:
                    datos_locales['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break
                 

