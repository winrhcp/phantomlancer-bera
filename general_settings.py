"""
------------------------------------------------GENERAL SETTINGS--------------------------------------------------------
    WALLETS_TO_WORK = 0 | The software will take wallets from the table according to the rules described below
    0 = all wallets in a row
    3 = only wallet №3
    4, 20 = wallets №4 and №20
    [5, 25] = wallets from №5 to №25

    ACCOUNTS_IN_STREAM      | Number of wallets in the execution stream. If there are a total of 100 wallets and you specify 10,
                            then the software will make 10 passes with 10 wallets each

"""
SOFTWARE_MODE = 0               # 0 - последовательный запуск / 1 - параллельный запуск
ACCOUNTS_IN_STREAM = 10          # Только для SOFTWARE_MODE = 1 (параллельный запуск)
WALLETS_TO_WORK = 0             # 0 / 3 / 3, 20 / [3, 20]
BREAK_ROUTE = False             # Прекращает выполнение маршрута, если произойдет ошибка
SHUFFLE_WALLETS = False         # Перемешивает кошельки перед запуском
SAVE_PROGRESS = False           # True или False | Включает сохранение прогресса аккаунта для Classic-routes
TELEGRAM_NOTIFICATIONS = False  # True или False | Включает уведомления в Telegram
WAIT_FAUCET = False             # Ожидает получение $BERA из Faucet

'------------------------------------------------SLEEP CONTROL---------------------------------------------------------'
SLEEP_MODE = False               # True или False | Включает сон после каждого модуля и аккаунта
SLEEP_TIME = (10, 15)           # (минимум, максимум) секунд | Время сна между модулями.
SLEEP_TIME_STREAM = (5, 10)    # (минимум, максимум) секунд | Время сна между аккаунтами.

'------------------------------------------------RETRY CONTROL---------------------------------------------------------'
MAXIMUM_RETRY = 3               # Количество повторений при ошибках
SLEEP_TIME_RETRY = (5, 10)      # (минимум, максимум) секунд | Время сна после очередного повторения

'------------------------------------------------PROXY CONTROL---------------------------------------------------------'
MOBILE_PROXY = False             # True или False | Включает использование мобильных прокси.
MOBILE_PROXY_URL_CHANGER = ['',
                            '',
                            '']  # ['link1', 'link2'..] | Ссылки для смены IP

'------------------------------------------------SECURE DATA-----------------------------------------------------------'
# https://2captcha.com/enterpage
TWO_CAPTCHA_API_KEY = ""

# TELEGRAM DATA
TG_TOKEN = ""  # https://t.me/BotFather
TG_ID = ""  # https://t.me/getmyid_bot

"""
--------------------------------------------CLASSIC-ROUTES CONTROL------------------------------------------------------

    mint_berachain_tokens  # минт $BERA на BeraChain Faucet (https://artio.faucet.berachain.com/)
    swap_btc_bex           # свап на BEX ($BERA -> $BTC)
    swap_honey_bex         # свап на BEX ($BERA -> $HONEY)
    swap_stgusdc_bex       # свап на BEX ($BERA -> $STGUSDC)
    swap_eth_bex           # свап на BEX ($BERA -> $ETH)
    supply_honey_bend      # добавление $HONEY ликвидности на Bend           
    supply_btc_bend        # добавление $BTC ликвидности на Bend      
    supply_eth_bend        # добавление $ETH ликвидности на Bend      
    withdraw_honey_bend    # вывод $HONEY ликвидности на Bend         
    withdraw_btc_bend      # вывод $BTC ликвидности на Bend           
    withdraw_eth_bend      # вывод $ETH ликвидности на Bend           
    add_liqiudity_bex      # добавление ликвидности на BEX
    mint_honey             # минт $HONEY за $STGUSDC
    mint_booga_ticket      # минт OOGA BOOGA Ticket за 4.2 $HONEY
    mint_bera_red          # минт  Mint BERA RED ENVELOPE за 1.8 $HONEY
    claim_galxe_points     # выполнение дейлика на Galxe (5 поинтов за визит Faucet)

    Выберите необходимые модули для взаимодействия
    Вы можете создать любой маршрут, софт отработает строго по нему. Для каждого списка будет выбран один модуль в
    маршрут, если софт выберет None, то он пропустит данный список модулей. 
    Список модулей сверху.

    CLASSIC_ROUTES_MODULES_USING = [
        ['mint_berachain_tokens'],
        ['swap_stgusdc_bex'],
        ['mint_honey'],
        ['claim_galxe_points']
        ...
    ]
"""
CLASSIC_ROUTES_MODULES_USING = [
    ['mint_berachain_tokens'],
    ['swap_stgusdc_bex'],
    ['swap_eth_bex', 'swap_btc_bex'],
    ['add_liqiudity_bex'],
    ['mint_honey'],
    ['mint_booga_ticket', None],
    ['supply_honey_bend', 'supply_btc_bend', 'supply_eth_bend'],
    ['claim_galxe_points']
]
