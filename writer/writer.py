import os
import csv
import string
import random
import numpy as np
import matplotlib.pyplot as plt

def writer(attack_name, attack_func, hash_func, amount=100):
    dirname = '{}_results'.format(attack_name)
    if dirname not in os.listdir():
        os.mkdir(dirname)
    os.chdir(dirname)

    attacks_counts = []
    for i in range(amount):
        message = 'Меднікова Олександра Валеріївна + випадкове: {}'.format(random.choice(string.printable))
        message_hash = hash_func(message)

        count, messages, hashes = attack_func(message, message_hash, hash_func)
        attacks_counts.append(count)
        if i == 0:
            with open('{}_hashes.csv'.format(attack_name), 'w') as csvfile:
                writer = csv.writer(csvfile) 
                writer.writerow(['message', message])
                writer.writerow(['message_hash', message_hash])
                writer.writerow(['count', count])
                for j in range(30):
                    writer.writerow([j+1, messages[j], hashes[j]])

                if attack_name.startswith('p'):
                    writer.writerow([len(messages)-1, messages[-1], hashes[-1]])
                elif attack_name.startswith('b'):
                    coll1, coll2 = messages[-1]
                    numcoll1, numcoll2 = messages.index(coll1), messages.index(coll2)
                    writer.writerow([numcoll1 + 1, coll1, hashes[numcoll1]])
                    writer.writerow([numcoll2 + 1, coll2, hashes[numcoll2]])

    with open('{}_counts.csv'.format(attack_name), 'w') as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerow(['Attack', attack_name])
        writer.writerow(['M', np.mean(attacks_counts)])
        writer.writerow(['D', np.var(attacks_counts)])
        writer.writerow(['sigma', np.std(attacks_counts)])
        for k in range(amount):
            writer.writerow([k+1, attacks_counts[k]])

    fig, ax = plt.subplots()
    ax.bar(list(range(1, 101)), attacks_counts, color='violet')
    fig.savefig('{}.png'.format(attack_name))
    os.chdir('..')