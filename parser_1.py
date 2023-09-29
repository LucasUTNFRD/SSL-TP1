from grammar import *
def parser(lista_tokens):                   #la lista de tokens viene del lexer
    datos_parser = {
        'tokens': lista_tokens + [('#','#')],
        'posicion_indice': 0,
        'error': False,     
    }
    
    def principal():
        print(datos_parser['tokens'])
        pni('Program')
        token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        if token_actual != '#' or datos_parser['error']:
            print('la cadena no pertenece al lenguaje')
            return False
        else:
            print ('la cadena pertenece al lenguaje')

    def pni(no_terminal):
        terminal = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        parteDerecha = SD [no_terminal][terminal]           #no terminal es el tope de la pila, terminal es donde apunta el puntero en la cadena
        procesar(parteDerecha)
        
    
    def procesar(cuerpo_produccion):  #ingresa una produccion
        for simbolo in cuerpo_produccion:
            token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
            datos_parser['error']= False
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
# def parser(codigo_fuente):
#     datos_locales = {
#         'lista_tokens': codigo_fuente + [('#','#')],
#         'index': 0,
#         'error': False,
#     }   
#     def principal():
#         pni('Program')
#         caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0] # se obtiene token de [('Token','Lexema')]
#         if caracter_actual != '#' or datos_locales['error']:
#             print('La cadena no pertenece al lenguaje')
#             return False
#         print('La cadena pertenece al lenguaje')
#         return True   
#            
#     def pni(no_terminal):
#         terminal = datos_locales['lista_tokens'][datos_locales['index']][0]
#         if terminal in SD[no_terminal]:
#             procesar(SD[no_terminal][terminal])
#
#     def procesar(cuerpo_produccion):
#         for simbolo in cuerpo_produccion:
#             caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
#             datos_locales['error'] = False
#             if simbolo in VT:
#                 if simbolo == caracter_actual:
#                     datos_locales['index'] += 1                        
#                 else:
#                     datos_locales['error'] = True
#                     break
#             elif simbolo in VN:
#                 pni(simbolo)
#                 if datos_locales['error']:
#                     break
#                  

parser(lexer("leer vauxi ; vauxi equal 5"))
