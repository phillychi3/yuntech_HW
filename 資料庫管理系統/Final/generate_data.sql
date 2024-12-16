CREATE OR REPLACE FUNCTION random_name() RETURNS TEXT AS $$
DECLARE
    first_names TEXT[] := ARRAY['王', '李', '張', '劉', '陳', '楊', '黃', '趙', '吳', '周', '林', '徐', '孫', '馬', '朱', '胡', '郭', '何', '高', '羅'];
    last_names TEXT[] := ARRAY['小明', '大明', '志明', '俊傑', '建志', '文華', '家豪', '志豪', '志偉', '俊宏', '怡君', '淑芬', '淑華', '美玲', '雅婷', '麗華', '美華'];
BEGIN
    RETURN first_names[1 + floor(random() * array_length(first_names, 1))] ||
           last_names[1 + floor(random() * array_length(last_names, 1))];
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION random_address() RETURNS TEXT AS $$
DECLARE
    districts TEXT[] := ARRAY['中正區', '大安區', '信義區', '士林區', '北投區', '內湖區', '松山區', '萬華區'];
    roads TEXT[] := ARRAY['中山路', '忠孝路', '信義路', '仁愛路', '和平路', '民生路', '南京路', '建國路'];
BEGIN
    RETURN '台北市' ||
           districts[1 + floor(random() * array_length(districts, 1))] ||
           roads[1 + floor(random() * array_length(roads, 1))] ||
           floor(random() * 500 + 1)::TEXT || '號';
END;
$$ LANGUAGE plpgsql;

DO $$
DECLARE
    i INTEGER;
    gender_arr VARCHAR[] := ARRAY['男', '女', '非二元', '其他'];
    specialist_arr VARCHAR[] := ARRAY['內科', '外科', '小兒科', '婦產科', '骨科', '眼科', '耳鼻喉科', '皮膚科', '神經科', '精神科', '家醫科', '急診醫學科'];
BEGIN
    FOR i IN 1..200 LOOP
        INSERT INTO doctor (
            name,
            specialist,
            sexual,
            phone_numbers,
            email,
            address
        ) VALUES (
            random_name(),
            specialist_arr[1 + floor(random() * array_length(specialist_arr, 1))],
            gender_arr[1 + floor(random() * array_length(gender_arr, 1))],
            '09' || floor(random() * (99999999 - 10000000 + 1) + 10000000)::TEXT,
            'doctor' || i || '@hospital.com',
            random_address()
        );
    END LOOP;
END $$;

INSERT INTO clinic (floor, building, address)
SELECT
    floor(random() * 10) + 1,
    chr(65 + floor(random() * 5)::integer) || '棟',
    random_address()
FROM generate_series(1, 30);

DO $$
DECLARE
    i INTEGER;
    gender_arr VARCHAR[] := ARRAY['男', '女', '非二元', '其他'];
    gender VARCHAR;
    birth_date DATE;
BEGIN
    FOR i IN 1..100 LOOP
        gender := gender_arr[1 + floor(random() * 4)];
        birth_date := CURRENT_DATE - ((18 + floor(random() * 20))::INTEGER || ' years')::INTERVAL;

        INSERT INTO patients (
            name,
            birthday,
            sexual,
            phone_numbers,
            email,
            address
        ) VALUES (
            '病人' || i,
            birth_date,
            gender,
            '09' || floor(random() * (99999999 - 10000000 + 1) + 10000000)::TEXT,
            'patient' || i || '@email.com',
            '臺灣' || (500 + i) || '號'
        );
    END LOOP;
END $$;

CREATE OR REPLACE FUNCTION generate_appointments(
    start_date DATE,
    end_date DATE,
    appointment_count INTEGER
) RETURNS void AS $$
DECLARE
    curr_date DATE;
    curr_time TIME;
    selected_doctor_id INTEGER;
    selected_patient_id INTEGER;
    selected_clinic_id INTEGER;
    current_weekday INTEGER;
    appointment_interval INTERVAL := '30 minutes';
    max_daily_appointments INTEGER := 8;
    daily_count INTEGER;
BEGIN
    CREATE TEMP TABLE IF NOT EXISTS available_patients AS
    SELECT patient_id
    FROM patients;


    curr_date := start_date;

    WHILE curr_date <= end_date AND appointment_count > 0 LOOP
        current_weekday := EXTRACT(DOW FROM curr_date);
        IF current_weekday = 0 THEN current_weekday := 7; END IF;


        FOR selected_doctor_id IN (
            SELECT DISTINCT ds.doctor_id
            FROM doctor_schedule ds
            WHERE ds.weekday = current_weekday
            AND NOT EXISTS (
                SELECT 1 FROM doctor_leaves dl
                WHERE dl.doctor_id = ds.doctor_id
                AND dl.leave_date = curr_date
            )
            LIMIT 5
        ) LOOP

            SELECT COUNT(*) INTO daily_count
            FROM appointments
            WHERE doctor_id = selected_doctor_id
            AND appointment_date = curr_date;

            IF daily_count < max_daily_appointments THEN
                SELECT ds.start_time INTO curr_time
                FROM doctor_schedule ds
                WHERE ds.doctor_id = selected_doctor_id
                AND ds.weekday = current_weekday
                LIMIT 1;

                SELECT clinic_id INTO selected_clinic_id
                FROM clinic
                ORDER BY RANDOM()
                LIMIT 1;

                WHILE daily_count < max_daily_appointments AND appointment_count > 0
                AND curr_time < '17:00:00'::TIME LOOP
                    WITH available_today AS (
                        SELECT p.patient_id
                        FROM available_patients p
                        WHERE NOT EXISTS (
                            SELECT 1
                            FROM appointments a
                            WHERE a.patient_id = p.patient_id
                            AND a.appointment_date = curr_date
                        )
                        LIMIT 100
                    )
                    SELECT patient_id INTO selected_patient_id
                    FROM available_today
                    ORDER BY RANDOM()
                    LIMIT 1;

                    IF FOUND THEN
                        INSERT INTO appointments (
                            doctor_id,
                            patient_id,
                            clinic_id,
                            appointment_date,
                            appointment_time,
                            status
                        ) VALUES (
                            selected_doctor_id,
                            selected_patient_id,
                            selected_clinic_id,
                            curr_date,
                            curr_time,
                            'confirmed'
                        );

                        appointment_count := appointment_count - 1;
                        daily_count := daily_count + 1;
                        curr_time := curr_time + appointment_interval;
                    ELSE
                        curr_time := curr_time + appointment_interval;
                    END IF;
                END LOOP;
            END IF;

            EXIT WHEN appointment_count <= 0;
        END LOOP;

        curr_date := curr_date + 1;
    END LOOP;


    DROP TABLE IF EXISTS available_patients;
END;
$$ LANGUAGE plpgsql;


TRUNCATE appointments CASCADE;


SELECT generate_appointments('2024-12-16', '2024-12-31', 300);