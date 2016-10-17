# BOT
StartupType = '0'  # 0 For starting up as a Bot, 1 for starting up as a Normal User
Token = ''  # Discord App Token (If StartupType is 0)
ClientID = ''  # Discord App Client ID
dsc_email = ''  # Discord Email (If StartupType is 1)
dsc_password = ''  # Discord Password (If StartupType is 1)
OwnerID = ''  # Your UniqueID for special permissions
Prefix = '>>'  # Bot Command Prefix
sigma_version = ''

# APIs
# Blizzard/Battle.net
BlizzardKey = ''
RLAPIKey = ''

# Reddit
reddit_un = ''
reddit_pw = ''

# MyAnimeList
mal_un = ''  # Username
mal_pw = ''  # Password

# Open Weather Map API Key
OpenWeatherMapKey = ''

# Mashape API Key
MashapeKey = ''

# Riot Games API Key
RiotAPIKey = ''

# Google API KEy
GoogleAPIKey = ''

# LastFM API Key
LastFMAPIKey = ''

# IsThereAnyDeal API Key
ITADKey = ''

# Pushbullet API Key
Pushbullet = ''
Notifications = 'No'  # Experimental Pushbullet Notification Toggle

# Steam API Key
SteamAPI = ''

# Sonarr API Key
SonarrKey = ''

# Imgur API
ImgurClientID = ''
ImgurClientSecret = ''

# GitHub
GitHubToken = ''

# Commands
cmd_help = 'help'
cmd_modules = 'modules'
cmd_overwatch = 'overwatch'
cmd_league = 'league'
cmd_echo = 'echo'
cmd_bns = 'bnsstats'
cmd_bns_att = 'bnsatt'
cmd_bns_def = 'bnsdef'
cmd_osu = 'osu'
cmd_dota2 = 'dota2'
cmd_ud = 'ud'
cmd_weather = 'weather'
cmd_hearthstone = 'hearthstone'
cmd_pokemon = 'pokemon'
cmd_joke = 'joke'
cmd_rip = 'rip'
cmd_lfm = 'lastfm'
cmd_nsfw_permit = 'nsfwpermit'
cmd_nhentai = 'nhentai'
cmd_ehentai = 'ehentai'
cmd_gelbooru = 'gelbooru'
cmd_rule34 = 'rule34'
cmd_e621 = 'e621'
cmd_hentaims = 'hentaims'
cmd_itad = 'itad'
cmd_imdb = 'imdb'
cmd_jisho = 'jisho'
cmd_wk = 'wanikani'
cmd_wk_store = 'wksave'
cmd_anime = 'anime'
cmd_manga = 'manga'
cmd_vindi = 'es'
cmd_sonarr = 'sonarr'
cmd_handup = 'handup'
cmd_handdown = 'handdown'
cmd_takemic = 'takemic'
cmd_dropmic = 'dropmic'
cmd_repertoire = 'singers'
cmd_vndb = 'vndb'
cmd_remind = 'remind'

# Descriptions
desc_help = 'Returns the list of command modules or gives you the description and usage for a selected command.'
desc_overwatch = 'Shows the Overwatch statistics of inputed Battle.Net ID. (\'Warning: Case Sensitive\')'
desc_league = 'Shows the player\'s League of Legends statistics of inputed Summoner Name. You can also place a gamemode between the Region and Summoner Name to get statistics for it.'
desc_osu = 'Generates a signature image with the user\'s stats for osu!.'
desc_ud = 'Shows the Urban Dictionary definition for the given word.'
desc_weather = 'Shows weather data for the selected location.'
desc_pokemon = 'Shows details for the chosen Pokemon.'
desc_lfm = 'Shows the users top listened to songs from LastFM.'
desc_nsfw_permit = 'Permits the NSFW module in the channel where the command is written to. (\'Server Administrator Only\')'
desc_rule34 = 'Searches Rule34 for selected tags, if no tags are specified, it gives a random image.'
desc_nhentai = 'Searches nHentai for doujinshi for the inputed name, displays the results, cover and tags.'
desc_anime = 'Searches MyAnimeList for anime by given name. Generates a really cool image with the details!'
desc_manga = 'Searches MyAnimeList for manga by given name. Generates a really cool image with the details!'
desc_jisho = 'Searches the Japanese word dictionary (Jisho) for the given word and gives information for it'
desc_wanikani = 'Shows the WaniKani statistics of the person who used the command or a mentioned person. Also searches WaniKani fora given username. For advanced stats, a user must save his WaniKani API Key with the ' + str(
    Prefix) + str(cmd_wk_store) + 'command. Use help on it to get more info.'
