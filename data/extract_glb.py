import numpy as np
import matplotlib.pyplot as plt

from habitat_sim.utils.data import ImageExtractor

# For viewing the extractor output
def display_sample(sample, name):
    img = sample["rgba"]
    depth = sample["depth"]
    semantic = sample["semantic"]

    arr = [img, depth, semantic]
    titles = ["rgba", "depth", "semantic"]
    plt.figure(figsize=(12, 8))
    plt.imshow(img)
    plt.savefig(name + '.png')

    plt.show()

scene_filepath = "./Stokes.glb"

extractor = ImageExtractor(
    scene_filepath,
    img_size=(512, 512),
    output=["rgba", "depth", "semantic"],
)

# Use the list of train outputs instead of the default, which is the full list
# of outputs (test + train)
extractor.set_mode('train')
print(extractor)
# Index in to the extractor like a normal python list
sample = extractor[0]

# Or use slicing
ii = 0
samples = extractor[0:len(extractor)]
for sample in samples:
    display_sample(sample, "sample" + str(ii))
    ii+=1

# Close the extractor so we can instantiate another one later
# (see close method for detailed explanation)
extractor.close()
