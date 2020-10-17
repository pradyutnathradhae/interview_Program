import numpy as np
def rotate_img(img_mat , n):
    rot_img = []
    y = n - 1
    while y != -1:
        x_temp = []
        for j in range(n):
            x_temp.append(img_mat[j][y])
        rot_img.append(x_temp)
        y -= 1
    return rot_img

def rotate_img_2(image_mat, n):
    for i in range(n):
        image_mat[i].reverse()
    image_mat = ((np.array(image_mat)).T).tolist()
    return image_mat

if __name__ == "__main__":
    n = int(input("Enter the number of rows :- "))
    image = []
    for i in range(n):
        image.append(list(map(int, input().split())))

    fin_img = rotate_img(image, n)
    for i in range(n):
        for j in range(n):
            print(fin_img[i][j], end = " ")
        print()