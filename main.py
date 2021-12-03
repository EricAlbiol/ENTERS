# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    n1 = int(input("Introdueix el primer enter: "))
    n2 = int(input("Introdueix el segon enter: "))
    aux = n1
    if n1 < n2:
        while aux < n2+1:
            print(aux)
            aux+=1
    else:
        while n1 > n2:
            print("error")
            n1 = int(input("Introdueix el primer enter: "))
            n2 = int(input("Introdueix el segon enter: "))
            aux = n1
            while aux < n2+1:
                print(aux)
                aux += 1
if __name__ == '__main__':
    main()

