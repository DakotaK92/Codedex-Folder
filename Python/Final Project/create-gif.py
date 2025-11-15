import imageio.v3 as iio

filenames = ['pic-1-of-me.png', 'pic-2-of-me.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('pictures-of-me.gif', images, duration = 500, loop = 0)