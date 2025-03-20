inventory = {}

# menu principal
def main_menu():
    print('Gestion de inventario. Menu principal')
    print('1. Agregar producto')
    print('2. Eliminar producto')
    print('3. Mostrar inventario')
    print('4. Salir')
    
# funcion para agregar productos
def add_product(inventory):
    name = input('Ingrese el nombre del producto: ')
    if name in inventory:
        print('El producto ya existe.')
    else:
        stock = int(input('Ingrese el stock del producto: '))
        inventory[name.capitalize()] = stock

# funcion para eliminar productos
def remove_product(inventory):
    name = input('Ingrese el nombre del producto a eliminar: ')
    if name in inventory:
        del inventory[name.capitalize()]
    else:
        print('El producto no existe')

# funcion para mostrar inventario
def show_inventory(inventory):
    print(f'Producto'{inventory[key]})
print()




while True:
    main_menu()
    option = input('Seleccione una opción: ')
    if option == '1':
        add_product(inventory)
    elif option == '2':
        remove_product(inventory)
    if option == '3':
        show_inventory(inventory)
    if option == '4':
        break