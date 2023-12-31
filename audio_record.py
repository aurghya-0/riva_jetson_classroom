import pyaudio
import wave

class AudioRecord:
    def __init__(self, 
                 chunk=1024, 
                 sample_format=pyaudio.paInt16, 
                 channels=2, fs=44100, 
                 seconds=10, 
                 filename="output.wav"):
        self.chunk = chunk
        self.sample_format = sample_format
        self.channels = channels
        self.fs = fs
        self.seconds = seconds
        self.filename = filename

    # Record a wav file
    def record(self):
        p = pyaudio.PyAudio()

        print("Recording...")
        stream = p.open(format=self.sample_format,
                        channels=self.channels,
                        rate=self.fs,
                        frames_per_buffer=self.chunk,
                        input=True)

        frames = []

        for i in range(0, int(self.fs / self.chunk * self.seconds)):
            data = stream.read(self.chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        print("Finished recording.")
        wf = wave.open(self.filename, "wb")
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b"".join(frames))
        wf.close()

        