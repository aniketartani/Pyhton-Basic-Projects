import moviepy.editor


video=moviepy.editor.VideoFileClip("1.mp4")
audio=video.audio
audio.write_audiofile("sample.mp3")
print("completeD")
