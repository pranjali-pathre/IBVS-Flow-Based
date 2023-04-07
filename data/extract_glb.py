import numpy as np
import matplotlib.pyplot as plt
import habitat_sim
import habitat_sim.registry as registry
from habitat_sim.utils.data import ImageExtractor, PoseExtractor

@registry.register_pose_extractor(name="random_pose_extractor")
# class RandomPoseExtractor(PoseExtractor):
#     def extract_poses(self, view, fp):
#         height, width = view.shape
#         num_random_points = 4
#         points = []
#         print(height, width)
#         while len(points) < num_random_points:
#             # Get the row and column of a random point on the topdown view
#             # row, col = np.random.randint(0, height/8), np.random.randint(0, width/8)

#             row, col = np.random.randint(0, height/2), np.random.randint(0, width/2)
#             print(row, col)
#             # Convenient method in the PoseExtractor class to check if a point
#             # is navigable
#             if self._valid_point(row, col, view):
#                 points.append((row, col))

#         poses = []
#         # points = []
#         # point.append()

#         # Now we need to define a "point of interest" which is the point the camera will
#         # look at. These two points together define a camera position and angle
#         for point in points:
#             r, c = point
#             point_of_interest = (r - 1, c) # Just look forward
#             pose = (point, point_of_interest, fp)
#             poses.append(pose)

#         return poses

class RandomPoseExtractor(PoseExtractor):
    def extract_poses(self, view, fp):
        height, width = view.shape
        num_random_points = 4
        points = []
        print(height, width)
        while len(points) < num_random_points:
            # Get the row and column of a random point on the topdown view
            # row, col = np.random.randint(0, height/8), np.random.randint(0, width/8)

            # row, col = np.random.randint(0, height/2), np.random.randint(0, width/2)
            # print(row, col)

            # row, col = 65, 82 # From right
            row, col = 69, 63 # From front
            # row, col = 69, 50 # From left

            # Convenient method in the PoseExtractor class to check if a point
            # is navigable
            if self._valid_point(row, col, view):
                points.append((row, col))

        poses = []
        # points = []
        # point.append()

        # Now we need to define a "point of interest" which is the point the camera will
        # look at. These two points together define a camera position and angle
        for point in points:
            r, c = point
            point_of_interest = (r - 1, c) # Just look forward
            pose = (point, point_of_interest, fp)
            poses.append(pose)

        return poses

# For viewing the extractor output
def display_sample(sample, name):
    img = sample["rgba"]
    depth = sample["depth"]
    semantic = sample["semantic"]

    arr = [img, depth, semantic]
    titles = ["rgba", "depth", "semantic"]
    my_dpi = 96
    # plt.figure(frameon=False)
    plt.axis('off')
    plt.imshow(img)
    plt.savefig(name + '.png', bbox_inches='tight', pad_inches = 0, dpi=my_dpi)

    plt.show()

scene_filepath = "./skokloster-castle/Skokloster-castle.glb"
extractor = ImageExtractor(
    scene_filepath,
    img_size=(384, 512),
    output=["rgba", "depth", "semantic"],
    pose_extractor_name="random_pose_extractor"
)
# extractor = ImageExtractor(
#     scene_filepath,
#     img_size=(512, 512),
#     output=["rgba", "depth", "semantic"],
# )

extractor.set_mode('train')
print(extractor)
sample = extractor[0]

ii = 0
samples = extractor[0:len(extractor)]
for sample in samples:
    display_sample(sample, "sample" + str(ii))
    ii+=1

extractor.close()
