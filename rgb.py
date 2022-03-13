def hextofloats(h):
    color =  tuple(int(h[i:i + 2], 16) / 255. for i in (1, 3, 5))
    print(f"{color[0]:.3f},{color[1]:.3f},{color[2]:.3f}")
    return color

#Colores #fffff
Uno = "#44B8AF"
Dos = "#E50054"
Tres = "#FFE06E"
Cuatro= "#ED6D05"
Cinco = "#cbeaf1"
Seis = "#c3cfea"
Siete = "#f9bd13"
Ocho = "#f1b5a2"

#Llamado a la funcion hexagesimal a floats
Uno = hextofloats(Uno)
Dos = hextofloats(Dos)
Tres = hextofloats(Tres)
Cuatro= hextofloats(Cuatro)
Cinco = hextofloats(Cinco)
Seis = hextofloats(Seis)
Siete = hextofloats(Siete)
Ocho = hextofloats(Ocho)
     
def r_g_b (r,g,b):
    factor = 1/255
    r_color = factor * r
    g_color = factor *g
    b_color = factor * b
    print(f"fill({r_color:.2f},{g_color:.2f},{b_color:.2f})")
    return r_color , g_color , b_color
    
    
# sol = r_g_b(7,145,240)
# luna = r_g_b(245,65,21)
# newPage(500,500)
# fill(*sol)
# rect(0,0,500,500)
# fill(*luna)
# rect(100,100,300,300)

#Color hex
newPage(1000,1000)
blendMode('multiply')
fill(*Uno)
rect(0,0,1000,1000)
fill(*Dos)
rect(50,50,900,900)
fill(*Tres)
rect(100,100,800,800)
# fill(*Cuatro)
# rect(150,150,700,700)
# fill(*Cinco)
# rect(200,200,600,600)
# fill(*Seis)
# rect(250,250,500,500)
# fill(*Siete)
# rect(300,300,400,400)
# fill(*Ocho)
# rect(350,350,300,300)


     