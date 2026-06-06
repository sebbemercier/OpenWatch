import discord

async def setup(bot):
    @bot.tree.command(name="about", description="Affiche des informations sur le bot")
    async def about_cmd(interaction: discord.Interaction):
        await interaction.response.send_message("Bonjour! Je suis un bot Discord opensource pour aider à monitorer des serveurs / services depuis des apis grafana uptime kuma ou autres pour plus d'info aller sur la page github du projet ( faites /github pour avoir le lien )")

    @bot.tree.command(name="github", description="Affiche le lien vers le dépôt GitHub")
    async def github_cmd(interaction: discord.Interaction):
        await interaction.response.send_message("Voici le lien vers le dépôt GitHub du projet : https://github.com/sebbemercier/OpenWatch")