import os, sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

data_dir = os.path.abspath(
    os.path.join(sys.prefix, 'share','cil')
)

pics = ['boat.tiff', 'camera.png', 'rainbow.png', 'resolution_chart.tiff', 'shapes.png']
for which in pics:
    dpath = os.path.join(data_dir, which)
    with Image.open(dpath) as f:
        print("opening {}".format(dpath))
        bands = f.getbands()
        if len(bands) > 1:
            if len(bands) == 4:
                f = f.convert('RGB')
                bands = f.getbands()
        plt.imshow(f)
        plt.show()

