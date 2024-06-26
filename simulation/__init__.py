from simulation.uniswap_v2 import *
from simulation.uniswap_v3 import *
from simulation.online_simulator import *


RPC_ENDPOINTS = {
    'ethereum': os.getenv('ETHEREUM_HTTP_RPC_URL'),
    'polygon': os.getenv('POLYGON_HTTP_RPC_URL'),
    'arbitrum': os.getenv('ARBITRUM_HTTP_RPC_URL'),
}