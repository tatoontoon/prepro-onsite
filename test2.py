"""ขนมตู้"""
def main():
    """ขนม"""
    money = int(input())
    water = int(input())
    snack_1 = int(input())
    snack_2 = int(input())
    snack_3 = int(input())
    kanom_1 = (money - water)%3
    print(kanom_1)
main()
