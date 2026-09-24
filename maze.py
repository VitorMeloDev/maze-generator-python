from random import choice

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

cols = 3
rows = 3
start = (0, 0)
end = (2, 2)
visited = []
stack = []

def create_maze():
    if not grid:
        return
    
    current = start
    visited.append(current)

    while len(visited) < (rows * cols):
        next_cell = check_next(current)
        
        if next_cell:
            remove_walls(current, next_cell)
            stack.append(current)
            current = next_cell
            visited.append(current)
        elif stack:
            # Só faz o pop se ainda houver elementos na pilha
            current = stack.pop()
        else:
            # Se não há vizinhos livres E a pilha esvaziou, o labirinto acabou!
            break


def check_next(pos):
    nei = []
    x, y = pos

    # CIMA: Garante que não vai subir além da linha 0
    if y > 0 and (x, y - 1) not in visited:
        nei.append((x, y - 1))

    # BAIXO: Garante que não vai descer além da última linha
    if y < rows - 1 and (x, y + 1) not in visited:
        nei.append((x, y + 1))

    # ESQUERDA: Garante que não vai para a esquerda além da coluna 0
    if x > 0 and (x - 1, y) not in visited:
        nei.append((x - 1, y))

    # DIREITA: Garante que não vai para a direita além da última coluna
    if x < cols - 1 and (x + 1, y) not in visited:
        nei.append((x + 1, y))

    return (choice(nei)) if nei else False

def remove_walls(current, next_cell):
    cX, cY = current
    nX, nY = next_cell

    # IMPORTANTE: Acessamos como grid[linha][coluna], ou seja, grid[y][x]
    
    # Movimento Horizontal (Eixo X)
    if nX > cX: # Foi para a direita (Leste)
        grid[cY][cX] &= ~WALL_EAST
        grid[nY][nX] &= ~WALL_WEST
    elif nX < cX: # Foi para a esquerda (Oeste)
        grid[cY][cX] &= ~WALL_WEST
        grid[nY][nX] &= ~WALL_EAST
        
    # Movimento Vertical (Eixo Y)
    elif nY > cY: # Foi para baixo (Sul)
        grid[cY][cX] &= ~WALL_SOUTH
        grid[nY][nX] &= ~WALL_NORTH
    elif nY < cY: # Foi para cima (Norte)
        grid[cY][cX] &= ~WALL_NORTH
        grid[nY][nX] &= ~WALL_SOUTH

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
create_maze()
print_hex_grid()

print("\nVisualização do Labirinto:")
draw_terminal_maze()
