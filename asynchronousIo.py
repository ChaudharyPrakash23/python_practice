import asyncio

# async def main():
#     print("Hello...")
    
#     await asyncio.sleep(2)
    
#     print("...World!")

# asyncio.run(main())

async def count():
    print("lets start counting")
    for i in range(10):
        print(i)
        await asyncio.sleep(2)

asyncio.run(count())
        