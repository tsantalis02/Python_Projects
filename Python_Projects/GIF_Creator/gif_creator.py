import imageio
filenames = ["FB_IMG_1618076251281.jpg","profile_picture.jpg"]
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('new_gif.gif', images,'GIF',duration=1)


