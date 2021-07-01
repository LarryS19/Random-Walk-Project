from random import choice


class RandomWalk:
    """A random walk generator"""

    def __init__(self, num_points=10000):
        """Initialize attributes"""
        self.num_points = num_points

        # Create lists that will hold all x and y points, all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Calculate all the points in the walk"""
        # Choose positive or negative (Cartesian coordinate system)
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])  # choose how far
        step = direction * distance
        return step

    def fill_walk(self):
        """Insert and append calculated steps to list"""
        # Keep taking steps until num_points has been reached
        while len(self.x_values) < self.num_points:

            # 'get_step' decides direction and how far to go in that direction
            x_step = self.get_step()
            y_step = self.get_step()

            # Do not append if x and y step = 0
            if x_step and y_step == 0:
                continue

            # Calculate new step
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Add points to list
            self.x_values.append(x)
            self.y_values.append(y)
