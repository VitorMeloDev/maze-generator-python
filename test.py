import random

WALL_NORTH = 1
WALL_EAST = 2
WALL_SOUTH = 4
WALL_WEST = 8

rows = 10
cols = 10
start = (0, 0)

# O jeito correto: uma lista de listas
grid = [[15 for col in range(cols)] for row in range(rows)]

visited = []
stack = []

def generate_maze():
    current = start
    visited.append(current)
    stack.append(current)

    while stack:
        next = get_neigh(current)

        if next:
            remove_walls(current, next)
            current = next
            visited.append(current)
            stack.append(current)
        elif stack:
            current = stack.pop()
        else:
            break

def remove_walls(current, next):
    cX, cY = current
    nX, nY = next

    if nX > cX:
        grid[cY][cX] &= ~WALL_EAST
        grid[nY][nX] &= ~WALL_WEST
    elif nX < cX:
        grid[cY][cX] &= ~WALL_WEST
        grid[nY][nX] &= ~WALL_EAST

    if nY > cY:
        grid[cY][cX] &= ~WALL_SOUTH
        grid[nY][nX] &= ~WALL_NORTH
    elif nY < cY:
        grid[cY][cX] &= ~WALL_NORTH
        grid[nY][nX] &= ~WALL_SOUTH

def get_neigh(item):
    nei = []
    x, y = item

    if y > 0 and (x, y - 1) not in visited:
        nei.append((x, y - 1))
    if y < rows - 1 and (x, y + 1) not in visited:
        nei.append((x, y + 1))
    if x > 0 and (x - 1, y) not in visited:
        nei.append((x - 1, y))
    if x < cols -1 and (x + 1, y) not in visited:
        nei.append((x + 1, y))

    return random.choice(nei) if nei else False


def print_hex_grid() -> None:
    """Mostra a matriz em Hexadecimal (como exige o PDF)."""
    for row in grid:
        # Pega cada número (0 a 15) e converte para Hexadecimal maiúsculo (0-F)
        print("".join(f"{cell:X}" for cell in row))

def draw_terminal_maze():
    """Desenha as paredes do labirinto de forma visual no terminal."""
    print("+" + "---+" * cols)  # Desenha o teto do labirinto completo

    for y in range(rows):
        # Linha para o conteúdo da célula e paredes laterais (Leste/Oeste)
        row_str = "|"
        for x in range(cols):
            cell = grid[y][x]
            # Se tiver a parede leste (EAST = 2), coloca "|", senão deixa vazio
            if cell & WALL_EAST:
                row_str += "   |"
            else:
                row_str += "    "
        print(row_str)

        # Linha para as paredes de baixo (Sul)
        bottom_str = "+"
        for x in range(cols):
            cell = grid[y][x]
            # Se tiver a parede sul (SOUTH = 4), coloca "---", senão deixa vazio
            if cell & WALL_SOUTH:
                bottom_str += "---+"
            else:
                bottom_str += "   +"
        print(bottom_str)


# --- Teste de Execução ---
print("Grid Inicial (Tudo Fechado):")
print_hex_grid()

# Movendo de (0,0) para (0,1) -> Baixo (Sul)
# remove_walls((0,0), (0, 1))

# --- Teste de Execução ---
print("Labirinto em Hexadecimal:")
generate_maze()
print_hex_grid()

print("\nVisualização do Labirinto:")
draw_terminal_maze()
