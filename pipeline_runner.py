
from moviepy.editor import VideoFileClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont

def merge_intro_outro(intro, main, outro, output):
    clips = [VideoFileClip(p) for p in [intro, main, outro]]
    final = concatenate_videoclips(clips)
    final.write_videofile(output)

def create_thumbnail(text, path="thumbnail.jpg"):
    img = Image.new('RGB', (1280, 720), color='white')
    d = ImageDraw.Draw(img)
    d.text((100, 300), text, fill='black')
    img.save(path)
    return path
