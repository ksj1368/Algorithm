-- 코드를 입력하세요
SELECT
    AO.ANIMAL_ID,
    AO.NAME
FROM 
    ANIMAL_OUTS AS AO
LEFT OUTER JOIN
    ANIMAL_INS AS AI
ON
    AO.ANIMAL_ID = AI.ANIMAL_ID
ORDER BY
    DATEDIFF(AO.DATETIME, AI.DATETIME) DESC
LIMIT 2;