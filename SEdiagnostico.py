from tkinter import * 
from tkinter.ttk import *


#--------Base de conocimientos
def colesterol():
    preguntas_colesterol = []
    preguntas_colesterol.append("¿Tiene hinchazón en alguna extremidad del cuerpo?")
    preguntas_colesterol.append("¿Tiene pérdida del equilibrio y mareos?")
    preguntas_colesterol.append("¿Tienes dolor de cabeza?")
    preguntas_colesterol.append("¿Tiene amarillo en sus ojos?")
    preguntas_colesterol.append("¿Tiene visión borrosa?")
    preguntas_colesterol.append("¿Tiene agitación al caminar o al realizar alguna actividad?")
    preguntas_colesterol.append("¿Tiene dolor en el pecho?")
    return preguntas_colesterol

def diabetes():
    preguntas_diabetes = []
    preguntas_diabetes.append("¿Padece de orinar con frecuencia?")
    preguntas_diabetes.append("¿Padece de sed constante?")
    preguntas_diabetes.append("¿Padece de hambre excesivo?")
    preguntas_diabetes.append("¿Padece de pérdida de peso inexplicable?")
    preguntas_diabetes.append("¿Padece de debilidad de su cuerpo?")
    preguntas_diabetes.append("¿Padece de irratibilidad?")
    preguntas_diabetes.append("¿Padece de visión borrosa?")
    return preguntas_diabetes

def gastritis():
    preguntas_gastritis = []
    preguntas_gastritis.append("¿Padece de ardor en el estómago?")
    preguntas_gastritis.append("¿Padece de pérdida de peso?")
    preguntas_gastritis.append("¿Padece de nauseas repentinas?")
    preguntas_gastritis.append("¿Padece de hipo o eructos frecuentes?")
    preguntas_gastritis.append("¿Padece de mal de sabor de la boca?")
    preguntas_gastritis.append("¿Padece de vacío gástrico?")
    return preguntas_gastritis

def asma():
    preguntas_asma = []
    preguntas_asma.append("¿Padece de tos?")
    preguntas_asma.append("¿Tiene sibilancias?")
    preguntas_asma.append("¿Siente alguna presion en el pecho?")
    preguntas_asma.append("¿Tiene dificultad para respirar?")
    return preguntas_asma

def sida():
    preguntas_sida = []
    preguntas_sida.append("¿Tiene fiebre?")
    preguntas_sida.append("¿Tiene dolor de cabeza?")
    preguntas_sida.append("¿Tiene o sufre de fatiga?")
    preguntas_sida.append("¿Tiene glandios linfáticos hinchados?")
    preguntas_sida.append("¿Tiene dolor de garganta?")
    preguntas_sida.append("¿Tiene sarpullido?")
    return preguntas_sida

def tuberculosis():
    preguntas_tuberculosis = []
    preguntas_tuberculosis.append("¿Tiene tos con sangre o esputo?")
    preguntas_tuberculosis.append("¿Tiene dolor en el pecho?")
    preguntas_tuberculosis.append("¿Tiene debilidad o cansancio?")
    preguntas_tuberculosis.append("¿Tiene falta de apetito?")
    preguntas_tuberculosis.append("¿Tiene escalofrios?")
    preguntas_tuberculosis.append("¿Tiene pérdida de peso?")
    preguntas_tuberculosis.append("¿Tiene fiebre?")
    return preguntas_tuberculosis

def neumonia():
    preguntas_neumonia = []
    preguntas_neumonia.append("¿Padece de malestar general?")
    preguntas_neumonia.append("¿Padece de dolores musculares y articulares?")
    preguntas_neumonia.append("¿Padece de dolor de cabeza?")
    preguntas_neumonia.append("¿Padece de cansancio?")
    return preguntas_neumonia
    
def pestes():
    preguntas_peste = []
    preguntas_peste.append("¿Padece de dolor de cabeza?")
    preguntas_peste.append("¿Padece de infiltraciones de sangre en la piel?")
    preguntas_peste.append("¿Padece de dolor de estómago?")
    preguntas_peste.append("¿Padece de fiebre?")
    preguntas_peste.append("¿Padece de cansancio?")
    preguntas_peste.append("¿Padece de escalofrios?")
    return preguntas_peste

def obesidad():
    preguntas_obesidad = []
    preguntas_obesidad.append("¿Padece de baja resistencia?")
    preguntas_obesidad.append("¿Padece de sudoración?")
    preguntas_obesidad.append("¿Padece de molestias articulares?")
    return preguntas_obesidad
    
