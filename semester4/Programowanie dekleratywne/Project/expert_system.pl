main :- identify.

identify:-
  retractall(known(_,_,_)), % clear stored information
  race(X),
  write('The perfect dog for you: '),write(X),nl.
identify:-
  write('We don\'t have such a dog in our database.'),nl.

race(french_buldog):- 
  size(small), 
  temperament(calm),
  hair_length(short),
  origin(france),
  fur_type(fur),
  destiny(family).

race(dachshund):- 
  size(small), 
  temperament(calm),
  hair_length(short),
  origin(germany),
  fur_type(fur),
  destiny(hunting).

race(beagle):- 
  size(medium), 
  temperament(energetic),
  hair_length(short),
  origin(great_britain),
  fur_type(fur),
  destiny(hunting).

race(alaskan_malamute):- 
  size(big), 
  temperament(calm),
  hair_length(long),
  origin(usa),
  fur_type(fur),
  destiny(train).


race(golden_retriever):-
  size(medium), 
  temperament(calm),
  hair_length(long),
  origin(scotland),
  fur_type(fur),
  destiny(family).

race(american_pitbulterier):- 
  size(medium), 
  temperament(aggresive),
  hair_length(short),
  origin(great_britain),
  fur_type(fur),
  destiny(defensive).

race(border_collie):- 
  size(medium), 
  temperament(energic),
  hair_length(short),
  origin(scotland),
  fur_type(fur),
  destiny(shepherd).

race(maltese):- 
  size(small), 
  temperament(calm),
  hair_length(long),
  origin(italy),
  fur_type(hair),
  destiny(family).

race(doberman):-
  size(big),
  temperament(aggresive),
  hair_length(short),
  origin(germany),
  fur_type(fur),
  destiny(defensive).

race(german_shepherd):-
  size(big),
  temperament(energic),
  hair_length(short),
  origin(germany),
  fur_type(fur),
  destiny(defensive).

race(yorkshire_terrier):-
  size(small),
  temperament(energic),
  hair_length(long),
  origin(great_britain),
  fur_type(hair),
  destiny(family).

race(labrador_retriever):-
  size(big),
  temperament(energic),
  hair_length(long),
  origin(new_foundland),
  fur_type(fur),
  destiny(family).

size(X):- menuask(size, X, [big, small, medium]).
temperament(X):- menuask(temperament, X, [calm, aggresive, energic]).
hair_length(X):- menuask(hair_length, X, [long, short, short]).
origin(X):- menuask(origin, X, [france, germany, great_britain, usa, scotland, italy, new_foundland]).
fur_type(X):- menuask(fur_type, X, [fur, hair]).
type(X):- menuask(type, X, [family, hunting, maratonczyk, shepherd, train, defensive]).

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
                                    

pick_menu(_,_,inny,[]). 
pick_menu(N,N, Item, [Item|_]).      
pick_menu(Ctr,N, Val, [_|Rest]):-
  NextCtr is Ctr + 1,               
  pick_menu(NextCtr, N, Val, Rest).
