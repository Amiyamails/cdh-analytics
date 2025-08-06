from config.MathOperations import MathOperations
from config.logger import get_logger

logger = get_logger(__name__)

def main():
    math_ops = MathOperations()
    logger.info(f"Add: {math_ops.add(4, 3)}")
    logger.info(f"Subtract: {math_ops.subtract(4, 3)}")
    logger.info(f"Multiply: {math_ops.multiply(4, 3)}")

if __name__ == "__main__":
    main()
