#Criar tabelas "aqui é SQL puro"
create table if not exist times (
    id integer primary key,
    nome text not null
);

create table if not exists partidas (
    id integer primary key autoincrement,
    fase text not null,
    time1 text not null,
    time2 text not null,
    gols1 integer,
    gols2 integer,
    vencedor text
);

#qual time marcou mais gols?
select time1 as time, sum(gols1) as total_gols from partidas group by time1
union all
select time2, sum(gols2) from partidas group by time
order by total_goals desc
limit 1;

#quantas partidas por fase?
select fase, count (*) as total_partidas
from partidas
group by fase;