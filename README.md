## General Information

Software for testing the Berachain testnet. All settings are simple and clear, nothing extra.
The path will be conquered by the one who walks it, and the software will conquer any degenerate 

## Key Features

# Proxy support (including mobile)
# Extensive logging, even your sneeze will be logged
# Saving process for accounts
# Repeater (in case of errors in modules)
# Collection of unworked wallets
# Logging saving in files by day
# Parallel launch
# Asynchronous OOP code
# EIP-1559
# Modules 🧩

    1.  Faucet       (receiving tokens from faucet)                                      
    2.  BEX          (swaps $BERA to $STGUSDC, $BTC, $ETH, liquidity in pool $BERA/$STGUSDC)
    3.  Bend         (adding and withdrawing $HONEY, $BTC, $ETH liquidity)
    4.  Honey        (minting $HONEY for $STGUSDC)  
    5.  Honey        (minting OOGA BOOGA TICKET)   
    6.  Galxe        (completing daily tasks for 5 points by visiting Faucet)

## Main Functions

1.  **🚀 Launch of all account runs through prepared classic routes**

    This function will initiate route execution for all accounts. To make it work, you need to generate a route by running function №2 (Route Generation).

2.  **📄Generation of classic routes for each account**

    Classic generator, works on the old-school method. You need to specify the module lists in the `CLASSIC_ROUTES_MODULES_USING` setting, and when you run this function, the software will build a route for you based on this setting. `None` is supported as one of the modules in the list; when it appears in the route, the software will skip this list.

3. **✅Checking all proxies for functionality**

    Fast proxy check (really fast, as if it's torn off the chain)

## 📄Input of your data

### All necessary data must be specified in the `accounts_data` table in the `/data` folder.. 
   1. **Name** -  names of your accounts, each name must be unique
   2. **Private Key** - private keys from wallets
   3. **Proxy** - proxy for each account. If there are fewer proxies, the software will take them in a circle. If the proxies are mobile, you can specify one proxy.
   4. **Email address** - email address for the account.
   5. **Email password** - email password for the account.

You can set a password for your table and enable the `EXCEL_PASSWORD setting = True`. When the password is activated, the software will require it to be entered for further work. Useful when working on a server.

## Software Setup

All settings are moved to the `general_settings.py` file. The most important settings will be duplicated here.

1. `TWO_CAPTCHA_API_KEY` key. Specify your API key from 2captcha. There is a link in the file to the website where you can get the key.
2. Setting `EXCEL_PAGE_NAME`. The name of the sheet in the Excel table.
3. In the `CLASSIC_ROUTES_MODULES_USING` setting, specify the route for account operation.

## 🛠️Installation and Project Launch

> By installing the project, you accept the risks of using software for money mining (losing your ass, money, virginity).

Once you have downloaded the project, make sure you have Python 3.10.11

--------------------------------------------------------