#!/usr/bin/env python3
# coding: utf-8

import math, random
from argparse import ArgumentParser

def estimatePi(numberOfPoints):
  pointsInside = 0

  for i in range(0, numberOfPoints):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    
    if ( (x*x + y*y) < 1 ):
      pointsInside += 1
  
  piEstimate = (4.0*pointsInside)/numberOfPoints
  
  return piEstimate

def main(numberOfPoints):
  estimate = estimatePi(numberOfPoints)
  print('Estimate:\t{}'.format(estimate))
  print('Estimate error:\t{}'.format(abs(math.pi-estimate)))

def getArguments(parser):
  parser.add_argument("points", default=1000, help="Number of random points.", type=int)
  args = parser.parse_args()
  
  return args.points

if __name__ == '__main__':
  parser = ArgumentParser()
  numberOfPoints = getArguments(parser)
  main(numberOfPoints)
