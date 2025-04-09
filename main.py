import random
import itertools
import datetime
import matplotlib.pyplot as plt


def generate_objects(nclasses):
    objects = []
    for nclass in range(nclasses):
        for i in range(3):
            price = random.randint(1, 50)
            size = random.randint(1, 50)
            objects.append((nclass+1,i+1,size,price))
    return objects


def generate_all_permutations(nclasses):
    permutations = itertools.product(range(3),repeat=nclasses)
    return permutations


def bruteforce_best_permutation(objects, permutations):
    start_time = datetime.datetime.now()
    best_permutation_objects = []
    best_price = 9999999999
    best_size = 99999999999
    max_size = int(len(objects)/3*20)
    for j,permutation in enumerate(permutations):
        permutation_size = 0
        permutation_price = 0
        permutation_objects = []
        for x,i in enumerate(permutation):
            current_object = objects[x*3+i]
            permutation_size += current_object[2]
            permutation_price += current_object[3]
            permutation_objects.append(current_object)
        if permutation_size <= max_size:
            if permutation_price <= best_price:
                best_price = permutation_price
                best_size = permutation_size
                best_permutation_objects = permutation_objects
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds()
    print(f'Calculation duration: {duration} s')
    return best_permutation_objects,best_size,best_price

if __name__ == '__main__':
    class_count = 5
    generated_objects = generate_objects(class_count)
    possible_permutations = generate_all_permutations(class_count)
    best_permutation,best_size,best_price = bruteforce_best_permutation(generated_objects, possible_permutations)
    row_labels = ['Trida','Id','Objem','Cena']
    plt.table(cellText=generated_objects,colLabels=row_labels, loc='center')
    plt.axis('off')
    plt.show()
    plt.table(cellText=best_permutation, colLabels=row_labels, loc='center')
    plt.axis('off')
    plt.title(f'Nejlepší kombinace objektů\nSumy - Objem: {best_size} Cena: {best_price}')
    plt.show()