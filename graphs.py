import matplotlib.pyplot as plt

def plot_graphs(latency_value):

    protocols = ['WPA2', 'WPA3', 'Proposed Protocol']

    # Use real value for proposed
    latency = [120, 180, latency_value]

    security = [2, 3, 5]
    privacy = [1, 2, 5]
    overhead = [2, 4, 3]

    # -------- LATENCY --------
    plt.bar(protocols, latency)
    plt.xlabel('Protocol')
    plt.ylabel('Latency (ms)')
    plt.title('Latency Comparison')
    plt.savefig("latency.png")
    plt.show()
    plt.clf()

    # -------- SECURITY --------
    plt.bar(protocols, security)
    plt.xlabel('Protocol')
    plt.ylabel('Security Level')
    plt.title('Security Comparison')
    plt.savefig("security.png")
    plt.show()
    plt.clf()

    # -------- PRIVACY --------
    plt.bar(protocols, privacy)
    plt.xlabel('Protocol')
    plt.ylabel('Privacy Level')
    plt.title('Privacy Comparison')
    plt.savefig("privacy.png")
    plt.show()
    plt.clf()

    # -------- OVERHEAD --------
    plt.bar(protocols, overhead)
    plt.xlabel('Protocol')
    plt.ylabel('Computational Overhead')
    plt.title('Overhead Comparison')
    plt.savefig("overhead.png")
    plt.show()