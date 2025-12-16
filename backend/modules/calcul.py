from loguru import logger

def calcul(value: int) -> int:
    logger.debug(f"calcul(): value={value}")
    return value * value
