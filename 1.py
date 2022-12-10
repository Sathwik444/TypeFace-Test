import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt


sys.setrecursionlimit(10**6)

x = [-1, 0, 0, 1]
y = [0, -1, 1, 0]

def dfs(i, j, vis, img, bb):
  bb[0], bb[1], bb[2], bb[3] = min(bb[0], i), min(bb[1], j), max(bb[2], i), max(bb[3], j)
  vis[i][j] = 1
  for k in range(0, 4):
    tx, ty = i+x[k], j+y[k]
    if tx < 0 or tx >= img.shape[0] or ty < 0 or ty >= img.shape[1] or (img[tx][ty] == 0) or vis[tx][ty] != 0:
      continue
    dfs(i+x[k], j+y[k], vis, img, bb)
  return

def boxed_white_spaces(path_to_image):
  img = cv2.imread(path_to_image, cv2.IMREAD_GRAYSCALE)
  vis = np.zeros(img.shape)
  ans = []
  img //= 255
  # print(len(img[0]), img.shape)
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      if img[i][j] and (vis[i][j] == 0):
        bb = [img.shape[0]+1, img.shape[1]+1, -1, -1]
        dfs(i, j, vis, img, bb)
        ans.append(bb.copy())
  
  for bd in ans:
    img[bd[0]][:] = 1
    img[:][bd[1]] = 1
    img[bd[2]][:] = 1
    img[:][bd[2]] = 1

  plt.imshow(img)
  return ans
  boxed_white_spaces("1.png")
