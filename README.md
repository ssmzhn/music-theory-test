# music-theory-test
A simple music theory test.

## Usage

If you haven't installed `mingus` and `fluidsynth`, then you should install them via:

``` 
pip install -r requirements.txt
```

Then

```
python main.py
```

Enjoy it!

## For Windows Users

If this error occurs:

```
C:\Users\21720\Desktop\music-theory-test-main>python main.py
Traceback (most recent call last):
  File "C:\Users\21720\Desktop\music-theory-test-main\main.py", line 9, in <module>
    from sequencer import Sequencer
  File "C:\Users\21720\Desktop\music-theory-test-main\sequencer.py", line 2, in <module>
    from mingus.midi.fluidsynth import FluidSynthSequencer
  File "C:\Users\21720\AppData\Local\Programs\Python\Python310\lib\site-packages\mingus\midi\fluidsynth.py", line 41, in <module>
    from mingus.midi import pyfluidsynth as fs
  File "C:\Users\21720\AppData\Local\Programs\Python\Python310\lib\site-packages\mingus\midi\pyfluidsynth.py", line 41, in <module>
    raise ImportError("Couldn't find the FluidSynth library.")
ImportError: Couldn't find the FluidSynth library.
```

Then you may refer to [this issue](https://github.com/aniawsz/rtmonoaudio2midi/issues/6#issuecomment-864448495).

If it doesn't work, try to copy the `libfluidsynth64.dll` file to `%WINDIR%\System32` or add the directory in which the .dll file is to PATH.

## License

GPL-3.0
