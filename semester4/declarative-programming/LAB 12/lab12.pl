% zad 1

intersection([X|Y],M,[X|Z]) :- member(X,M), intersection(Y,M,Z).
intersection([X|Y],M,Z) :- \+ member(X,M), intersection(Y,M,Z).
intersection([],M,[]).

union([X|Y],Z,W) :- member(X,Z),  union(Y,Z,W).
union([X|Y],Z,[X|W]) :- \+ member(X,Z), union(Y,Z,W).
union([],Z,Z).
        
subtract([], _, []).
subtract([X|Y], W, Z) :- memberchk(X, W), !, subtract(Y, W, Z).
subtract([X|Y], W, [X|Z]) :- subtract(Y, W, Z).

% zad 2

% a)
delete([], A, []).
delete([Y|K], X, [Y|M]):- delete(K, X, M), dif(X, Y).
delete([X|K], X, R) :- delete(K, X, R).

% b)
select(E,[E|Xs],Xs).
select(E,[X|Xs],[X|Ys]) :- select(E,Xs,Ys).

% c)
permutation([],[]).
permutation([H|T],S) :- permutation(T,P),append(X,Y,P),append(X,[H|Y],S).

% d)
sort(List,Sorted):-b_sort(List,[],Sorted).
b_sort([],Acc,Acc).
b_sort([H|T],Acc,Sorted):-bubble(H,T,NT,Max),b_sort(NT,[Max|Acc],Sorted).

bubble(X,[],[],X).
bubble(X,[Y|T],[Y|NT],Max):-X>Y,bubble(X,T,NT,Max).
bubble(X,[Y|T],[X|NT],Max):-X=<Y,bubble(Y,T,NT,Max).
