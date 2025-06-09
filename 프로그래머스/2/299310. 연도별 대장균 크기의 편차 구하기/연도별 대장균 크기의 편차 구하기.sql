with MAX_SIZE_BY_YEAR as (
    select
        date_format(DIFFERENTIATION_DATE, '%Y') as YEAR,
        max(SIZE_OF_COLONY) as MAX_SIZE
    from
        ECOLI_DATA 
    group by
        YEAR
)

select
    cast(date_format(DIFFERENTIATION_DATE, '%Y') as unsigned) AS YEAR,
    abs(msby.MAX_SIZE - ed.SIZE_OF_COLONY) as YEAR_DEV,
    ID
from
    ECOLI_DATA as ed
join MAX_SIZE_BY_YEAR as msby on date_format(ed.DIFFERENTIATION_DATE, '%Y') = msby.YEAR
order by
    YEAR asc,
    YEAR_DEV asc;