0.1::burglary(N).
0.12::fire(N).
0.999999990252684::p_alarm1(N).
0.999999999999978::p_alarm2(N).
0.999999999999979::p_alarm3(N).
0.999999999999988::smoke(N) :- fire(N).
alarm(N) :- burglary(N), fire(N), p_alarm1(N).
alarm(N) :- burglary(N), \+fire(N), p_alarm2(N).
alarm(N) :- \+burglary(N), fire(N), p_alarm3(N).

