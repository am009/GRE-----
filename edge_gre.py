
gres = []
with open('gre长难句.txt', 'r') as f:
    gres = f.readlines()

import asyncio,os

import edge_tts

voice_map = {"male": "en-US-EricNeural",
"female": "en-US-MichelleNeural"}

async def create_one(text, voice, file) -> None:
    communicate = edge_tts.Communicate(text, voice, rate="-20%")
    await communicate.save(file)

async def main() -> None:
    i = 0
    for sentence in gres:
        i += 1
        print(f'###{i}###: {sentence}')
        for ty in voice_map:
            out = os.path.join("out", f'{i}-{ty}.mp3')
            await create_one(sentence, voice_map[ty], out)
            # exit()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
