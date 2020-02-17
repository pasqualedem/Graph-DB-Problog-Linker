t(_)::burglary(N).
t(_)::fire(N).
t(_)::p_alarm1(N).
t(_)::p_alarm2(N).
t(_)::p_alarm3(N).
t(0.2)::smoke(N) :- fire(N).
alarm(N) :- burglary(N), fire(N), p_alarm1(N).
alarm(N) :- burglary(N), \+fire(N), p_alarm2(N).
alarm(N) :- \+burglary(N), fire(N), p_alarm3(N).