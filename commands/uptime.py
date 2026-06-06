import discord

async def setup(bot):
    @bot.tree.command(name="uptime-server", description="Affiche le temps de fonctionnement d'un serveur.")
    async def uptime_server_cmd(interaction: discord.Interaction, nodeID: int):
        await interaction.response.send_message(f'Tu as rentré l\'argument {nodeID} dans la commande')