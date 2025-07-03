import numpy as np
import matplotlib.pyplot as plt

def checkerboard(square_size, rows, cols):
    # Kreiranje crnih i belih kvadrata
    black_square = np.zeros((square_size, square_size), dtype=np.uint8)
    white_square = np.ones((square_size, square_size), dtype=np.uint8) * 255

    # Kreiranje jednog reda
    row_even = np.hstack([black_square, white_square] * (cols // 2) + ([black_square] if cols % 2 else []))
    row_odd = np.hstack([white_square, black_square] * (cols // 2) + ([white_square] if cols % 2 else []))

    # Složimo redove da formiraju šah
    checkerboard = np.vstack([row_even, row_odd] * (rows // 2))

    return checkerboard

# Pravimo sliku 4x5 sa kvadratima veličine 50x50
img = checkerboard(50, 4, 5)

# Prikaz slike
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.xticks(np.arange(0, 251, 50)) 
plt.yticks(np.arange(0, 201, 50)) 
plt.show()