# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MCPI must be open and in a world at
#this time)
mc = Minecraft.create()

x = input("X Coordinate: ")
y = input("Y Coordinate: ")
z = input("Z Coordinate: ")

x = int(x)
y = int(y)
z = int(z)

width = 10
height = 10
length = 10

mc.setBlocks(x, y, z, x + width, y + height, z + length, 3)
mc.setBlocks(x + 1, y, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)