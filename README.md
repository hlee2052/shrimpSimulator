# Shrimp Simulator

A python program with * [pyGame](https://www.pygame.org/news) to simulate fresh water shrimp breeding and selling.
  

- Work in progress-
- need to tweak parameters
- need to implement more event handling and refactoring 
- minor bug fixes in shrimp crossing.

## How to use:

- A player is given credit to buy four types of shrimps. User can freely buy and sell their four shrimps.
- Shrimp will have finite fitness and as month progresses they are likely to pass away. 
- When shrimp is purchased, it can be either male or females. As time is progressed, if there are both males and females,
shrimp will be pregant (berried) and after certain time has passed, they will give birth to babies which will increase your 
inventory, which you can sell off.

### Shrimp genetics

-each shrimp has 2 genes and each gene is in pairs (diploid): Crystal and Color gene.
-based on mating, a shrimp can have different genetic variations and if different shrimps are mixed and mated(complete random
among all shrimps), then their offspring could be different type compared to their parents.
 check out* [dihybrid] (http://www.biology.arizona.edu/mendelian_genetics/problem_sets/dihybrid_cross/03t.html) for more info.


