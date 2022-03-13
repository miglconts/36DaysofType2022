#Duración de animación
totalFrames = 150
segundos = 5
#Lienzo
factor = 1
ganancia = 0
ancho,alto = 1600*factor,1600*factor
print(ancho,alto)
y= 350
separacion = 0
texto= "A"*3
fuente_size= 1200*factor
primeraLinea = 0*factor
lineas = 1
separarLineas = 0*factor
#Cargar la fuente
fuente= '2022VF.ttf'

#Colores de fondo y texto
bg_r, bg_g, bg_b = 214, 11, 81
colores=[(0.267,0.722,0.686),(0.898,0.000,0.329),(1.000,0.878,0.431),(0.929,0.427,0.020
),(0.898,0.000,0.329),(1.000,0.878,0.431),(0.957,0.906,0.631),(0.945,0.710,0.200),(0.961,0.980,0.090),(0.953,0.820,0.776), ]

#Calcular numero de caracteres
chars= len(texto) 
#Calcular el tamaño de la fuente
#fuente_size= ancho/ 8.0
axis_name=list(listFontVariations(fuente).items())[0][0]
minValue = listFontVariations(fuente)[axis_name]["minValue"]
maxValue= listFontVariations(fuente)[axis_name]["maxValue"]
print(axis_name,minValue,maxValue)
# duración
frame_duration = segundos /totalFrames

#Por cada frame
for frame in range(totalFrames):
    #Nueva pagina
    newPage(ancho,alto)
    frameDuration(frame_duration)
    # Dibujar el fondoe
    fill(1)
    rect(0,0,ancho,alto)
    #Carcular la posicion vertical de la primera linea
    blendMode("multiply")
    #Inicio de animación
    frame_start = (2*pi) * frame/totalFrames
    #Por cada linea
    x = width()/2 - ganancia
    #translate(width()/2, height()/2)
    for char_index in range(chars):
        step_start = frame_start - (pi * (char_index / (chars)))
        txt = FormattedString()
        txt.fill(*colores[char_index] )
        txt.font(fuente)
        txt.fontSize(fuente_size) 
        #txt.tracking(0)
        
        # Calculate the wght value
        dx = pi * frame / totalFrames
        delta = pow(sin(dx), 3)
        inst_step = pi * (char_index / (chars -1))
        curr_step = (cos(step_start - inst_step) + 1) / 2
        axisValue = minValue + curr_step * (maxValue - minValue)

        kwargs = {axis_name: axisValue}
        #print(kwargs)
        #print(wght_value)
        # Add the character to the text object
        txt.append(
            texto[char_index], 
            fontVariations=dict(**kwargs),
            tracking = 5
            )
        # After all characters were added 
        # to the text object, get its dimensions
        text_width, text_height = textSize(txt)

        # Calculate the horizontal position required 
        # to center this line on the page
        x += separacion 
        
        # Finally draw this line of text
        text(txt, (x, y), align =  'center')

        # Move the y coordinate up for the next line
    
    
saveImage(f"{texto}-olas.mp4")