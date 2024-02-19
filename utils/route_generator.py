import json
import random

from utils.tools import clean_progress_file
from functions import *
from config import ACCOUNT_NAMES
from modules import Logger
from general_settings import CLASSIC_ROUTES_MODULES_USING

AVAILABLE_MODULES_INFO = {
    # module_name                       : (module name, priority, tg info, can`t be shuffled, supported network)
    mint_berachain_tokens               : (mint_berachain_tokens, 1, 'Mint $BERA on Faucet', 1, [0]),
    swap_btc_bex                        : (swap_btc_bex, 2, '$BERA -> $BTC Bex Swap', 0, [0]),
    swap_honey_bex                      : (swap_honey_bex, 2, '$BERA -> $HONEY Bex Swap', 0, [0]),
    swap_eth_bex                        : (swap_eth_bex, 2, '$BERA -> $ETH Bex Swap', 0, [0]),
    swap_stgusdc_bex                    : (swap_stgusdc_bex, 2, '$BERA -> $STGUSDC Bex Swap', 0, [0]),
    add_liqiudity_bex                   : (add_liqiudity_bex, 3, 'Add liquidity on Bex', 0, [0]),
    supply_honey_bend                   : (supply_honey_bend, 3, 'Supply $HONEY on Bend', 0, [0]),
    supply_btc_bend                     : (supply_btc_bend, 3, 'Supply $BTC on Bend', 0, [0]),
    supply_eth_bend                     : (supply_eth_bend, 3, 'Supply $ETH on Bend', 0, [0]),
    withdraw_honey_bend                 : (withdraw_honey_bend, 3, 'Withdraw $HONEY from Bend', 0, [0]),
    withdraw_btc_bend                   : (withdraw_btc_bend, 3, 'Withdraw $BTC from Bend', 0, [0]),
    withdraw_eth_bend                   : (withdraw_eth_bend, 3, 'Withdraw $ETH from Bend', 0, [0]),
    mint_honey                          : (mint_honey, 3, 'Mint $HONEY', 0, [0]),
    mint_booga_ticket                   : (mint_booga_ticket, 3, 'Mint OOGA BOOGA Ticket', 0, [0]),
    mint_bera_red                       : (mint_bera_red, 3, 'Mint BERA RED ENVELOPE', 0, [0]),
    claim_galxe_points                  : (claim_galxe_points, 3, 'Claim Galxe Daily Points', 0, [0]),
}


def get_func_by_name(module_name, help_message:bool = False):
    for k, v in AVAILABLE_MODULES_INFO.items():
        if k.__name__ == module_name:
            if help_message:
                return v[2]
            return v[0]


class RouteGenerator(Logger):
    def __init__(self):
        Logger.__init__(self)

    @staticmethod
    def classic_generate_route():
        route = []
        for i in CLASSIC_ROUTES_MODULES_USING:
            module_name = random.choice(i)
            if module_name is None:
                continue
            module = get_func_by_name(module_name)
            route.append(module.__name__)
        return route
    @staticmethod
    def faucet_generate_route():
        route = []
        # Extract the module name from the sublist
        module_name = CLASSIC_ROUTES_MODULES_USING[0][0]  # The module is the first element of the first sublist
        module = get_func_by_name(module_name)
        route.append(module.__name__)
        return route

    def classic_routes_json_save(self):
        clean_progress_file()
        with open('./data/services/wallets_progress.json', 'w') as file:
            accounts_data = {}
            for account_name in ACCOUNT_NAMES:
                if isinstance(account_name, (str, int)):
                    classic_route = self.classic_generate_route()
                    account_data = {
                        "current_step": 0,
                        "route": classic_route
                    }
                    accounts_data[str(account_name)] = account_data
            json.dump(accounts_data, file, indent=4)
        self.logger_msg(
            None, None,
            f'Successfully generated {len(accounts_data)} classic routes in data/services/wallets_progress.json\n',
            'success')
    def faucet_routes_json_save(self):
        clean_progress_file()
        with open('./data/services/wallets_progress.json', 'w') as file:
            accounts_data = {}
            for account_name in ACCOUNT_NAMES:
                if isinstance(account_name, (str, int)):
                    classic_route = self.faucet_generate_route()
                    account_data = {
                        "current_step": 0,
                        "route": classic_route
                    }
                    accounts_data[str(account_name)] = account_data
            json.dump(accounts_data, file, indent=4)
        self.logger_msg(
            None, None,
            f'Successfully generated {len(accounts_data)} faucet routes in data/services/wallets_progress.json\n',
            'success')