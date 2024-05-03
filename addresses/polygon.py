EXCHANGE = 'polygon'

TOKENS = {
    'WETH': ['0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619', 18],
    'WMATIC': ['0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270', 18], #AGREGADAS TODAS WMATIC /
    'USDT': ['0xc2132D05D31c914a87C6611C10748AEb04B58e8F', 6],
    'USDC': ['0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174', 6],
    'USDC.e': ['0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174', 6],
    'AAVE': ['0xD6DF932A45C0f255f85145f286eA0b292B21C90B', 6],
    'WBTC': ['0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6', 8],
    'DAI': ['0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063', 18],

}


columns = ['chain', 'exchange', 'version', 'name', 'address', 'fee', 'token0', 'token1']

POOLS = [
    ['uniswap', 3, 'WMATIC/USDC', '0xb6e57ed85c4c9dbfef2a68711e9d6f36c56e0fcb', 500, 'WMATIC', 'USDC'],
     ['uniswap', 3, 'WMATIC/USDC', '0xA374094527e1673A86dE625aa59517c5dE346d32', 500, 'WMATIC', 'USDC'],
    ['uniswap', 3, 'WMATIC/WETH', '0x86f1d8390222a3691c28938ec7404a1661e618e0', 500, 'WMATIC', 'WETH'],
    ['uniswap', 3, 'WMATIC/WETH', '0x167384319b41f7094e62f7506409eb38079abff8', 3000, 'WMATIC', 'WETH'],
    ['uniswap', 3, 'WMATIC/USDT', '0x9b08288c3be4f62bbf8d1c20ac9c5e6f9467d8b7', 3000, 'WMATIC', 'USDT'],
    ['uniswap', 3, 'WMATIC/DAI', '0x0f663c16dd7c65cf87edb9229464ca77aeea536b', 500, 'WMATIC', 'DAI'],
    ['uniswap', 3, 'WMATIC/WBTC', '0x6b75f2189f0e11c52e814e09e280eb1a9a8a094a', 500, 'WMATIC', 'WBTC'],
    ['uniswap', 3, 'USDC/USDC', '0x6b75f2189f0e11c52e814e09e280eb1a9a8a094a', 100, 'USDC', 'USDC'],
    ['uniswap', 3, 'USDC/USDT', '0xdac8a8e6dbf8c690ec6815e0ff03491b2770255d', 100, 'USDC', 'USDT'],
    ['uniswap', 3, 'WBTC/USDT', '0x50eaedb835021e4a108b7290636d62e9765cc6d7', 500, 'WBTC', 'USDT'],
    ['uniswap', 3, 'WBTC/USDC', '0xeef1a9507b3d505f0062f2be9453981255b503c8', 500, 'WBTC', 'USDC'],
    ['uniswap', 3, 'WETH/USDT', '0xbb98b3d2b18aef63a3178023a920971cf5f29be4', 500, 'WETH', 'USDT'],
    ['uniswap', 3, 'WETH/USDT', '0x4ccd010148379ea531d6c587cfdd60180196f9b1', 500, 'WETH', 'USDT'],
    ['uniswap', 3, 'AAVE/WETH', '0x2aceda63b5e958c45bd27d916ba701bc1dc08f7a', 3000, 'AAVE', 'WETH'],
    ['uniswap', 3, 'WBTC/WETH', '0xfe343675878100b344802a6763fd373fdeed07a4', 3000, 'AAVE', 'WETH'],
    ['uniswap', 3, 'AAVE/WMATIC', '0xa9077cdb3d13f45b8b9d87c43e11bce0e73d8631', 3000, 'AAVE', 'WMATIC'],
    ['uniswap', 3, 'USDC/WETH', '0x45dda9cb7c25131df268515131f647d726f50608', 500, 'USDC', 'WETH'],
    ['uniswap', 3, 'USDT/USDC', '0x3F5228d0e7D75467366be7De2c31D0d098bA2C23', 500, 'USDT', 'USDC'],



    ['sushiswap', 3, 'WMATIC/USDT', '0x55ff76bffc3cdd9d5fdbbc2ece4528ecce45047e', 300, 'WMATIC', 'USDT'],
    ['sushiswap', 2, 'WMATIC/WETH', '0xc4e595acdd7d12fec385e5da5d43160e8a0bac0e', 300, 'WMATIC', 'WETH'],
    ['sushiswap', 2, 'USDC.e/WETH', '0x34965ba0ac2451a34a0471f04cca3f990b8dea27', 300, 'USDC.e', 'WETH'],
    ['sushiswap', 2, 'WETH/DAI', '0x6ff62bfb8c12109e8000935a6de54dad83a4f39f', 300, 'WETH', 'DAI'],
    ['sushiswap', 2, 'WBTC/WETH', '0xe62ec2e799305e0d367b0cc3ee2cda135bf89816', 300, 'WETH', 'DAI'],
     ['sushiswap', 2, 'USDC.e/USDT', '0x4b1f1e2435a9c96f7330faea190ef6a7c8d70001', 300, 'USDC.e', 'USDT'],
     ['sushiswap', 2, 'WETH/AAVE', '0x2813d43463c374a680f235c428fb1d7f08de0b69', 300, 'WETH', 'AAVE'],
     ['sushiswap', 2, 'MATIC/USD.e', '0xcd353f79d9fade311fc3119b841e1f456b54e858', 300, 'MATIC', 'USD.e'],
     ['sushiswap', 2, 'USDC.e/WETH', '0x1b0585fc8195fc04a46a365e670024dfb63a960c', 300, 'USDC.e', 'WETH'],






]

POOLS = [dict(zip(columns, [EXCHANGE] + pool)) for pool in POOLS]

SIMULATION_HANDLERS = {
    'uniswap_v2': '0x9e5A52f57b3038F1B8EeE45F28b3C1967e22799C',    # factory
    'sushiswap_v2': '0xc35DADB65012eC5796536bD9864eD8773aBc74C4',  # factory
    'uniswap_v3': '0x61fFE014bA17989E743c5F6cB21bF9697530B21e',    # quoterv2
    'sushiswap_v3': '0xb1E835Dc2785b52265711e17fCCb0fd018226a6e',  # quoterv2
}

EXECUTION_HANDLERS = {
    'uniswap_v2': '0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B',    # router2
    'sushiswap_v2': '0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506',  # router2
    'uniswap_v3': '0xe592427a0aece92de3edee1f18e0157c05861564',    # swap router2
    'sushiswap_v3': '0x0aF89E1620b96170e2a9D0b68fEebb767eD044c3',  # TODO: Sushiswap V3 doesn't have SwapRouter2, needs to use pool contract
}
