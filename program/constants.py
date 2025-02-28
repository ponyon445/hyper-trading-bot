#
from decouple import config

ticker_1 = "SOL/USDC:USDC"
ticker_2 = "ETH/USDC:USDC"

# Close all open positions and orders
ABORT_ALL_POSITIONS = False

# Find Cointegrated Pairs
FIND_COINTEGRATED = False
# Manage Exits
MANAGE_EXITS = False
# Place Trades
PLACE_TRADES = False

# Resolution
RESOLUTION = "1HOUR"

# Stats Window
WINDOW = 21

# Thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
ZSCORE_THRESH_CLOSE = 1
CLOSE_THRESH = -0.15
USD_PER_TRADE = 12
USD_MIN_COLLATERAL = 25

# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

# Environment Variables
HYPPER_ADDRESS = config("HYPPER_ADDRESS")
HYPPER_SECRET_PHRASE = config("SECRET_PHRASE")
MNEMONIC = (HYPPER_SECRET_PHRASE)
TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = config("TELEGRAM_CHAT_ID")
PRIVATE_KEY = config("PRIVATE_KEY")
WALLET_ADDRESS = config("WALLET_ADDRESS")