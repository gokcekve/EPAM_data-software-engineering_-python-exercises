import time

def create_grid():
    return [['1' for _ in range(6)] for _ in range(6)]

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n")

def drop_R(grid, col, row):
    # Kullanıcının inputunu index'e çevir (index 0 tabanlı)
    col -= 1
    row -= 1

    # 'R' yerleştir:
    grid[row][col] = 'R'
    print("R placed: ")
    print_grid(grid)
    time.sleep(1)   # 1 saniye bekle

    # 'R' yi kaydır, her adımı yazdır
    for r in range(row, 5):
        if grid[r + 1][col] == '1':
            grid[r][col] = '1'  # Rnin önceki konumu:   R -> 1 diye değiştir
            grid[r + 1][col] = 'R'  # Rnin yeni konumu:   1 -> R diye değiştir
            if r + 1 != 5:
                print("R is scrolling down: ")
                print_grid(grid)
                time.sleep(1)

def main():
    grid = create_grid()
    print("Initial Grid:")
    print_grid(grid)

    while True:
        # try-ecept kullanıcı geçersiz input girerse kontrol amaçlı bir yapı
        # Eğer input geçerli bir değerse kod çalışır değilse hata verir.
        try:
            col = int(input("Enter column (1-6): "))
            row = int(input("Enter row (1-6): "))

            if not (1 <= col <= 6) or not (1 <= row <= 6):
                print("Please enter values between 1 and 6.")
                continue

            drop_R(grid, col, row)
            print("FINAL GRID: ")
            print_grid(grid)

        #ValueError: spesifik bir hata mesajı; kullancı sayı yerine harf vs girmeye kalkarsa kod hata verecek.
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
