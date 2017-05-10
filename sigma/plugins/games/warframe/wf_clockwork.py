import asyncio
import discord
from .nodes.sortie_functions import get_sortie_data, generate_sortie_embed
from .nodes.fissure_functions import get_fissure_data, generate_fissure_embed
from .nodes.alert_functions import get_alert_data, generate_alert_embed

async def wf_clockwork(ev):
    while True:
        all_guilds = ev.bot.guilds
        sorties = await get_sortie_data(ev.db)
        if sorties:
            sortie_response = generate_sortie_embed(sorties)
            for guild in all_guilds:
                try:
                    sortie_channel = ev.db.get_settings(guild.id, 'WarframeSortieChannel')
                except:
                    sortie_channel = None
                if sortie_channel:
                    sortie_target_channel = discord.utils.find(lambda x: x.id == sortie_channel, guild.channels)
                    if sortie_target_channel:
                        try:
                            await sortie_target_channel.send(embed=sortie_response)
                        except:
                            pass
        fissures = await get_fissure_data(ev.db)
        if fissures:
            fissure_response = generate_fissure_embed(fissures)
            for guild in all_guilds:
                try:
                    fissure_channel = ev.db.get_settings(guild.id, 'WarframeFissureChannel')
                except:
                    fissure_channel = None
                if fissure_channel:
                    fissure_target_channel = discord.utils.find(lambda x: x.id == fissure_channel, guild.channels)
                    try:
                        await fissure_target_channel.send(embed=fissure_response)
                    except:
                        pass
        alerts = await get_alert_data(ev.db)
        if alerts:
            alert_response = await generate_alert_embed(alerts)
            for guild in all_guilds:
                try:
                    alert_channel = ev.db.get_settings(guild.id, 'WarframeAlertChannel')
                except:
                    alert_channel = None
                if alert_channel:
                    alert_target_channel = discord.utils.find(lambda x: x.id == alert_channel, guild.channels)
                    try:
                        await alert_target_channel.send(embed=alert_response)
                    except:
                        pass
        await asyncio.sleep(10)
