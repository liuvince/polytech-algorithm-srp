# Stable Roommates Problem 
This is a demo of the Irving Algorithm for the Stable roommates problem. The code is written in Python with the easygui library. It was a simple code for school coursework during my first year at Polytech Sorbonne.

## Algorithm

The algorithm is very well explained on [Wikipedia](https://en.wikipedia.org/wiki/Stable_roommates_problem#Algorithm).

## Getting Started
```
python main.py
```

## Screenshots

![ScreenShot](https://github.com/liuvince/polytech-algorithm-srp/blob/master/images-for-demo/1.png)

![ScreenShot](https://github.com/liuvince/polytech-algorithm-srp/blob/master/images-for-demo/2.png)

![ScreenShot](https://github.com/liuvince/polytech-algorithm-srp/blob/master/images-for-demo/3.png)

![ScreenShot](https://github.com/liuvince/polytech-algorithm-srp/blob/master/images-for-demo/4.png)

![ScreenShot](https://github.com/liuvince/polytech-algorithm-srp/blob/master/images-for-demo/5.png)

## Example - Unit Test

We have 6 agents each with a preference list, ranking the other agents.

| Names | Choice 1 | Choice 2 | Choice 3 | Choice 4 | Choice 5 |
|-------|---|---|---|---|---|
|  *A*  | B | C | F | E | D |
|  *B*  | F | D | A | C | E |
|  *C*  | F | E | B | A | D |
|  *D*  | A | C | E | B | F |
|  *E*  | B | A | D | C | F |
|  *F*  | A | B | D | E | C |

### Phase 1
A -> B so B accepts A's offer

B -> F so F accepts B's offer

C -> F so F rejects C's offer

C -> E so E accepts C's offer

D -> A so A accepts D's offer

E -> B so B rejects E's offer

E -> A so A accepts E's offer, D is therefore rejected

D -> C so C accepts D's offer

F -> A so A accepts F's offer, E is therefore rejected

E -> D so D accepts E's offer

Finally,

|Name   | A | B | C | D | E | F |
|-------|--|--|--|--|--|--|
|accepts| F | A | D | E | C | B |

### Phase 2: Preference lists are reduced

| Names | Choice 1 | Choice 2 | Choice 3 | Choice 4 | Choice 5 |
|-------|---|---|---|---|---|
|  *A*  | B | C | F |   |   |
|  *B*  | F |   | A |   |   |
|  *C*  |   | E |   | A | D |
|  *D*  |   | C | E |   |   |
|  *E*  |   |   | D | C |   |
|  *F*  | A | B |   |   |   |

As one of the reduced list of the Phase 1 table contains more than one individual,
the algorithm enters phase 3.


### Phase 3: Find a rotation

To find a rotation, start at a p_0 containing at least two individuals in their reduced list, and define recursively q_{i+1} to be the second on p_i's list and p_{i+1} to be the last on q_{i+1}'s list, until this sequence repeats some p_{j}, at which point a rotation is found.

| p_i | A | D | C | F | A | 
|-----|---|---|---|---|---|
| q_i | C | E | A | B | C |  

Then, we reject simultaneously each q_i and p_{i+1} for i = [[0, 4]] in the reduced list.

| Names | Choice 1 | Choice 2 | Choice 3 | Choice 4 | Choice 5 |
|-------|---|---|---|---|---|
|  *A*  |   | C |   |   |   |
|  *B*  | F |   |   |   |   |
|  *C*  |   |   |   | A |   |
|  *D*  |   |   | E |   |   |
|  *E*  |   |   | D |   |   |
|  *F*  |   | B |   |   |   |

As each of the reduced list contains exactly one individual, the matching is stable.


## Authors

* **Vincent Liu** - *Polytech Sorbonne - MAIN 2019* - [LinkedIn](https://www.linkedin.com/in/liuvince25/)

## Acknowledgments

* Inspiration from [this Wikipedia's article](https://en.wikipedia.org/wiki/Stable_roommates_problem)
* Inspiration from [this research paper Stable Roommates and Constraint Programming written by Patrick Prosser ](http://www.dcs.gla.ac.uk/~pat/roommates/distribution/papers/cpaior2014.pdf)





