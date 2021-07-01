import matplotlib.pyplot as plt

from randomwalk import RandomWalk

# Keep making new walk visualizations as long as the user wants to.
while True:
    # Create an instance of RandomWalk class.
    rw = RandomWalk()
    rw.fill_walk()

    # Set up plot
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))  # figsize arg sets size of figure using tuple.
    point_numbers = range(rw.num_points)  # rw.num_points used as num_points can be changed, used for cmap.
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='None', s=7)

    # Emphasize first and last points of random walk.
    ax.scatter(0, 0, c='green', edgecolors='None', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='None', s=100)

    # Customize labels.
    ax.set_title('Random Walk', fontsize=14)
    # Removing axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    run_again = input('Make another random walk? (Y/N)?: ')
    if run_again.title() == 'N':
        break
