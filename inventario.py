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
        try:
            stock = int(input('Ingrese el stock del producto: '))
            inventory[name.capitalize()] = stock
        except:
            print('Ingrese un valor correcto')
            
def remove_product(inventory):
    name = input('Ingrese el nombre del producto a eliminar: ')
    if name in inventory:
        del inventory[name]
    else:
        print('El producto no existe')
    
def show_inventory(inventory):
    print(inventory)
print()


inventory = {}

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