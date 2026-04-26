from Libreria.IA.openRouter import OpenRouter
from Libreria.Audio.audio import Audio
audiouwu=Audio()
ia=OpenRouter()
audiouwu.hablar("¿Quieres usar teclado o micrófono?")
opcion=input("¿Quieres usar teclado o micrófono? ").lower()
#imaginemos que no es ciego, entonces que diga qué quiere usar(microfono o tecaldo)
if opcion=="teclado":#si es teclado
    texto=input("¿Qué quieres preguntarle a la IA? ")
    respuesta=ia.generar(texto)
    print("IA respondió: "+respuesta)
    audiouwu.hablar(respuesta)
elif opcion=="microfono":#si es micro
    texto=audiouwu.escuchar()
    if texto:
        respuesta=ia.generar(texto)
        print("IA respondió: "+respuesta)
        audiouwu.hablar(respuesta)
else:#si es que puso otra cosa >:v, tal vez es ciego y por eso puso alguna wbda, entonces que hable
    audiouwu.hablar("No entendí, dime por micrófono si quieres teclado o micrófono")
    print("No entendí, dime por micrófono si quieres teclado o micrófono")
    print("Habla:")
    texto=audiouwu.escuchar()
    if texto and "teclado" in texto.lower(): #si dijo teclado
        pregunta=input("¿Qué quieres preguntarle a la IA?")
        respuesta=ia.generar(pregunta)
        print("IA respondió: "+respuesta)
        audiouwu.hablar(respuesta)
    elif texto and "microfono" in texto.lower():#si dijo micro
        texto=audiouwu.escuchar()
        if texto:
            respuesta=ia.generar(texto)
            print("IA respondió: "+respuesta)
            audiouwu.hablar(respuesta)
    else:#sino tampoco dijo algo válido :c
        print("No se pudo entender :c")
