import asyncio
from func_connects import connect_hyper
from func_private import place_market_order, abort_all_positions
from func_cointegration import store_cointegration_results
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED, PLACE_TRADES, MANAGE_EXITS
from func_public import construct_market_prices
from func_entry_pairs import open_positions
from func_exit_pairs import manage_trade_exits
from func_messaging import send_message
import time
# MAIN FUNCTION

async def main():
    try:
        # Message on start
        send_message("Bot launch successful")
        # Connect to client
        try:
            print("")
            print("Program started...")
            print("Connecting to Client...")
            client = await connect_hyper()
        except Exception as e:
            print("Error connecting to client: ", e)
            send_message(f"Failed to connect to client {e}")
            exit(1)


        #Abort all open positions
        if ABORT_ALL_POSITIONS:
            try:
              print("")
              print("Closing open positions...")
              await abort_all_positions(client)
            except Exception as e:
              print("Error closing all positions: ", e)
              send_message(f"Error closing all positions {e}")
              exit(1)


        # Find Cointegrated Pairs
        if FIND_COINTEGRATED:

            # Construct Market Prices
            try:
                print("")
                print("Fetching token market prices, please allow around 5 minutes...")
                df_market_prices = await construct_market_prices(client)
            except Exception as e:
                print("Error constructing market prices: ", e)
                send_message(f"Error constructing market prices {e}")
                exit(1)
            #print(df_market_prices)

            # Store Cointegrated Pairs
            try:
                print("")
                print("Storing cointegrated pairs...")
                stores_result = store_cointegration_results(df_market_prices)
                if stores_result != "saved":
                    print("Error saving cointegrated pairs")
                    exit(1)
            except Exception as e:
                print("Error saving cointegrated pairs: ", e)
                send_message(f"Error saving cointegrated pairs {e}")
                exit(1)

        # Run as always on
        while True:
            # Manage existing positions
            if MANAGE_EXITS:
                try:
                    print("")
                    print("Managing exits...")
                    await manage_trade_exits(client)
                    time.sleep(1)
                except Exception as e:
                    print("Error managing exiting positions: ", e)
                    send_message(f"Error managing exiting positions {e}")
                    exit(1)

            # # Place trades for opening positions
            if PLACE_TRADES:
                try:
                    print("")
                    print("Finding trading opportunities...")
                    await open_positions(client)
                except Exception as e:
                    print("Error trading pairs: ", e)
                    send_message(f"Error opening trades {e}")
                    exit(1)
    finally:
            await client.close()

asyncio.run(main())