desc_wk_store = 'Stores a given API Key or Username for you. If you want detailed stats when calling the ' + str(
    Prefix) + str(cmd_wk) + ' command you need to save your WK API Key like in the example bellow!'
desc_bns = 'The Blade and Soul module provides in-depth character information. You can additionally use ' + str(
    Prefix) + str(cmd_bns_att) + ' to get every detail on your characters offensive stats or ' + str(Prefix) + str(
    cmd_bns_def) + ' for defensive.'
desc_echo = 'Repeats the given text. (\'Bot Owner Only\')'
desc_gelbooru = 'Searches GelBooru for selected tags, if no tags are specified, it gives a random image. If the wanted tag contains spaces type it with an underscore instead as spaces are used to separate multiple tags.'
desc_hearthstone = 'Hearthstone card lookup.'
desc_imdb = 'Searches the Internet Movie Database for a Title of your choice.'
desc_itad = 'Lists the latest deals from IsThereAnyDeal'
desc_joke = 'Outputs a random joke from a random source, it is totally cancerous.'

# Usage
usg_help = str(Prefix) + str(cmd_help) + ' overwatch'
usg_overwatch = str(Prefix) + str(cmd_overwatch) + ' EU Aurora#22978'
usg_league = str(Prefix) + str(cmd_league) + ' EUNE AXAz0r'
usg_osu = str(Prefix) + str(cmd_osu) + ' AXAz0r'
usg_ud = str(Prefix) + str(cmd_ud) + ' Alex'
usg_weather = str(Prefix) + str(cmd_weather) + ' Melbourne, AU'
usg_pokemon = str(Prefix) + str(cmd_pokemon) + ' Snorlax'
usg_lfm = str(Prefix) + str(cmd_lfm) + ' axaz0r'
usg_nsfw_permit = str(Prefix) + str(cmd_nsfw_permit)
usg_rule34 = str(Prefix) + str(cmd_rule34) + ' ovum'
usg_nhentai = str(Prefix) + str(cmd_nhentai) + ' Oreimo'
usg_anime = str(Prefix) + str(cmd_anime) + ' Terror in Resonance'
usg_manga = str(Prefix) + str(cmd_manga) + ' Silent Voice'
usg_jisho = str(Prefix) + str(cmd_jisho) + ' kawaii'
usg_wanikani = str(Prefix) + str(cmd_wk) + ' breadstickninja'
usg_wk_store = str(Prefix) + str(cmd_wk_store) + ' key 12345678901234567890123456789012'
usg_bns = str(Prefix) + str(cmd_bns) + ' EU Lucia Konohana'
usg_echo = str(Prefix) + str(cmd_echo) + ' Hello world!'
usg_gelbooru = str(Prefix) + str(cmd_gelbooru) + ' vella mabinogi_heroes'
usg_hearthstone = str(Prefix) + str(cmd_hearthstone) + ' Murloc Raider'
usg_imdb = str(Prefix) + str(cmd_imdb) + ' A Clockwork Orange'
usg_itad = str(Prefix) + str(cmd_itad)
usg_joke = str(Prefix) + str(cmd_joke)

# Experimental
permitted_id = ['1234567891361631']
permitted_roles = ['Admin']
unpermitted_id = []
unpermitted_roles = []