def malaria():
    preguntas_malaria = []
    preguntas_malaria.append("¿Padece de sudoración?")
    preguntas_malaria.append("¿Padece de fiebre?")
    preguntas_malaria.append("¿Padece de escalofrios?")
    preguntas_malaria.append("¿Padece de tiritonas?")
    preguntas_malaria.append("¿Padece de vómito y diarrea?")
    preguntas_malaria.append("¿Padece de dolores generalizados de musculos y articulaciones?")
    return preguntas_malaria

def epilepsia():
    preguntas_epilepsia = []
    preguntas_epilepsia.append("¿Padece de mareos?")
    preguntas_epilepsia.append("¿Padece de crisis epileptica?")
    preguntas_epilepsia.append("¿Padece de dificultad para hablar?")
    preguntas_epilepsia.append("¿Padece de sensacion de desconexion con el entorno?")
    preguntas_epilepsia.append("¿Padece de rigidez muscular?")
    preguntas_epilepsia.append("¿Padece de convulsiones?")
    return preguntas_epilepsia

preguntas_colesterol = colesterol()
preguntas_diabetes = diabetes()
preguntas_gastritis = gastritis()
preguntas_asma = asma()
preguntas_sida = sida()
preguntas_tuberculosis = tuberculosis()
preguntas_neumonia = neumonia()
preguntas_peste = pestes()
preguntas_obesidad = obesidad()
preguntas_malaria = malaria()
preguntas_epilepsia = epilepsia()


n = 0

def ventana_preguntas():
    ventana_preguntas_colesterol(preguntas_colesterol, 0)



def ventana_resultados(flag, enfermedad):
    res = Tk()
    res.title('Resultados')
    
    global n 
    n = 0
    
    texto=Label(res ,justify=CENTER, text='De acuerdo a las preguntas contestadas, usted padece de la enfermedad: ', wraplength=450, pad=10)
    texto.pack()
    texto.config(font=("Arial", 15))
    texto_enfermedad = Label(res, justify=CENTER, text = enfermedad, pad = 10)
    texto_enfermedad.pack()
    texto_enfermedad.config(font=("Arial", 15))


def main():
    master = Tk() 
    master.title('Diagnóstico de Enfermedades')
    
    titulo=Label(master,justify=CENTER, text='Diagnóstico de Enfermedades', wraplength=450, pad=10)
    titulo.pack()
    titulo.config(font=("Courier", 35))
    
    descrip = "El objetivo principal del presente trabajo es crear un sistema experto para el diagnóstico de enfermedades, permitiendo con ello atender de manera inmediata las inquietudes de los pacientes."
    description=Label(master,justify=CENTER, text=descrip, wraplength=450, pad=10)
    description.pack()
    description.config(font=("Arial", 12))
    
    btn = Button(master, text = 'Comenzar',  
                              command = ventana_preguntas).pack(side='top', pady=20)
    
    mainloop() 



#------------------------------------------------------COLESTEROL

