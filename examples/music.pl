0.2::genre(A,G) :- birthDate(A,D1), birthDate(B,D2), D1 is D2, genre(B,G).

birthDate(giacomo,1955.0).
query(genre(giacomo,X)).