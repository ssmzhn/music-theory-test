from mingus.midi import fluidsynth
from mingus.containers import Note, NoteContainer
from time import sleep
from mingus.core import notes
from random import randint
fluidsynth.init('Wii Grand Piano.sf2')
fluidsynth.play_NoteContainer(NoteContainer(["C-5", "E-5", "G-5"]))
sleep(1)
fluidsynth.stop_NoteContainer(NoteContainer(["C-5", "E-5", "G-5"]))

def test():
    while True:
        print('请聆听标准音 A-4 (440 Hz)')
        for x in range(3):
            fluidsynth.play_Note(Note('A-4'))
            sleep(0.5)
            fluidsynth.stop_Note(Note('A-4'))
            sleep(0.5)
        tone = randint(48 - 12, 48 + 12)
        tone_note = Note()
        fluidsynth.play_Note(tone_note.from_int(integer=tone))
        sleep(1)
        fluidsynth.stop_Note(tone_note.from_int(integer=tone))
        inp = ''
        while True:
            inp = input('请输入音名: ')
            if not notes.is_valid_note(inp):
                print('输入格式有误! ')
                print('格式: 音名 + 升降号 (如降 B 请输入 Bb, 升 F 请输入 F#. 注意, 音名必须大写.')
            else:
                break
        if tone % 12 == notes.note_to_int(inp) % 12:
            print('正确! ')
        else:
            print('错误! 正确答案是 {}'.format(notes.int_to_note(tone%12)))

if __name__ == "__main__":
    print('欢迎使用乐感测试! 请键入正确的音名.')
    test()
