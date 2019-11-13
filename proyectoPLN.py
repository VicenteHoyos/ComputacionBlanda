import  mysql.connector
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import nltk 
from nltk.corpus import stopwords #filtra palabras de parada
from nltk.tokenize import word_tokenize # tokeniza el texto 
from nltk.corpus import wordnet # libreria para comparar palabras
from nltk.tokenize import RegexpTokenizer# libreria para eliminar los dignos de puntuacion
import tkinter as tk
import threading

text_frame = '...'
pantalla = tk.Tk()
label = tk.Label(pantalla,height = 5,width = 200,bg = 'white',justify = 'center', text = text_frame)
texto = tk.StringVar()


def preguntarTipo(clave):
    if clave==11:
        db = mysql.connector.connect(user ='root', host ='127.0.0.1',database='pcdoc') #Se puede establecer una conexión con el servidor MySQL 
        cursor = db.cursor() # El objeto cursor interactúa con el servidor MySQL 
        sql = "SELECT tipo FROM tipos WHERE tipoID = %d " %(clave) #Consulta SQL
        cursor.execute(sql) #Se realiza la consulta con el cursor
        lista = ""
        resultados = cursor.fetchall() #Cual metodo usar dependera de la cantidad de datos que tengamos, la memoria disponible en la PC y sobre todo, de como querramos hacerlo. Si estamos trabajando con datasets limitados, no habra problema con el uso de fetchall()
        for registro in resultados:
            nombre = registro[0]
            lista = lista + ("%s,"%(nombre))
        return lista

    if clave== "memoria" or "procesador" or "fuente":
        db = mysql.connector.connect(user ='root', host ='127.0.0.1',database='pcdoc') #Se puede establecer una conexión con el servidor MySQL 
        cursor = db.cursor()
        sql = "SELECT preguntaDESCRIPCION FROM preguntas WHERE preguntaTIPO ='%s'" %(clave)
        cursor.execute(sql)
        lista = ""
        resultados = cursor.fetchall()
        for registro in resultados:
            nombre = registro[0]
            lista = lista + ("%s,"%(nombre))
        return lista

def preguntaProblema(clave,respuestas):
    db = mysql.connector.connect(user ='root', host ='127.0.0.1',database='pcdoc')
    cursor = db.cursor()
    sql = "SELECT problemaID FROM problemas WHERE (preguntaTIPO ='%s' AND problemaDesc ='%s')" %(clave,respuestas)
    cursor.execute(sql)
    lista = ""
    resultados = cursor.fetchall()
    for registro in resultados:
        nombre = registro[0]
        lista = lista + ("%s"%(nombre))

    sql = "SELECT DescripcionRecomendacion FROM recomendacion WHERE problemaID ='%s' " %(lista)
    cursor.execute(sql)
    lista = ""
    resultados = cursor.fetchall()
    for registro in resultados:
        nombre = registro[0]
        lista = lista + ("%s, "%(nombre))
    return lista

def nula(variable):      # Implementamos la funcion.
  if(len(variable)==0):  # Preguntamos por la longitud de la variable.
    return True          # Si es 0 la funcion devuelve Verdadero(True)
  else:
    return False         # Si la funcion no es cero, devolvemos Falso(False)

def saludo():
    saludo = "Bienvenido a su PCdoc...¿Que tipo de error cree que presenta?"    
    tts = gTTS(saludo,'es')
    tts.save('voz.mp3')
    texto.set(saludo)
    label.config(textvariable=texto)
    playsound('voz.mp3')
    


