with HR_TOTAL_GRADE as (
    select  
        EMP_NO,
        sum(SCORE) as SCORE
    from
        HR_GRADE
    where
        YEAR = '2022'
    group by
        EMP_NO
)

select
    htg.SCORE as SCORE,
    he.EMP_NO as EMP_NO,
    he.EMP_NAME as EMP_NAME,
    he.POSITION as POSITION,
    he.EMAIL as EMAIL
from
    HR_EMPLOYEES as he
join HR_TOTAL_GRADE as htg on he.EMP_NO = htg.EMP_NO
where
    htg.SCORE = (
        select 
            max(SCORE) 
        from 
            HR_TOTAL_GRADE
    )