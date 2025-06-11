with HR_GRADE_TIER as (
    select
        EMP_NO,
        case
            when avg(SCORE) >= 96 then 'S'
            when avg(SCORE) < 96 and avg(SCORE) >= 90 then 'A'
            when avg(SCORE) < 90 and avg(SCORE) >= 80 then 'B'
            else 'C'
        end as GRADE
    from
        HR_GRADE
    group by
        EMP_NO, YEAR
    
)
 
select
    he.EMP_NO,
    he.EMP_NAME,
    hgt.GRADE,
    case
        when GRADE = 'S' then he.SAL * 0.2 
        when GRADE = 'A' then he.SAL * 0.15 
        when GRADE = 'B' then he.SAL * 0.1 
        else 0
    end as BONUS
from
    HR_EMPLOYEES as he
join HR_GRADE_TIER as hgt on he.EMP_NO = hgt.EMP_NO
order by
    he.EMP_NO asc;