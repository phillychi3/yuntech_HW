WITH all_medical_events AS (
    SELECT
        p.patient_id,
        p.name as patient_name,
        a.appointment_date as event_date,
        'appointment' as event_type,
        d.name as doctor_name,
        mr.cases_id as event_detail
    FROM patients p
    JOIN appointments a ON p.patient_id = a.patient_id
    JOIN doctor d ON a.doctor_id = d.doctor_id
    LEFT JOIN medical_records mr ON a.appointment_id = mr.appointment_id
    UNION ALL

    SELECT
        p.patient_id,
        p.name as patient_name,
        e.examination_date as event_date,
        'examination' as event_type,
        NULL as doctor_name,
        e.examination_name as event_detail
    FROM patients p
    JOIN examination e ON p.patient_id = e.patient_id
    UNION ALL

    SELECT
        p.patient_id,
        p.name as patient_name,
        ar.admission_date as event_date,
        'admission' as event_type,
        NULL as doctor_name,
        ar.reason as event_detail
    FROM patients p
    JOIN admission_record ar ON p.patient_id = ar.patient_id
)
SELECT *
FROM all_medical_events
ORDER BY patient_id, event_date DESC;
-- 查詢每位病人的完整就醫歷史，包含門診、檢查和住院記錄