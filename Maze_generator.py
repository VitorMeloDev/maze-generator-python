# 1. Definimos o valor numérico de cada muro
WALL_NORTH = 1
WALL_EAST  = 2
WALL_SOUTH = 4
WALL_WEST  = 8

# 2. Criamos o Grid 3x3 zerado (tudo 15 = F)
grid = [
    [15, 15, 15],
    [15, 15, 15],
    [15, 15, 15]
]

def open_wall(x1: int, y1: int, x2: int, y2: int) -> None:
    """Abre o muro entre a célula (x1,y1) e sua vizinha (x2,y2)."""
    # Mover para a Direita (Leste)
    if x2 > x1:
        grid[y1][x1] &= ~WALL_EAST   # Subtrai/desliga o bit Leste da atual
        grid[y2][x2] &= ~WALL_WEST   # Subtrai/desliga o bit Oeste da vizinha
    # Mover para Baixo (Sul)
    elif y2 > y1:
        grid[y1][x1] &= ~WALL_SOUTH  # Subtrai/desliga o bit Sul da atual
        grid[y2][x2] &= ~WALL_NORTH  # Subtrai/desliga o bit Norte da vizinha

def print_hex_grid() -> None:
    """Mostra a matriz em Hexadecimal (como exige o PDF)."""
    for row in grid:
        # Pega cada número (0 a 15) e converte para Hexadecimal maiúsculo (0-F)
        print("".join(f"{cell:X}" for cell in row))

print("--- 1. Matriz 3x3 Inicial (Tudo Fechado) ---")
print_hex_grid()

# PASSO A: Abrir passagem da célula (0,0) para a (1,0) [Direita]
open_wall(0, 0, 1, 0)

print("\n--- 2. Passagem (0,0) -> (1,0) Aberta ---")
print_hex_grid()

# PASSO B: Abrir passagem da célula (1,0) para a (1,1) [Baixo]
open_wall(1, 0, 1, 1)

print("\n--- 3. Passagem (1,0) -> (1,1) Aberta ---")
print_hex_grid()