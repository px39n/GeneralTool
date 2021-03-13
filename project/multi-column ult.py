from scipy.io import loadmat
import numpy as np
import math
import matplotlib.pylab as plt

import random

gt_path="D:\Code\GeneralTool\File\GT_IMG_1.mat"
image_path="D:\Code\GeneralTool\File\IMG_1.jpg"

label_data = loadmat(gt_path)
points = label_data['image_info'][0][0]['location'][0][0]
crowd_count = label_data['image_info'][0][0]['number'][0][0]

def random_crop_img(img, points, crop_size=256):
    h, w = img.shape[0], img.shape[1]
    if h < crop_size or w < crop_size:
        crop_size = crop_size // 2
    x1 = random.randint(0, h - crop_size)
    y1 = random.randint(0, w - crop_size)
    x2 = x1 + crop_size
    y2 = y1 + crop_size

    cropped_img = img[x1:x2, y1:y2, ...]

    cropped_points = []
    for i in range(len(points)):
        if x1 <= points[i, 1] <= x2 and y1 <= points[i, 0] <= y2:
            points[i, 0] = points[i, 0] - y1
            points[i, 1] = points[i, 1] - x1
            cropped_points.append(points[i])
    cropped_points = np.asarray(cropped_points)

    for i in range(len(cropped_points)):
        cropped_points[i] = cropped_points[i] / 4

    return cropped_img, cropped_points

img,points=random_crop_img(plt.imread(image_path),points)

def fspecial(ksize, sigma):
    """
    Generates 2d Gaussian kernel
    """
    # [left, right)
    left = -ksize / 2 + 0.5
    right = ksize / 2 + 0.5
    x, y = np.mgrid[left:right, left:right]
    # generate 2d Gaussian Kernel by normalization
    gaussian_kernel = np.exp(-(np.square(x) + np.square(y)) / (2 * np.power(sigma, 2))) / (2 * np.power(sigma, 2)).sum()
    sum = gaussian_kernel.sum()
    normalized_gaussian_kernel = gaussian_kernel / sum

    return normalized_gaussian_kernel
def get_avg_distance(position, points, k):
  """
  Compu
  """
  num = len(points)
  if num == 1:
      return 1.0
  elif num <= k:
      k = num - 1
  euclidean_distance = np.zeros((num, 1))
  for i in range(num):
      x = points[i, 1]
      y = points[i, 0]
      # Euclidean distance
      euclidean_distance[i, 0] = math.sqrt(math.pow(position[1] - x, 2) + math.pow(position[0] - y, 2))

  # the all distance between current point and other points
  euclidean_distance[:, 0] = np.sort(euclidean_distance[:, 0])
  avg_distance = euclidean_distance[1:k + 1, 0].sum() / k
  return avg_distance

def get_density_map(points, knn_phase, k=2, scaled_min_head_size=2, scaled_max_head_size=30):
  h, w = 64,64
  density_map = np.zeros((h, w))
  # In case that there is no one in the image
  num = len(points)
  if num == 0:
      return density_map
  for i in range(num):
      x = min(h, max(0, abs(int(math.floor(points[i, 1])))))
      y = min(w, max(0, abs(int(math.floor(points[i, 0])))))
      # now for a specific point, it represents as position[x, y]

      position = [x, y]

      sigma = 1.5
      beta = 0.3
      ksize = 25
      if knn_phase:
          avg_distance = get_avg_distance(position, points, k=k)
          avg_distance = max(min(avg_distance, scaled_max_head_size), scaled_min_head_size)
          sigma = beta * avg_distance
          ksize = 1.0 * avg_distance

      # Edge processing
      x1 = x - int(math.floor(ksize / 2))
      y1 = y - int(math.floor(ksize / 2))
      x2 = x + int(math.ceil(ksize / 2))
      y2 = y + int(math.ceil(ksize / 2))

      if x1 < 0 or y1 < 0 or x2 > h or y2 > w:
          x1 = max(0, x1)
          y1 = max(0, y1)
          x2 = min(h, x2)
          y2 = min(w, y2)

          tmp = x2 - x1 if (x2 - x1) < (y2 - y1) else y2 - y1
          ksize = min(tmp, ksize)

      ksize = int(math.floor(ksize / 2))
      H = fspecial(ksize, sigma)
      density_map[x1:x1 + ksize, y1:y1 + ksize] = density_map[x1:x1 + ksize, y1:y1 + ksize] + H
  return np.asarray(density_map)

map=get_density_map(points,True)

print(1)
plt.figure(figsize=(4,4))

plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(map)
plt.axis('off') # 不显示坐标轴
plt.show()
print(map.sum())
print(1)