from enum import Enum

class ProductCondition(str, Enum):
    ACTIVE = "ACTIVO"
    DISCONTINUED = "DISCONTINUADO"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PAUSED = "PAUSED"