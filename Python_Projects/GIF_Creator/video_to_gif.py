import moviepy.editor 

clip = (moviepy.editor.VideoFileClip("production_id_3833491 (1080p).mp4").subclip((2.25),(6.25))
        .resize(0.3))
clip.write_gif("output.gif")