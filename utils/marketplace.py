"""
Author: Fabio Daros start in 14.02.204
"""

from typing import List, Dict
from time import sleep
from models.product import Product
from utils.helper import format_float_coin

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('==================================')
    print('============ Welcome =============')
    print('========== Marketplace ===========')
    print('==================================')
    print('Select an option: ')
    print('1. Register products')
    print('2. List products')
    print('3. Buy products')
    print('4. View cart')
    print('5. Close order')
    print('6. Exit')
    print('----------------------------------')

    option: int = int(input('Option: '))

    if option == 1:
        register_product()
    elif option == 2:
        list_products()
    elif option == 3:
        buy_product()
    elif option == 4:
        view_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print('Thank you for your business!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option')
        sleep(1)
        menu()


def register_product() -> None:
    print('================')
    print('Register Product')
    print('================')

    name: str = input('Name: ')
    price: float = float(input('Price: '))

    product: Product = Product(name, price)

    products.append(product)
    sleep(1)
    print(f'Product {product.name} registered successfully!')
    sleep(2)
    menu()


def list_products() -> None:
    if len(products) > 0:
        print('-----------------')
        print('List of products:')
        print('-----------------')
        for product in products:
            print(product)
            print('----------------')
            sleep(1)
    else:
        print('No products registered yet!')
    sleep(2)
    menu()


def buy_product() -> None:
    if len(products) > 0:
        print('Enter the product code to add to cart: ')
        print('---------------------------------------')
        print('========= Available Products ==========')
        for product in products:
            print(product)
            print('-----------------------------------')
            sleep(1)
        code: int = int(input())

        product: Product = get_product_by_code(code)

        if product is not None:
            if len(cart) > 0:
                have_in_cart: bool = False
                for item in cart:
                    qt: int = item.get(product)
                    if qt:
                        item[product] = qt + 1
                        print(f'The product {product.name} now have {qt + 1} units in the cart.')
                        have_in_cart = True
                        sleep(2)
                        menu()
                if not have_in_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'Product {product.name} added to cart!')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'Product {product.name} added to cart!')
                sleep(2)
                menu()
        else:
            print('Invalid product code!')
            sleep(2)
            menu()
    else:
        print('No products registered yet!')
        sleep(2)
        menu()


def view_cart() -> None:
    if len(cart) > 0:
        print('Product(s) in cart: ')

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('---------------------')
                sleep(1)
                menu()
    else:
        print('Cart is empty!')
        sleep(2)
        menu()


def close_order() -> None:
    if len(cart) > 0:
        total_value: float = 0

        print('Cart Items: ')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total_value += data[0].price * data[1]
                print('---------------------')
        print(f'Your invoice is {format_float_coin(total_value)}')
        print('Thank You! Always Time!')
        cart.clear()
        sleep(5)
    else:
        print('Cart is empty!')
        sleep(2)
        menu()


def get_product_by_code(code: int) -> Product:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p


if __name__ == '__main__':
    main()
