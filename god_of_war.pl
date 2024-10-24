% man Class
man("Kratos").
man("Atrey").
man("Mimir").
man("Odin").
man("Baldur").
man("Thor").
man("Brok").
man("Sindri").
man("Tur").
man("Magni").
man("Modi").
man("Durlin").
man("Fenrir").
man("Jormungandr").
man("Zeus").

% Woman class
female("Freya").
female("Angroba").
female("Athena").
female("Gaia").
female("Styx").
female("Pandrora").

% relationship between characters.
parent("Kratos","Atrey").
parent("Zeus","Kratos").
parent("Styx","Kratos").
parent("Odin","Thor").
parent("Odin","Magni").
parent("Odin","Modi").
parent("Odin","Mag").
parent("Odin","Baldur").
parent("Freya","Baldur").

% Enemies.
enemy("Kratos","Odin").
enemy("Atrey","Odin").
enemy("Mimir","Odin").
enemy("Sindri","Odin").
enemy("Brok","Odin").
enemy("Jormungandr","Odin").
enemy("Kratos","Thor").
enemy("Kratos","Magni").
enemy("Kratos","Baldur").

% Also we have love.
suri_muri("Kratos","Freya").
suri_muri("Odin","Freya").
suri_muri("Atrey","Pandrora").


% rule that male persoange is father
father(A,B)		:- parent(A,B),man(A).

% rule that female persoange is father
mother(A,B)		:- parent(A,B),female(A). 

% rule that male personage has father or mother
sun(A, B)               :- parent(A, B), male(B).

% rule that female personage has father or mother
daugther(A, B)          :- parent(A, B), female(B).

% rule that personage has grandfather
grandfather(A, B)       :- parent(A,C), parent(C,B), man(A).

% rule that personage has grandmother
grandmother(A, B)	:- parent(A,C), parent(C,B), female(A).

% rule that characters are friends if they have common enemy
friend(A,B)		:- enemy(A,C), enemy(B,C), A \= B.

% rule that characters have brother if  another character have the same parents and male. 
brother(A, B)           :- brother_or_sister(A, B), man(B).

% rule that characters have brother if  another character have the same parents and female. 
sister(A, B)            :- brother_or_sister(A, B), female(B).

brother_or_sister(A, B) :- father(C, A),father(C,B),mother(D,A),mother(D,B), A \= B.

% Woman is a distraction
% rule that show woman can be a problem if they have shuri_muir with both man.
man_conflict(A,B,C)       :- suri_muri(A,C),suri_muri(B,C), A \=B,man(A),man(B).

woman_is_bad(A)         :- man_conflict(_,_,A).

% man can be friends if they not love one woman and they are not enemies or they love one woman but they have common enemy
can_be_friends(A,B)     :-  ( \+ man_conflict(A,B,_), \+ enemy(A,B), A \= B);(man_conflict(A,B,_),friend(A,B)).