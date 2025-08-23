import copy
import random
import logging
from typing import Dict, List, Optional

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

class Hat:
    """Represents a hat containing colored balls."""

    def __init__(self, **balls: int) -> None:
        """
        Initialize the hat with given balls.
        
        Args:
            **balls: keyword arguments where key is ball color and value is count
        """
        self.contents: List[str] = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls: int) -> List[str]:
        """
        Draw balls randomly from the hat.

        Args:
            num_balls: Number of balls to draw

        Returns:
            List of drawn balls
        """
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        
        drawn_balls = random.sample(self.contents, num_balls)
        # Efficiently remove drawn balls
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls
    
def experiment(
    hat: Hat,
    expected_balls: Dict[str, int],
    num_balls_drawn: int,
    num_experiments: int,
    seed: Optional[int] = None
) -> float:
    """
    Conduct an experiment to estimate the probability of drawing
    the expected balls from the hat.

    Args:
        hat: Hat object
        expected_balls: Dict of balls expected to draw {color: count}
        num_balls_drawn: Number of balls to draw in each experiment
        num_experiments: Number of experiments to run
        seed: Optional seed for reproducibility

    Returns:
        Estimated probability of success
    """

    if seed is not None:
        random.seed(seed)

    success_count = 0

    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        drawn_balls = temp_hat.draw(num_balls_drawn)

        # Check if all expected balls are drawn
        success = all(
            drawn_balls.count(color) >= count
            for color, count in expected_balls.items()
        )

        if success:
            success_count += 1

    return success_count / num_experiments


if __name__ == "__main__":
    # Example usage
    hat = Hat(red=3, blue=2, green=6)
    probability = experiment(
        hat,
        expected_balls={"red": 2, "green": 1},
        num_balls_drawn=4,
        num_experiments=1000,
        seed=42
    )

    logging.info("Hat contents: %s", hat.contents)
    logging.info(
        "Estimated probability of drawing 2 red and 1 green in 4 draws: %.2f",
        probability,
    )

