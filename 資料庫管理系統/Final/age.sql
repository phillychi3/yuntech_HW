WITH patient_age_groups AS (
    SELECT
        p.patient_id,
        p.name,
        CASE
            WHEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, p.birthday)) < 18 THEN '未成年'
            WHEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, p.birthday)) BETWEEN 18 AND 30 THEN '青年'
            WHEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, p.birthday)) BETWEEN 31 AND 50 THEN '中年'
            WHEN EXTRACT(YEAR FROM AGE(CURRENT_DATE, p.birthday)) BETWEEN 51 AND 70 THEN '中老年'
            ELSE '老年'
        END as age_group
    FROM patients p
)
SELECT
    pag.age_group,
    COUNT(DISTINCT pag.patient_id) as patient_count,
    COUNT(DISTINCT a.appointment_id) as total_appointments,
    COUNT(DISTINCT e.examination_id) as total_examinations,
    COUNT(DISTINCT ar.admission_id) as total_admissions,
    ROUND(AVG(mc.amount)::numeric, 2) as avg_medical_cost
FROM patient_age_groups pag
LEFT JOIN appointments a ON pag.patient_id = a.patient_id
LEFT JOIN examination e ON pag.patient_id = e.patient_id
LEFT JOIN admission_record ar ON pag.patient_id = ar.patient_id
LEFT JOIN medical_costs mc ON pag.patient_id = mc.patient_id
GROUP BY pag.age_group
ORDER BY patient_count DESC;
-- 不同年齡層的就醫