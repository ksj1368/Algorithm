-- 코드를 입력하세요
SELECT
    A.APNT_NO,
    P.PT_NAME,
    A.PT_NO,
    A.MCDP_CD,
    D.DR_NAME,
    A.APNT_YMD
FROM
    APPOINTMENT AS A
JOIN DOCTOR AS D
    ON D.DR_ID = A.MDDR_ID
JOIN PATIENT AS P
    ON P.PT_NO = A.PT_NO
WHERE
    A.MCDP_CD = 'CS'
    AND
    A.APNT_YMD LIKE '2022-04-13%'
    AND
    APNT_CNCL_YMD IS NULL
ORDER BY
    A.APNT_YMD ASC;

