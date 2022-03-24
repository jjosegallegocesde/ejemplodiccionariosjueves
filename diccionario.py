persona={
    'nombre':'Juan Jose',
    'edad':32,
    'estatura':1.62,
    'leGustaFutbol':True
}

print(persona)
print(persona['nombre'])
print(persona.get('edad'))

persona['carrera']="ingeniero"
print(persona)