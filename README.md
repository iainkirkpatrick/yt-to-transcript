# yt-to-transcript

I wanted to read [Rasumus Andersson's chat about Playbit on the Local First Podcast](https://www.youtube.com/watch?v=46ROIJ2NtKM) rather than watch it - I sometimes prefer reading long videos to spending a couple of hours watching!

With Whisper available, why not have a little tool to transcribe for me?

Requires ffmpeg installed on the host machine as per [Whisper installation instructions](https://github.com/openai/whisper?tab=readme-ov-file#setup).

## notes
- would be cool if the tool could look at a incoming stream (i.e. the audio stream) of my computer, and pipe that into a transcription service running locally? is that possible?
  - https://rogueamoeba.com/audiohijack/
  - https://github.com/ExistentialAudio/BlackHole/