def main():
    Clave= 11
    saludo()


    #Realizamos una consulta, donde extraemos los tipos de problema que puede presentar.
    consulta=preguntarTipo(Clave)
    tts = gTTS(consulta,'es') #la consulta realizada es transformada con la API de google traslate
    tts.save('voz1.mp3')
    playsound('voz1.mp3')


    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Responda: ")
        texto.set("Responda...")
        label.config(textvariable=texto)
        audio = r.listen(source)
        #print("OK!")
        texto.set("Procesando...")
        label.config(textvariable=texto)
    usuario = "Error"
    try:
        #print("Usted dijo: "+r.recognize_google(audio, language ='es-LA'))        
        var = "Usted dijo: "+r.recognize_google(audio, language ='es-LA')     
        usuario = r.recognize_google(audio, language ='es-LA')
        texto.set(var)
        label.config(textvariable=texto)
        tts = gTTS("Usted dijo: "+r.recognize_google(audio, language ='es-LA'),'es')
        tts.save('voz4.mp3')
        playsound('voz4.mp3')
    except:
        pass

    #NLTK tiene por defecto un grupo de palabras que considera palabras vacías. 
    #Se puede acceder a través del corpus NLTK con:
    #from nltk.corpus import stopwords
    #Para consultar la lista de palabras vacías almacenadas para el idioma inglés:
    #stop_words = set(stopwords.words("english"))
    #print(stop_words)

    stop_words = set(stopwords.words('spanish'))
    words = word_tokenize(usuario) #Devuelve una copia con token del texto(Respuesta Usuario), utilizando la palabra tokenizer recomendada por NLTK 
                                   #(actualmente nltk.tokenize.treebank.TreebankWordTokenizer junto con nltk.tokenize.punkt.PunktSentenceTokenizer para el idioma especificado).
    consultas= word_tokenize(consulta)

    new_consulta = []
    new_sentence = []

    #filtración de palabras de parada.
    for word in words:
        if word not in stop_words:
            new_sentence.append(word)
    for word in consultas:
        if word not in stop_words:
            new_consulta.append(word)


    print(new_sentence)#sentencia tokenizada que el usario a hablado 
    print(new_consulta)#sentencia tokenizada de la consulta tipo

    #Buscamos el token que coincida en ambas listas
    for word1 in new_sentence:
        for word2 in new_consulta:
            if word1==word2:
                Clave=word1
                print(Clave)
                if word1 == "poder" or word1 == "fuente":
                    Clave= "fuente"
                    print(Clave)

    consulta=preguntarTipo(Clave) 

    if Clave != 11:
        print("A continuación conteste con: SI o NO")
        #------------------------------------------------------
        texto.set("A continuación conteste con: SI o NO")
        label.config(textvariable=texto)
        #------------------------------------------------------
        tts = gTTS("A continuacion conteste con: SI o NO",'es')
        tts.save('voz3.mp3')
        playsound('voz3.mp3')

        new_sentence =consulta.split(',') #tokenizamos la consulta de preguntas, a partir del caracter ',';
                                        #lo que permite separar cada una de las preguntas
        lenght = len(new_sentence)
        list = ""
        i=0
        for i in range(lenght-1):
            tts = gTTS(new_sentence[i],'es')
            tts.save('consulta'+str(i)+'.mp3')
            playsound('consulta'+str(i)+'.mp3')
            i=i+1
            r = sr.Recognizer()
            with sr.Microphone() as source:
                #print("Responda: ")

                #------------------------------------------------------
                texto.set("Responda...")
                label.config(textvariable=texto)
                #------------------------------------------------------
                audio = r.listen(source)
                
                #------------------------------------------------------
                texto.set("Procesando...")
                label.config(textvariable=texto)
                #------------------------------------------------------
            usuario = "Error"
            try:
                var = "Usted Dijo: "+r.recognize_google(audio, language ='es-LA')
                UsuarioAnswer = r.recognize_google(audio, language ='es-LA')
                #------------------------------------------------------
                texto.set(var)
                label.config(textvariable = texto)
                #------------------------------------------------------
                list= list + ("%s,"%(UsuarioAnswer))
            except:
                var = "No se pudo entender el audio, por defecto sera 'no'"

                #------------------------------------------------------
                texto.set(var)
                label.config(textvariable = texto)
                #------------------------------------------------------

                UsuarioAnswer = "no"
                list= list + ("%s,"%(UsuarioAnswer))

        print(list)        
        Respuesta= preguntaProblema(Clave,list)
        
        Validar = nula(Respuesta) #Validamos que nuestra consulta fue exitosa

        if Validar== False:
            tts = gTTS("A continuación pcdoc, le hace las siguientes recomendaciones",'es')
            tts.save('Respuesta.mp3')

            #------------------------------------------------------
            texto.set("A continuación pcdoc, le hace las siguientes recomendaciones")
            label.config(textvariable = texto)
            #------------------------------------------------------

            playsound('Respuesta.mp3')
            tts = gTTS(Respuesta,'es')
            tts.save('Respuesta1.mp3')
            playsound('Respuesta1.mp3')
        else:
            tts = gTTS("lo sentimos no encontramos su problema en nuestra base de datos",'es')
            tts.save('Respuesta1.mp3')
            #------------------------------------------------------
            texto.set("lo sentimos no encontramos su problema en nuestra base de datos")
            label.config(textvariable = texto)
            #------------------------------------------------------
            playsound('Respuesta1.mp3')  
    else:
        tts = gTTS("lo sentimos no encontramos su problema en nuestra base de datos",'es')
        tts.save('Respuesta.mp3')
        #------------------------------------------------------
        texto.set("lo sentimos no encontramos su problema en nuestra base de datos")
        label.config(textvariable = texto)
        #------------------------------------------------------
        playsound('Respuesta.mp3')

def center(screen):        

    screen.update_idletasks()
    w = screen.winfo_screenwidth()
    h = screen.winfo_screenheight()
    size = tuple(int(_) for _ in screen.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    screen.geometry("%dx%d+%d+%d" % (size + (x, y)))

def iniciar():
    center(pantalla)
    pantalla.geometry('500x200')
    pantalla.resizable(False,False)
    pantalla.title('PCDOC')    
    label.pack()
    boton_inicio = tk.Button(pantalla,text='Empezar',command=hilo_2.start)
    boton_inicio.pack()
    pantalla.mainloop()



hilo_1 = threading.Thread(name='hilo 1',target=iniciar)
hilo_2 = threading.Thread(name='hilo 2',target=main)

#hilo_1.start()
iniciar()
#hilo_2.start()

 
#python project.py           


