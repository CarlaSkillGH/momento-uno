# Lista para almacenar los libros
biblioteca = []

def agregar_libro():
    # Pedir información al usuario
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el autor del libro: ")
    año = input("Ingresa el año del libro: ")
    
    # Crear un diccionario con la información del libro
    libro = {
        'titulo': titulo,
        'autor': autor,
        'año': año
    }
    
    # Agregar el libro a la biblioteca
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado exitosamente.")

def ver_biblioteca():
    if biblioteca:
        print("Libros en la biblioteca:")
        for libro in biblioteca:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}")
    else:
        print("No hay libros en la biblioteca.")

# Ejemplo de uso
agregar_libro()
ver_biblioteca()
