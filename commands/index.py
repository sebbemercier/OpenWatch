async def setup(bot):
    from commands import about, uptime

    await about.setup(bot)
    await uptime.setup(bot)
