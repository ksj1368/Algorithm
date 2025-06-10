select
    concat(quarter(DIFFERENTIATION_DATE), 'Q') as QUARTER,
    count(ID) as ECOLI_COUNT
from   
    ECOLI_DATA
group by
    QUARTER
order by
   QUARTER asc;
    