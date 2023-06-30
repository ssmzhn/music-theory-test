import asyncio
import random
from datetime import timedelta

from mingus.containers import Note
from mingus.core import notes, chords

from sequencer import Sequencer

async def single_note():
    sequencer = Sequencer("Wii Grand Piano.sf2")
    test_chore = [Note("C", 4), Note("E", 4), Note("G", 4)]
    await sequencer.play_notes(test_chore, timedelta(seconds=1))

    print("欢迎使用乐感测试! 请键入正确的音名.")
    while True:
        print("请聆听标准音 A-4 (440 Hz)")
        for _ in range(3):
            await sequencer.play_note(Note("A", 4), timedelta(seconds=0.5))
            await asyncio.sleep(0.5)

        note = Note()
        pitch = random.randint(48 - 12, 48 + 12)
        note.from_int(pitch)
        await sequencer.play_note(note, timedelta(seconds=1))

        while True:
            inp = input("请输入音名: ").strip()
            if notes.is_valid_note(inp):
                break
            print(
                "输入格式有误!\n"
                "格式: 音名 + 升降号 (如降 B 请输入 Bb, 升 F 请输入 F#. 注意, 音名必须大写)"
            )

        print("正确! " if inp == note.name else f"错误! 正确答案是 {note.name}")

async def chord_test(standard_note: bool=True) -> None:
    print('听和弦, 然后写出和弦名')
    sequencer = Sequencer("Wii Grand Piano.sf2")
    test_chore = [Note("C", 4), Note("E", 4), Note("G", 4)]
    for _ in range(2):
        await sequencer.play_texture(test_chore)
    await sequencer.play_notes(test_chore, timedelta(seconds=1))
    while True:
        if standard_note:
            print("请聆听标准音 A-4 (440 Hz)")
            for _ in range(3):
                await sequencer.play_note(Note("A", 4), timedelta(seconds=0.5))
                await asyncio.sleep(0.5)
        base_note = Note()
        pitch = random.randint(48 - 12, 48 + 12)
        base_note.from_int(pitch)
        list_of_chord_pitch_delta = { # 不用 chords 是因为我觉得 chords 不好写织体 (x
            "maj": (0, 4, 7),
            "m": (0, 3, 7),
            "dim": (0, 3, 6),
            "aug": (0, 4, 8)
        }
        chord_type, chord_pitch_delta = random.sample(list(list_of_chord_pitch_delta.items()),1)[0]
        chord = [Note().from_int(pitch+i) for i in chord_pitch_delta]
        await sequencer.play_notes(chord, timedelta(seconds=1))

        while True:
            inp = input("请输入和弦: ").strip()
            try:
                chords.from_shorthand(inp)
            except:
                print(
                    "输入格式有误!\n"
                    "格式: 根音 + 和弦属性 (如 C 大三和弦请输入 C 或 CM 或 Cmaj, 升 F 减三和弦请输入 F#dim. 注意, 根音必须大写)"
                )
            else:
                break
        if set([notes.note_to_int(i) for i in chords.from_shorthand(inp)]) == set([int(i)%12 for i in chord]):
            print("正确!")
        else:
            print(f"错误! 正确答案是 {base_note.name}{'' if chord_type == 'maj' else chord_type}")
            await sequencer.play_texture(chord)
            await sequencer.play_notes(chord, timedelta(seconds=1))

if __name__ == "__main__":
    print("欢迎使用乐感测试! \n"
          "请选择听辨单音或和弦: \n"
          "1. 单音\n"
          "2. 和弦"
        )
    while True:
        choice = input("请选择(1 或 2): ").strip()
        if choice == "1":
            asyncio.run(single_note())
            break
        elif choice == "2":
            asyncio.run(chord_test())
            break
        else:
            print("输入格式有误!\n")
