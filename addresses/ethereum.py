EXCHANGE = 'ethereum'

TOKENS = {
    'ETH': ['0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 18],
    'USDT': ['0xdAC17F958D2ee523a2206206994597C13D831ec7', 6],
    'USDC': ['0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', 6],
    'BTC': ['0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599', 8],
    'DAI': ['0x6B175474E89094C44Da98b954EedeAC495271d0F', 18],
    # 'MATIC': ['0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0', 18],
    'PEPE': ['0x6982508145454Ce325dDbE47a25d4ec3d2311933', 18],
    # 'FRAX': ['0x853d955aCEf822Db058eb8505911ED77F175b99e', 18],
    # 'UNI': ['0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984', 18],
    # 'LINK': ['0x514910771AF9Ca656af840dff83E8264EcF986CA', 18],
}

columns = ['chain', 'exchange', 'version', 'name', 'address', 'fee', 'token0', 'token1']

POOLS = [
    ['uniswap', 3, 'ETH/USDT', '0x11b815efB8f581194ae79006d24E0d814B7697F6', 500, 'ETH', 'USDT'],
    ['uniswap', 3, 'USDC/USDT', '0x3416cF6C708Da44DB2624D63ea0AAef7113527C6', 100, 'USDC', 'USDT'],
    ['uniswap', 3, 'BTC/ETH', '0x4585FE77225b41b697C938B018E2Ac67Ac5a20c0', 500, 'BTC', 'ETH'],
    ['uniswap', 3, 'DAI/USDC', '0x5777d92f208679DB4b9778590Fa3CAB3aC9e2168', 100, 'DAI', 'USDC'],
    # ['uniswap', 3, 'FRAX/USDC', '0xc63B0708E2F7e69CB8A1df0e1389A98C35A76D52', 500, 'FRAX', 'USDC'],
    # ['uniswap', 3, 'UNI/ETH', '0x1d42064Fc4Beb5F8aAF85F4617AE8b3b5B8Bd801', 3000, 'UNI', 'ETH'],
    # ['uniswap', 3, 'LINK/ETH', '0xa6Cc3C2531FdaA6Ae1A3CA84c2855806728693e8', 3000, 'LINK', 'ETH'],
    ['uniswap', 3, 'PEPE/ETH', '0x11950d141EcB863F01007AdD7D1A342041227b58', 3000, 'PEPE', 'ETH'],
    # ['uniswap', 3, 'MATIC/ETH', '0x290A6a7460B308ee3F19023D2D00dE604bcf5B42', 3000, 'MATIC', 'ETH'],

    ['uniswap', 2, 'ETH/USDT', '0x0d4a11d5EEaaC28EC3F61d100daF4d40471f1852', 3000, 'ETH', 'USDT'],
    ['uniswap', 2, 'USDC/ETH', '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc', 3000, 'USDC', 'ETH'],
    ['uniswap', 2, 'DAI/USDC', '0xAE461cA67B15dc8dc81CE7615e0320dA1A9aB8D5', 3000, 'DAI', 'USDC'],
    ['uniswap', 2, 'PEPE/ETH', '0xA43fe16908251ee70EF74718545e4FE6C5cCEc9f', 3000, 'PEPE', 'ETH'],
    # ['uniswap', 2, 'UNI/ETH', '0xd3d2E2692501A5c9Ca623199D38826e513033a17', 3000, 'UNI', 'ETH'],

    ['sushiswap', 3, 'ETH/USDT', '0x72c2178E082feDB13246877B5aA42ebcE1b72218', 500, 'ETH', 'USDT'],
    ['sushiswap', 3, 'USDC/ETH', '0x35644Fb61aFBc458bf92B15AdD6ABc1996Be5014', 500, 'USDC', 'ETH'],
    ['sushiswap', 3, 'BTC/ETH', '0x801CCFae9d2C77893B545E8D0E4637C055CD26cB', 500, 'BTC', 'ETH'],
    ['sushiswap', 3, 'USDC/USDT', '0xfA6e8E97ecECDC36302eCA534f63439b1E79487B', 100, 'USDC', 'USDT'],
    ['sushiswap', 3, 'DAI/USDC', '0x31ac258B911Af9a0d2669ebDFC4e39D92e96b772', 100, 'DAI', 'USDC'],

    ['sushiswap', 2, 'BTC/ETH', '0xCEfF51756c56CeFFCA006cD410B03FFC46dd3a58', 3000, 'BTC', 'ETH'],
    ['sushiswap', 2, 'ETH/USDT', '0x06da0fd433C1A5d7a4faa01111c044910A184553', 3000, 'ETH', 'USDT'],
    ['sushiswap', 2, 'USDC/ETH', '0x397FF1542f962076d0BFE58eA045FfA2d347ACa0', 3000, 'USDC', 'ETH'],
    ['sushiswap', 2, 'DAI/ETH', '0xC3D03e4F041Fd4cD388c549Ee2A29a9E5075882f', 3000, 'DAI', 'ETH'],
]

POOLS = [dict(zip(columns, [EXCHANGE] + pool)) for pool in POOLS]
