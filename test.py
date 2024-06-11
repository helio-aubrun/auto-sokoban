import numpy as np

def find_value(matrix, value):
    """Trouve la position de la valeur dans la matrice."""
    result = np.where(matrix == value)
    positions = list(zip(result[0], result[1]))
    if positions:
        return positions[0]  # Retourne la première position trouvée
    else:
        return None

def move_value(matrix, value, target_pos):
    """Déplace la valeur vers la position cible."""
    current_pos = find_value(matrix, value)
    if current_pos:
        matrix[current_pos] = 0
        matrix[target_pos] = value
    else:
        raise ValueError(f"Valeur {value} non trouvée dans la matrice.")
    return matrix

def align_value(matrix, value, pos1, pos2):
    row1, col1 = pos1
    row2, col2 = pos2
    
    if row1 == row2:  # Alignement horizontal
        # Trouver la colonne libre adjacente à col1 ou col2
        if col1 > 0 and matrix[row1, col1-1] == 0:
            target_pos = (row1, col1-1)
        elif col2 > 0 and matrix[row2, col2-1] == 0:
            target_pos = (row2, col2-1)
        elif col1 < matrix.shape[1] - 1 and matrix[row1, col1+1] == 0:
            target_pos = (row1, col1+1)
        elif col2 < matrix.shape[1] - 1 and matrix[row2, col2+1] == 0:
            target_pos = (row2, col2+1)
        else:
            raise ValueError("Pas de position libre pour aligner la valeur.")
            
    elif col1 == col2:  # Alignement vertical
        # Trouver la ligne libre adjacente à row1 ou row2
        if row1 > 0 and matrix[row1-1, col1] == 0:
            target_pos = (row1-1, col1)
        elif row2 > 0 and matrix[row2-1, col2] == 0:
            target_pos = (row2-1, col2)
        elif row1 < matrix.shape[0] - 1 and matrix[row1+1, col1] == 0:
            target_pos = (row1+1, col1)
        elif row2 < matrix.shape[0] - 1 and matrix[row2+1, col2] == 0:
            target_pos = (row2+1, col2)
        else:
            raise ValueError("Pas de position libre pour aligner la valeur.")
            
    else:
        raise ValueError("Les deux valeurs ne sont ni alignées horizontalement ni verticalement.")
    
    return move_value(matrix, value, target_pos)

# Exemple d'utilisation
matrix = np.zeros((5, 5), dtype=int)
matrix[2, 2] = 1  # Première valeur alignée
matrix[2, 3] = 2  # Deuxième valeur alignée
matrix[0, 0] = 3  # Valeur à aligner

print("Matrice avant alignement :")
print(matrix)

matrix = align_value(matrix, 3, (2, 2), (2, 3))

print("Matrice après alignement :")
print(matrix)
