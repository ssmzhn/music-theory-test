from mingus.midi import sequencer
from mingus.midi.fluidsynth import FluidSynthSequencer
from mingus.containers import Note, NoteContainer
import asyncio
from datetime import timedelta
from typing import Iterable


class Sequencer:
    sequencer: FluidSynthSequencer

    def __init__(self, sound_font: str) -> None:
        sequencer = FluidSynthSequencer()
        sequencer.load_sound_font(sound_font)
        sequencer.start_audio_output(None)
        sequencer.fs.program_reset()
        self.sequencer = sequencer

    async def play_note(self, note: Note, last: timedelta) -> None:
        self.sequencer.play_Note(note)
        await asyncio.sleep(last.total_seconds())
        self.sequencer.stop_Note(note)

    async def play_notes(self, note: Iterable[Note], last: timedelta) -> None:
        container = NoteContainer(note)
        self.sequencer.play_NoteContainer(container)
        await asyncio.sleep(last.total_seconds())
        self.sequencer.stop_NoteContainer(container)

    async def play_texture(self, chord: list[Note] | tuple[Note]) -> None: # 劲爆织体
        beat = 0.15
        if len(chord) == 3:
            base, third, fifth = chord
            self.sequencer.play_Note(Note().from_int(int(base)-12))
            self.sequencer.play_Note(base)
            await asyncio.sleep(beat)
            self.sequencer.stop_Note(base)
            self.sequencer.play_Note(base)
            await asyncio.sleep(beat)
            self.sequencer.play_Note(third)
            await asyncio.sleep(beat)
            self.sequencer.play_Note(fifth)
            await asyncio.sleep(beat)
            self.sequencer.stop_Note(base)
            self.sequencer.stop_Note(third)
            self.sequencer.play_Note(third)
            await asyncio.sleep(beat)
            self.sequencer.play_Note(base)
            await asyncio.sleep(beat)
            self.sequencer.play_Note(fifth)
            await asyncio.sleep(beat)
            self.sequencer.play_Note(third)
            self.sequencer.stop_Note(base)
            await asyncio.sleep(beat)
            self.sequencer.stop_Note(Note().from_int(int(base)-12))
            self.sequencer.play_Note(Note().from_int(int(base)-12))
            self.sequencer.play_Note(Note().from_int(int(base)+12))
            await asyncio.sleep(beat)
            self.sequencer.play_Note(base)
            self.sequencer.stop_Note(fifth)
            await asyncio.sleep(beat)
            self.sequencer.play_Note(third)
            await asyncio.sleep(beat)
            self.sequencer.play_Note(fifth)
            self.sequencer.stop_Note(Note().from_int(int(base)+12))
            await asyncio.sleep(beat)
            self.sequencer.play_Note(base)
            await asyncio.sleep(beat)
            self.sequencer.stop_Note(third)
            self.sequencer.stop_Note(fifth)
            self.sequencer.play_Note(fifth)
            await asyncio.sleep(beat)
            self.sequencer.play_Note(third)
            await asyncio.sleep(beat)
            self.sequencer.play_Note(base)
            await asyncio.sleep(beat)
            self.sequencer.stop_Note(base)
            self.sequencer.stop_Note(third)
            self.sequencer.stop_Note(fifth)
