# Shrimp Simulator

- A python program with [pyGame](https://www.pygame.org/news) to simulate fresh water shrimp breeding and selling.
- As a shrimp breeder, I have been fascinated by these little critters and thus the motivation for this program. 

#### Work in progress-
- need to tweak parameters
- need to implement more event handling and refactoring 
- minor bug fixes in shrimp crossing.

## How to use:

- A player is given credit to buy four types of shrimps. User can freely buy and sell their four shrimps.
- Shrimp will have finite fitness and as month progresses they are likely to pass away. 
- When shrimp is purchased, it can be either male or females. As time is progressed, if there are both males and females,
shrimp will be pregant (berried) and after certain time has passed, they will give birth to babies which will increase your 
inventory, which you can sell off.
- player can purchase lottery to unlock unknown shrimp collections. Some shrimps will not show up on lottery unless you have unlocked
a certain type already. 

### Shrimp genetics

- each shrimp has 2 genes and each gene is in pairs (diploid): Crystal and Color gene.
-based on mating, a shrimp can have different genetic variations and if different shrimps are mixed and mated(complete random
among all shrimps), then their offspring could be different type compared to their parents.
 check out [dihybrid cross](http://www.biology.arizona.edu/mendelian_genetics/problem_sets/dihybrid_cross/03t.html) for more info.

### About Dwarf Shrimps (in real life)
- Dwarf shrimps are fresh water shrimp that can thrive well in a small aquarium. A type of this shrimp is called bee shrimp and it's becoming more and more popular due to their beautiful appearances. Over the past years, shrimp breeders have selectively bred shrimps which resulted in stronger and different phenotypes. These include the popular crystal red/black shrimps, tiger shrimps and taiwan bee shrimps.



