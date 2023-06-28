import asyncio
import random
from datetime import timedelta
from typing import Iterable

from mingus.containers import Note, NoteContainer
from mingus.core import notes
from mingus.midi.fluidsynth import FluidSynthSequencer


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


async def main():
    sequencer = Sequencer("Wii Grand Piano.sf2")
    test_chore = [Note("C", 5), Note("E", 5), Note("G", 5)]
    await sequencer.play_notes(test_chore, timedelta(seconds=1))

    print("欢迎使用乐感测试! 请键入正确的音名.")

    while True:
        print("请聆听标准音 A-4 (440 Hz)")
        for _ in range(3):
            await sequencer.play_note(Note("A", 4), timedelta(seconds=0.5))
            await asyncio.sleep(0.5)

        note = Note()
        note.from_int(random.randint(48 - 12, 48 + 12))
        await sequencer.play_note(note, timedelta(seconds=1))

        while True:
            inp = input("请输入音名: ").strip().upper()
            if notes.is_valid_note(inp):
                break
            print(
                "输入格式有误!\n"
                "格式: 音名 + 升降号 (如降 B 请输入 Bb, 升 F 请输入 F#. 注意, 音名必须大写)"
            )

        print("正确! " if inp == note.name else f"错误! 正确答案是 {note.name}")


if __name__ == "__main__":
    asyncio.run(main())
