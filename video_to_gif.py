from moviepy.editor import *

clip = (VideoFileClip("1.mp4").subclip((0.2),(0.5)))
clip.write_gif("output.gif")
print("completed")
