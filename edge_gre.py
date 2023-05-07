import asyncio
import os
import edge_tts

gres = []
with open('gre长难句.txt', 'r') as f:
    gres = f.readlines()
gmats = []
with open('gmat长难句.txt', 'r') as f:
    gmats = f.readlines()

voice_map = {"male": "en-US-EricNeural",
             "female": "en-US-MichelleNeural"}


def write_lrc(path, text):
    from pylrc.classes import Lyrics, LyricLine
    lrc = Lyrics([LyricLine("[00:00]", text), LyricLine("[59:00]")])
    with open(path, 'w') as f:
        f.write(lrc.toLRC())


async def create_one(text, voice, file, gen_lrc=True) -> None:
    communicate = edge_tts.Communicate(text, voice, rate="-20%")
    await communicate.save(file)
    if gen_lrc:
        write_lrc(file.removesuffix('.mp3')+'.lrc', text)


async def gen_sentences(sentences: list[str], out_folder='out', only=None) -> None:
    """generate for all or some of the sentences.

    Args:
        sentences (list[int]): a list of english sentences
        out_folder (str, optional): output folder name. Defaults to 'out'.
        only (list[int], optional): a list of line numbers, only generate for these sentences. Defaults to None.
    """
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    for i, sentence in enumerate(sentences):
        ind = i + 1
        print(f'###{ind}###: {sentence}')
        for ty in voice_map:
            out = os.path.join(out_folder, f'{ind:03d}-{ty}.mp3')
            # '--' will not pause, change to comma.
            await create_one(sentence.replace('--', ', '), voice_map[ty], out)


async def main() -> None:
    await gen_sentences(gres, "GRE语音")
    await gen_sentences(gmats, "GMAT语音")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
