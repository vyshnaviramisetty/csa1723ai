% Facts about birds and their ability to fly
can_fly(crow).
can_fly(sparrow).
can_fly(eagle).
cannot_fly(penguin).
cannot_fly(ostrich).

% Rules to determine if a bird can fly
fly(X) :- can_fly(X).
fly(X) :- \+cannot_fly(X).