def ventana_preguntas_colesterol(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Colesterol')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_col_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_col_no).pack(side='top', pady=10)
    

def cmd_col_si():
    ventana.destroy()
    global n
    global preguntas_colesterol
    n = n+1
    if n >= len(preguntas_colesterol):
        ventana_resultados(True, "Colesterol")
    else:
        ventana_preguntas_colesterol(preguntas_colesterol, n)
    
def cmd_col_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_diabetes(preguntas_diabetes, n)




#-----------------------------------------------------------DIABETES
def ventana_preguntas_diabetes(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Diabetes')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_dia_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_dia_no).pack(side='top', pady=10)    

def cmd_dia_si():
    ventana.destroy()
    global n
    global preguntas_diabetes
    n = n+1
    if n >= len(preguntas_diabetes):
        ventana_resultados(True, "Diabetes")
    else:
        ventana_preguntas_diabetes(preguntas_diabetes, n)
    
def cmd_dia_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_gastritis(preguntas_gastritis, n)

#----------------------------------------------------------GASTRITIS

def ventana_preguntas_gastritis(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Gastritis')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_gast_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_gast_no).pack(side='top', pady=10)    

def cmd_gast_si():
    ventana.destroy()
    global n
    global preguntas_gastritis
    n = n+1
    if n >= len(preguntas_gastritis):
        ventana_resultados(True, "Gastritis")
    else:
        ventana_preguntas_gastritis(preguntas_gastritis, n)
    
def cmd_gast_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_asma(preguntas_asma, n)

#--------------------------------------------------------ASMA
    
def ventana_preguntas_asma(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Asma')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_asma_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_asma_no).pack(side='top', pady=10)    

def cmd_asma_si():
    ventana.destroy()
    global n
    global preguntas_asma
    n = n+1
    if n >= len(preguntas_asma):
        ventana_resultados(True, "Asma")
    else:
        ventana_preguntas_asma(preguntas_asma, n)
    
def cmd_asma_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_sida(preguntas_sida, n)

    
#---------------------------------------------------------SIDA
    
    
def ventana_preguntas_sida(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - SIDA')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_sida_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_sida_no).pack(side='top', pady=10)    

def cmd_sida_si():
    ventana.destroy()
    global n
    global preguntas_sida
    n = n+1
    if n >= len(preguntas_sida):
        ventana_resultados(True, "SIDA")
    else:
        ventana_preguntas_sida(preguntas_sida, n)
    
def cmd_sida_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_tub(preguntas_tuberculosis, n)
    
#---------------------------------------------------------TUBERCULOSIS
    
    
def ventana_preguntas_tub(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Tuberculosis')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_tub_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_tub_no).pack(side='top', pady=10)    

def cmd_tub_si():
    ventana.destroy()
    global n
    global preguntas_tuberculosis
    n = n+1
    if n >= len(preguntas_tuberculosis):
        ventana_resultados(True, "Tuberculosis")
    else:
        ventana_preguntas_tub(preguntas_tuberculosis, n)
    
def cmd_tub_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_neumonia(preguntas_neumonia, n)
    
#---------------------------------------------------------NEUMONIA
    
    
def ventana_preguntas_neumonia(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Neumonia')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_neu_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_neu_no).pack(side='top', pady=10)    

def cmd_neu_si():
    ventana.destroy()
    global n
    global preguntas_neumonia
    n = n+1
    if n >= len(preguntas_neumonia):
        ventana_resultados(True, "Neumonia")
    else:
        ventana_preguntas_neumonia(preguntas_neumonia, n)
    
def cmd_neu_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_peste(preguntas_peste, n)
    
#---------------------------------------------------------PESTE
    

def ventana_preguntas_peste(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Peste')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_peste_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_peste_no).pack(side='top', pady=10)    

def cmd_peste_si():
    ventana.destroy()
    global n
    global preguntas_peste
    n = n+1
    if n >= len(preguntas_peste):
        ventana_resultados(True, "Peste")
    else:
        ventana_preguntas_peste(preguntas_peste, n)
    
def cmd_peste_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_obesidad(preguntas_obesidad, n)
    
#-------------------------------------------------------OBESIDAD
    

def ventana_preguntas_obesidad(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Obesidad')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_obe_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_obe_no).pack(side='top', pady=10)    

def cmd_obe_si():
    ventana.destroy()
    global n
    global preguntas_obesidad
    n = n+1
    if n >= len(preguntas_obesidad):
        ventana_resultados(True, "Obesidad")
    else:
        ventana_preguntas_obesidad(preguntas_obesidad, n)
    
def cmd_obe_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_malaria(preguntas_malaria, n)
    
#---------------------------------------------------------MALARIA
    
 
def ventana_preguntas_malaria(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Malaria')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_mal_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_mal_no).pack(side='top', pady=10)    

def cmd_mal_si():
    ventana.destroy()
    global n
    global preguntas_malaria
    n = n+1
    if n >= len(preguntas_malaria):
        ventana_resultados(True, "Malaria")
    else:
        ventana_preguntas_malaria(preguntas_malaria, n)
    
def cmd_mal_no():
    ventana.destroy()
    global n
    n = 0
    ventana_preguntas_epilepsia(preguntas_epilepsia, n)
    
    
#---------------------------------------------------------EPILEPSIA
    
    
def ventana_preguntas_epilepsia(preg_col, n):
    global ventana
    ventana = Tk()
    ventana.title('Preguntas - Epilepsia')

    
    pregunta=Label(ventana ,justify=CENTER, text=preg_col[n], wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    
    btn = Button(ventana, text = 'Sí',  
                              command = cmd_epil_si).pack(side='top', pady=10)
    
    
    btn = Button(ventana, text = 'No',  
                              command = cmd_epil_no).pack(side='top', pady=10)    

def cmd_epil_si():
    ventana.destroy()
    global n
    global preguntas_epilepsia
    n = n+1
    if n >= len(preguntas_epilepsia):
        ventana_resultados(True, "Epilepsia")
    else:
        ventana_preguntas_epilepsia(preguntas_epilepsia, n)
    
def cmd_epil_no():
    ventana.destroy()
    #global n
    #n = 0
    ventana_ninguna_enf()
    
    
#--------------------------------------- ninguno de los anteriores
    
    
def ventana_ninguna_enf():
    res = Tk()
    res.title('Resultados')
    
    texto=Label(res ,justify=CENTER, text='Usted NO padece todos los síntomas de ninguna de las enfermedades listadas para este programa', wraplength=450, pad=40)
    texto.pack()
    texto.config(font=("Arial", 15))
    
    
#----------------------------------------------    
main()