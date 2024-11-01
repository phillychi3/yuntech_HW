from PIL import Image
import matplotlib.pyplot as plt
import os

fig, axes = plt.subplots(4, 13, figsize=(10, 5))
c = 1
thisfilepos = os.path.dirname(os.path.abspath(__file__))

for i in range(52):
    row, col = divmod(i, 13)
    try:
        img = Image.open(os.path.join(thisfilepos, f'cards/{i}.gif'))
        axes[row, col].imshow(img)
        axes[row, col].axis('off')
    except FileNotFoundError:
        print(f'Missing image:\n{os.path.join(thisfilepos, f"cards/{i}.gif")}')
        axes[row, col].axis('off')

plt.tight_layout()
plt.show()