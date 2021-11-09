'''
Ibu Menyuruh andi ke pasar membeli 1 botol susu, dan bilamana ada telur. beli 1 botol susu dan 6 butir telur
'''
print("andi pergi ke pasar")
print("andi menanyakan apakah ada susu?")

stock_milk = 100
stock_egg = 10

if stock_milk > 0 :
    print(f"stok susu ada : {stock_milk} botol")
    print("andi menanyakan stock telur")

    if stock_egg > 0 :
        print(f"stok telur ada : {stock_egg} butir")
        print("andi membeli 1 botol susu dan 6 butir telur")
    else:
        print("telur habis")
        print("andi hanya membeli 1 botol susu")
else:
    print(f"susu habis")
    print("andi tidak jadi membeli susu")

print("andi pulang ke rumah")
print("andi menyerahkan belanjaan ke ibu")
