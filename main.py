import voltage
from voltage.ext import commands
import asyncio
from modules import api_key
from modules import colorextractor
from modules import easter_eggs
from modules import webscrapper

client = commands.CommandsClient('d!')

@client.command()
async def ping(ctx):
	'''sends pong'''
	await ctx.reply('pong')


@client.command()
async def dot(ctx):
	
	scrapper.Get()
	HEX = dotcolor.GetHex()
	RGB = dotcolor.GetRGB()
	HSV = dotcolor.GetHSV()
	hue = HSV[0]
	
	if hue in range(280, 359) or hue in range(0, 47):

		easter_description = easter_eggs.negative_message()


	elif hue in range(145, 266):

		easter_description = easter_eggs.positive_message()

	else:
		easter_description = None
	
	
	embed = voltage.SendableEmbed(
		title='Dotsy',
		colour=f'#{HEX}',
		description='d!dot',
		
	)
	
	text = f'''\n ###  [The Dot](https://gcpdot.com/)
### {easter_description}
Hex: #{HEX}
RGB: {RGB}'''
	
	embed.description += text

	await ctx.send(embed=embed)


async def shutdown():
	scraper.Shutdown()


async def refresh_loop():
	while True:
		await asyncio.sleep(10 * 60)
		scrapper.Refresh()
		print('refreshed')

loop = asyncio.get_event_loop()
loop.create_task(client.start(api_key.dotsy))
loop.create_task(refresh_loop())
loop.run_forever()

