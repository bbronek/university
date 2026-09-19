:- dynamic known/3.

main :- identify.

identify:-
  retractall(known(_,_,_)), % clear stored information
  breed(X), !,
  write('The perfect dog for you: '),write(X),nl.
identify:-
  write('We don\'t have such a dog in our database.'),nl.

breed(french_bulldog):-
  size(small),
  temperament(calm),
  hair_length(short),
  origin(france),
  fur_type(fur),
  purpose(family).

breed(dachshund):-
  size(small),
  temperament(calm),
  hair_length(short),
  origin(germany),
  fur_type(fur),
  purpose(hunting).

breed(beagle):-
  size(medium),
  temperament(energetic),
  hair_length(short),
  origin(great_britain),
  fur_type(fur),
  purpose(hunting).

breed(alaskan_malamute):-
  size(big),
  temperament(calm),
  hair_length(long),
  origin(usa),
  fur_type(fur),
  purpose(sled).


breed(golden_retriever):-
  size(medium),
  temperament(calm),
  hair_length(long),
  origin(scotland),
  fur_type(fur),
  purpose(family).

breed(american_pit_bull_terrier):-
  size(medium),
  temperament(aggressive),
  hair_length(short),
  origin(great_britain),
  fur_type(fur),
  purpose(defensive).

breed(border_collie):-
  size(medium),
  temperament(energetic),
  hair_length(short),
  origin(scotland),
  fur_type(fur),
  purpose(shepherd).

breed(maltese):-
  size(small),
  temperament(calm),
  hair_length(long),
  origin(italy),
  fur_type(hair),
  purpose(family).

breed(doberman):-
  size(big),
  temperament(aggressive),
  hair_length(short),
  origin(germany),
  fur_type(fur),
  purpose(defensive).

breed(german_shepherd):-
  size(big),
  temperament(energetic),
  hair_length(short),
  origin(germany),
  fur_type(fur),
  purpose(defensive).

breed(yorkshire_terrier):-
  size(small),
  temperament(energetic),
  hair_length(long),
  origin(great_britain),
  fur_type(hair),
  purpose(family).

breed(labrador_retriever):-
  size(big),
  temperament(energetic),
  hair_length(long),
  origin(newfoundland),
  fur_type(fur),
  purpose(family).

size(X):- menuask(size, X, [big, small, medium]).
temperament(X):- menuask(temperament, X, [calm, aggressive, energetic]).
hair_length(X):- menuask(hair_length, X, [long, short]).
origin(X):- menuask(origin, X, [france, germany, great_britain, usa, scotland, italy, newfoundland]).
fur_type(X):- menuask(fur_type, X, [fur, hair]).
purpose(X):- menuask(purpose, X, [family, hunting, runner, shepherd, sled, defensive]).

menuask(Attribute,Value,_):-
  known(yes,Attribute,Value),
  !.
menuask(Attribute,_,_):-
  known(yes,Attribute,_),
  !, fail.

menuask(Attribute,AskValue,Menu):-
  nl,write('Which option for '),write(Attribute),write('?'),nl,
  display_menu(Menu),
  write('Enter number of choice: '),
  read(Num),nl,
  pick_menu(Num,AnswerValue,Menu),
  asserta(known(yes,Attribute,AnswerValue)),
  AskValue = AnswerValue.

display_menu(Menu):-
  menu(1,Menu), !.

menu(_,[]).
menu(N,[Item | Rest]):-
  write(N),write(' : '),write(Item),nl,
  NN is N + 1,
  menu(NN,Rest).

pick_menu(N,Val,Menu):-
  integer(N),
  pick_menu(1,N,Val,Menu), !.
  pick_menu(Val,Val,_).


pick_menu(_,_,other,[]).
pick_menu(N,N, Item, [Item|_]).
pick_menu(Ctr,N, Val, [_|Rest]):-
  NextCtr is Ctr + 1,
  pick_menu(NextCtr, N, Val, Rest).
