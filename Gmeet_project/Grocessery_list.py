def get_prod_input():
    product = input("Enter the product name: ")
    Quantity = int(input("Enter your Quantity: "))
    Price = int(input("Enter the price: "))
    return product, Quantity, Price

def cal_total(quantity, price):
    total = quantity * price
    return total

def bill_total(product, quantity, price, total):
    print("---- grocerry bill ----")
    print("product name: ", product)
    print("Quantity: ", quantity)
    print("Price: ", price)
    print("Total: ", total)

def main():
    product, quantity, price = get_prod_input()
    total = cal_total(quantity, price)
    bill_total(product, quantity, price, total)
    
main()