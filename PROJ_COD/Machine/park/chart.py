import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    num_bars = len(data)
    positions = range (1, num_bars+1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.xlabel('rate')
    plt.ylabel('type')
    plt.show()

if __name__ == '__main__':
    steps = [60, 40]
    labels = ['Trojan', 'Adware']
    create_bar_chart(steps, labels)