import asyncio
import time

async def array(arr):
    index = 0
    for a in arr:
        await delayed(a, index)
        index += 1        
        
async def delayed(value, delay):
    await asyncio.sleep(2**delay)
    print(value)
    
arr = ['One', 'Two', 'Three', 'Four']

asyncio.run(array(arr))
