import asyncio

async def fake_function():
    await asyncio.sleep(2)
    raise ValueError("Что-то пошло не так!")  

async def main():
    try:
        await fake_function()
    except ValueError as err:
        print(f"Обработано исключение: {err}")


asyncio.run(main())
