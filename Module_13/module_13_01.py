import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for number in range(5):
        print(f'Силач {name} поднял {number+1}')
        await asyncio.sleep(round(5/power))
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    tack_1 = asyncio.create_task(start_strongman('Pasha', 3))
    tack_2 = asyncio.create_task(start_strongman('Denis', 4))
    tack_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await tack_1
    await tack_2
    await tack_3

if __name__ == '__main__':
    asyncio.run(start_tournament())



