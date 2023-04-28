import matplotlib.pyplot as plt

def rouge_chart(rouge_r, rouge_p, rouge_f):
    # Set the width of each bar
    bar_width = 0.2

    # Set the position of each bar on the x-axis
    r1 = [0, 1, 2]
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]

    # Create the plot
    plt.bar(r1, rouge_r, width=bar_width, label='Summary 1')
    plt.bar(r2, rouge_p, width=bar_width, label='Summary 2')
    plt.bar(r3, rouge_f, width=bar_width, label='Summary 3')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()