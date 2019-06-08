# Stable roommates problem 
This is a demo of the Irving Algorithm for the Stable roommates problem. The code is written in Python with the easygui library. It was a simple code for school coursework during my first year at Polytech Sorbonne.

## Getting Started
```
python main.py
```

## Algorithm

The algorithm is very well explained on [Wikipedia](https://en.wikipedia.org/wiki/Stable_roommates_problem#Algorithm).
## Example

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
A -> B et B accepts A's offer

B -> F et F accepts B's offer

C -> F et F rejects C's offer

C -> E et E accepts C's offer

D -> A et A accepts D's offer

E -> B et B rejects E's offer

E -> A et A accepts E's offer, D is therefore rejected

D -> C et C accepts D's offer

F -> A et A accepts F's offer, E is therefore rejected

E -> D et D accepts E's offer

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



## Authors

* **Vincent Liu** - *Polytech Sorbonne - MAIN 2019* - [LinkedIn](https://www.linkedin.com/in/liuvince25/)

## Acknowledgments

* Inspiration from [this Wikipedia's article](https://en.wikipedia.org/wiki/Stable_roommates_problem)
* Inspiration from [this research paper Stable Roommates and Constraint Programming written by Patrick Prosser ](http://www.dcs.gla.ac.uk/~pat/roommates/distribution/papers/cpaior2014.pdf)





