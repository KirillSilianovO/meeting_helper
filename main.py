from moviepy import VideoFileClip

def extract_audio() -> str:
    video_path = './input/input.webm'
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_path = './output/audio/audio.mp3'
    audio.write_audiofile(audio_path)
    return audio_path


def run():
    extract_audio()


if __name__ == "__main__":
    run()
