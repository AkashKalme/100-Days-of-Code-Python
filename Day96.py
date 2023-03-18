# AsyncIO in Python

import time
import asyncio
import requests

async def function1():
    print("Function 1")
    URL = "https://www.google.com/search?q=4k+wallpaper+for+pc&tbm=isch&chips=q:4k+wallpaper+pc,g_1:4k+resolution:TPxPmshTxdg%3D&rlz=1C1ONGR_enIN946IN946&hl=en&sa=X&ved=2ahUKEwi4r-2zyuT9AhXOgmMGHZWiD4wQ4lYoAnoECAEQJg&biw=1519&bih=722#imgrc=lbKp-UfYJmtc-M"
    response = requests.get(URL)
    open("img1.jpg", "wb").write(response.content)
    return "Akash"

async def function2():
    print("Function 2")
    URL = "https://www.google.com/search?q=4k+wallpaper+for+pc&rlz=1C1ONGR_enIN946IN946&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiy28qqyuT9AhWlSmwGHWS5DhgQ_AUoAXoECAIQAw&biw=1536&bih=722&dpr=1.25#imgrc=SB4y7GGtpFm-BM"
    response = requests.get(URL)
    open("img2.jpg", "wb").write(response.content)

async def function3():
    print("Function 3")
    URL = "https://www.google.com/search?q=4k+wallpaper+for+pc&tbm=isch&chips=q:4k+wallpaper+pc,g_1:4k+resolution:TPxPmshTxdg%3D&rlz=1C1ONGR_enIN946IN946&hl=en&sa=X&ved=2ahUKEwi4r-2zyuT9AhXOgmMGHZWiD4wQ4lYoAnoECAEQJg&biw=1519&bih=722#imgrc=KOB-QjK4aPoN4M"
    response = requests.get(URL)
    open("img.jpg", "wb").write(response.content)

async def main():
    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()
    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(L)

asyncio.run(main())