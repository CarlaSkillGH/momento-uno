# Lista para almacenar los libros
biblioteca = []

def agregar_libro():
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el autor del libro: ")
    año = input("Ingresa el año del libro: ")
    disponibilidad = True  # Por defecto, el libro está disponible
    
    libro = {
        'titulo': titulo,
        'autor': autor,
        'año': año,
        'disponible': disponibilidad
    }
    
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado exitosamente.")

def mostrar_libros():
    if biblioteca:
        print("Libros en la biblioteca:")
        for libro in biblioteca:
            estado = "Disponible" if libro['disponible'] else "Prestado"
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, Estado: {estado}")
    else:
        print("No hay libros en la biblioteca.")

# Ejemplo de uso
agregar_libro()
agregar_libro()  # Puedes agregar más libros para ver el funcionamiento
mostrar_libros()
