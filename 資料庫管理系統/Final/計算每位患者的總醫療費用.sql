SELECT
p.name AS patient_name,
SUM(mc.amount) AS total_cost
FROM
patients p
JOIN
medical_costs mc ON p.patient_id = mc.patient_id
GROUP BY
p.name;