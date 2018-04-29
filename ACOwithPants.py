import pants
import math
import random
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
import argparse

nodes = []
invalid_lines = 0

#Traitement des arguements
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-p", "--parse_only", help="Only to test parser",
                    action="store_true")
args = parser.parse_args()

# Traitement du fichier
with open('open_pubs.csv', newline='') as file:
    reader = csv.reader(file,delimiter=",")
    next(reader)
    for row in reader:
        try:
            if(row[8] == 'City of London'):
                nodes.append((int(row[5]), int(row[4])))
                if args.verbose:
                    print(int(row[5]), int(row[4]))
        except ValueError:
            invalid_lines += 1
            if args.verbose:
                print(row[1] + "contaoins invalid data")

#Affichage du nombres d'erreurs
if invalid_lines >= 1:
    print( "CSV Contains " + str(invalid_lines) + " invalid line(s)")       
nodes = list(set(nodes))

print('Pubs: ', len(nodes))


def distance(a, b):  # get distance in kilometers
    distance = math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))/1000
    return distance

if args.parse_only != True:
    world = pants.World(nodes, distance)
    solver = pants.Solver()
    solutions = solver.solutions(world)

    bestDistance = -1
    for solution in solutions:
        if(solution.distance < bestDistance or bestDistance < 0):
            bestDistance = solution.distance
            bestTour = solution.tour

    print('Distance parcourue : ' + str(bestDistance) + 'km')

    xArray = []
    yArray = []
    for node in bestTour:  # split nodes in 2 arrays for matplotlib
        xArray.append(node[0])
        yArray.append(node[1])
    plt.plot(xArray, yArray)
    plt.show()