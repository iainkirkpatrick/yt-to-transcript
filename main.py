import os
from sys import argv
from pytube import YouTube
from moviepy.editor import VideoFileClip
import whisper

def download_video(youtube_url, output_path):
  # Download the video
  yt = YouTube(youtube_url)
  video_id = yt.video_id
  video_file_name = f"{video_id}.mp4"
  video_file_path = os.path.join(output_path, video_file_name)

  if os.path.exists(video_file_path):
    print(f"Video already downloaded at: {video_file_path}")
    return video_file_path
  
  stream = yt.streams.filter(only_audio=False).first()
  downloaded_file_path = stream.download(output_path, filename=video_file_name)
  return downloaded_file_path

def extract_audio(video_path, output_path):
  base_name = os.path.basename(video_path)
  audio_file_name = os.path.splitext(base_name)[0] + ".mp3"
  audio_file_path = os.path.join(output_path, audio_file_name)

  if os.path.exists(audio_file_path):
    print(f"Audio already exists: {audio_file_path}")
    return audio_file_path
  
  video_clip = VideoFileClip(video_path)
  audio_clip = video_clip.audio
  audio_clip.write_audiofile(audio_file_path)
  audio_clip.close()
  video_clip.close()
  return audio_file_path

def save_transcription(transcription, output_path):
  with open(output_path, 'w') as f:
      f.write(transcription)

def main():
  if len(argv) < 2:
    print("Error: must use with args like python main.py <youtube_url>")
    exit(1)
  else:
    youtube_url = argv[1]

    video_dir = './videos'
    audio_dir = './audio' 
    transcription_dir = './transcripts'
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(transcription_dir, exist_ok=True)

    video_path = download_video(youtube_url, video_dir)
    audio_file_path = extract_audio(video_path, audio_dir)
    print(f"Audio extracted and saved to: {audio_file_path}")

    model = whisper.load_model("base")
    result = model.transcribe(audio_file_path)
    transcription = result["text"]
    transcription_file_path = os.path.join(transcription_dir, os.path.splitext(os.path.basename(audio_file_path))[0] + ".txt")
    save_transcription(transcription, transcription_file_path)
    print(f"Transcription saved to: {transcription_file_path}")

if __name__ == "__main__":
  main()
