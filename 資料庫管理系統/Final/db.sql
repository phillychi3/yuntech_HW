DROP TABLE IF EXISTS prescription_medicines CASCADE;
DROP TABLE IF EXISTS medical_costs CASCADE;
DROP TABLE IF EXISTS schedules CASCADE;
DROP TABLE IF EXISTS medical_records CASCADE;
DROP TABLE IF EXISTS appointments CASCADE;
DROP TABLE IF EXISTS admission_record CASCADE;
DROP TABLE IF EXISTS examination CASCADE;
DROP TABLE IF EXISTS prescription CASCADE;
DROP TABLE IF EXISTS medicine CASCADE;
DROP TABLE IF EXISTS clinic CASCADE;
DROP TABLE IF EXISTS doctor CASCADE;
DROP TABLE IF EXISTS patients CASCADE;
DROP TABLE IF EXISTS date CASCADE;
DROP TABLE IF EXISTS doctor_leaves CASCADE;
DROP TABLE IF EXISTS doctor_schedule CASCADE;


CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birthday DATE NOT NULL,
    sexual VARCHAR(10) NOT NULL CHECK (sexual IN ('男', '女', '非二元','其他')),
    phone_numbers VARCHAR(20) NOT NULL CHECK (phone_numbers ~ '^[0-9\+\-]{8,}$'),
    email VARCHAR(100) NOT NULL CHECK (email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    address TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE doctor (
    doctor_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialist VARCHAR(100) NOT NULL,
    sexual VARCHAR(10) NOT NULL CHECK (sexual IN ('男', '女', '非二元','其他')),
    phone_numbers VARCHAR(20) NOT NULL CHECK (phone_numbers ~ '^[0-9\+\-]{8,}$'),
    email VARCHAR(100) NOT NULL CHECK (email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    address TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE clinic (
    clinic_id SERIAL PRIMARY KEY,
    floor INTEGER NOT NULL,
    building VARCHAR(50) NOT NULL,
    address TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE date (
    date_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    clinic_id INTEGER REFERENCES clinic(clinic_id),
    hospital_stay_date DATE,
    examination_date DATE,
    payment_deadline DATE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE medicine (
    medication_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    instructions TEXT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE prescription (
    prescription_id SERIAL PRIMARY KEY,
    doctor_id INTEGER NOT NULL REFERENCES doctor(doctor_id),
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id),
    prescription_date DATE NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    dosage TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE prescription_medicines (
    prescription_id INTEGER REFERENCES prescription(prescription_id),
    medication_id INTEGER REFERENCES medicine(medication_id),
    dosage VARCHAR(100) NOT NULL,
    instructions TEXT NOT NULL,
    PRIMARY KEY (prescription_id, medication_id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    doctor_id INTEGER NOT NULL REFERENCES doctor(doctor_id),
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id),
    clinic_id INTEGER NOT NULL REFERENCES clinic(clinic_id),
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE medical_records (
    appointment_id INTEGER PRIMARY KEY REFERENCES appointments(appointment_id),
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id),
    doctor_id INTEGER NOT NULL REFERENCES doctor(doctor_id),
    cases_id VARCHAR(50) NOT NULL,
    prescription_id INTEGER REFERENCES prescription(prescription_id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE examination (
    examination_id SERIAL PRIMARY KEY,
    examination_name VARCHAR(100) NOT NULL,
    examination_date DATE NOT NULL,
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id),
    result TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE admission_record (
    admission_id SERIAL PRIMARY KEY,
    clinic_id INTEGER NOT NULL REFERENCES clinic(clinic_id),
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id),
    admission_date DATE NOT NULL,
    discharge_date DATE,
    reason TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE medical_costs (
    cost_id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id),
    payment_deadline DATE NOT NULL,
    prescription_id INTEGER REFERENCES prescription(prescription_id),
    amount DECIMAL(10,2) NOT NULL,
    payment_status VARCHAR(20) NOT NULL,
    created_date DATE NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE doctor_schedule (
    schedule_id SERIAL PRIMARY KEY,
    doctor_id INTEGER NOT NULL REFERENCES doctor(doctor_id),
    weekday INTEGER NOT NULL CHECK (weekday BETWEEN 1 AND 7),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    max_patients INTEGER NOT NULL DEFAULT 20,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (doctor_id, weekday)
);


CREATE TABLE doctor_leaves (
    leave_id SERIAL PRIMARY KEY,
    doctor_id INTEGER NOT NULL REFERENCES doctor(doctor_id),
    leave_date DATE NOT NULL,
    leave_type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (doctor_id, leave_date)
);


CREATE INDEX idx_patient_name ON patients(name);
CREATE INDEX idx_doctor_name ON doctor(name);
CREATE INDEX idx_appointment_date ON appointments(appointment_date);
CREATE INDEX idx_prescription_date ON prescription(prescription_date);
CREATE INDEX idx_examination_date ON examination(examination_date);
CREATE INDEX idx_medical_costs_deadline ON medical_costs(payment_deadline);

CREATE OR REPLACE FUNCTION check_doctor_availability()
RETURNS TRIGGER AS $$
DECLARE
    weekday_num INTEGER;
    schedule_record RECORD;
    appointment_count INTEGER;
    is_on_leave BOOLEAN;
BEGIN

    weekday_num := EXTRACT(DOW FROM NEW.appointment_date);
    IF weekday_num = 0 THEN weekday_num := 7; END IF;


    SELECT EXISTS (
        SELECT 1 FROM doctor_leaves
        WHERE doctor_id = NEW.doctor_id
        AND leave_date = NEW.appointment_date
    ) INTO is_on_leave;

    IF is_on_leave THEN
        RAISE EXCEPTION '醫生在該日期休假';
    END IF;


    SELECT * INTO schedule_record
    FROM doctor_schedule
    WHERE doctor_id = NEW.doctor_id
    AND weekday = weekday_num;

    IF NOT FOUND THEN
        RAISE EXCEPTION '醫生在該日期沒有排班';
    END IF;

    IF NEW.appointment_time < schedule_record.start_time
    OR NEW.appointment_time > schedule_record.end_time THEN
        RAISE EXCEPTION '預約時間不在醫生工作時間內';
    END IF;


    SELECT COUNT(*) INTO appointment_count
    FROM appointments
    WHERE doctor_id = NEW.doctor_id
    AND appointment_date = NEW.appointment_date
    AND status = 'confirmed';

    IF appointment_count >= schedule_record.max_patients THEN
        RAISE EXCEPTION '該日期的預約已達上限';
    END IF;


    SELECT COUNT(*) INTO appointment_count
    FROM appointments
    WHERE doctor_id = NEW.doctor_id
    AND appointment_date = NEW.appointment_date
    AND appointment_time = NEW.appointment_time
    AND status = 'confirmed';

    IF appointment_count > 0 THEN
        RAISE EXCEPTION '該時段已有其他預約';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER before_appointment_insert
    BEFORE INSERT OR UPDATE ON appointments
    FOR EACH ROW
    EXECUTE FUNCTION check_doctor_availability();


CREATE OR REPLACE FUNCTION check_patient_appointment_conflict()
RETURNS TRIGGER AS $$
DECLARE
    conflict_count INTEGER;
BEGIN

    SELECT COUNT(*) INTO conflict_count
    FROM appointments
    WHERE patient_id = NEW.patient_id
    AND appointment_date = NEW.appointment_date
    AND appointment_time = NEW.appointment_time
    AND status = 'confirmed'
    AND appointment_id != COALESCE(NEW.appointment_id, 0);

    IF conflict_count > 0 THEN
        RAISE EXCEPTION '病人在該時段已有其他預約';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_patient_conflict
    BEFORE INSERT OR UPDATE ON appointments
    FOR EACH ROW
    EXECUTE FUNCTION check_patient_appointment_conflict();

CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DO $$
DECLARE
    t text;
BEGIN
    FOR t IN
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_type = 'BASE TABLE'
    LOOP
        EXECUTE format('
            CREATE TRIGGER update_%I_timestamp
            BEFORE UPDATE ON %I
            FOR EACH ROW
            EXECUTE FUNCTION update_timestamp()',
            t, t);
    END LOOP;
END;
$$ LANGUAGE plpgsql;

INSERT INTO patients (name, birthday, sexual, phone_numbers, email, address) VALUES
('正泰', '2015-01-01', '男', '0912345678', '01@example.com', '台北市100'),
('羅利', '2013-05-15', '女', '0923456789', '02@example.com', '台北市200'),
('小明', '2010-12-25', '男', '0934567890', '03@example.com', '台北市300'),
('小美', '2012-06-30', '女', '0945678901', '04@example.com', '台北市400'),
('小華', '2014-11-11', '男', '0956789012', '05@example.com', '台北市500'),
('小芳', '2016-07-20', '女', '0967890123', '06@example.com', '台北市600'),
('小強', '2018-03-05', '男', '0978901234', '07@example.com', '台北市700');


INSERT INTO doctor (name, specialist, sexual, phone_numbers, email, address) VALUES
('老醫師', '內科', '男', '0934567890', 'old@hospital.com', '台北市北投區石牌路二段201號'),
('年輕醫師', '外科', '女', '0945678901', 'young@hospital.com', '台北市北投區石牌路二段201號'),
('王大明', '內科', '男', '0912345678', 'wang@hospital.com', '台北市北投區石牌路二段500號'),
('林美玲', '外科', '女', '0923456789', 'lin@hospital.com', '台北市北投區石牌路二段501號'),
('張志偉', '心臟科', '男', '0934567890', 'chang@hospital.com', '台北市北投區石牌路二段502號'),
('李佳芳', '小兒科', '女', '0945678901', 'lee@hospital.com', '台北市北投區石牌路二段503號'),
('陳建志', '骨科', '男', '0956789012', 'chen@hospital.com', '台北市北投區石牌路二段504號');


INSERT INTO clinic (floor, building, address) VALUES
(1, 'A棟', '台北市信義區忠孝東路五段123號'),
(2, 'A棟', '台北市信義區忠孝東路五段123號'),
(3, 'A棟', '台北市信義區忠孝東路五段123號'),
(1, 'B棟', '台北市信義區忠孝東路五段123號'),
(2, 'B棟', '台北市信義區忠孝東路五段123號'),
(3, 'B棟', '台北市信義區忠孝東路五段123號');


INSERT INTO medicine (name, instructions, unit_price) VALUES
('普拿疼', '飯後服用，每次一顆，一天三次', 5.00),
('維他命C', '飯後服用，每次一顆，一天一次', 3.00),
('氟西汀', '飯後服用，每次一顆，一天一次', 10.00),
('舍曲林', '飯後服用，每次一顆，一天一次', 8.00),
('阿斯匹靈', '每次一顆，一天兩次，飯後服用', 15.75),
('胃腸藥', '每次一包，一天三次，飯前服用', 20.00),
('鈣片', '每次一顆，一天兩次，飯後服用', 8.25);

INSERT INTO doctor_schedule (doctor_id, weekday, start_time, end_time, max_patients) VALUES
(1, 1, '09:00', '17:00', 20),
(1, 3, '09:00', '17:00', 20),
(1, 5, '09:00', '17:00', 20),
(2, 2, '09:00', '17:00', 15),
(2, 4, '09:00', '17:00', 15),
(3, 1, '09:00', '17:00', 18),
(3, 2, '09:00', '17:00', 18),
(3, 4, '09:00', '17:00', 18),
(4, 1, '09:00', '17:00', 25),
(4, 3, '09:00', '17:00', 25),
(4, 5, '09:00', '17:00', 25),
(5, 2, '09:00', '17:00', 16),
(5, 4, '09:00', '17:00', 16);

INSERT INTO doctor_leaves (doctor_id, leave_date, leave_type) VALUES
(1, '2024-12-25', 'vacation'),
(2, '2024-12-26', 'vacation'),
(3, '2024-12-27', 'official'),
(4, '2024-12-28', 'vacation'),
(5, '2024-12-29', 'vacation');

INSERT INTO appointments (doctor_id, patient_id, clinic_id, appointment_date, appointment_time, status) VALUES
(1, 1, 1, '2024-12-16', '09:00:00', 'confirmed'),
(1, 2, 1, '2024-12-16', '10:30:00', 'confirmed'),
(3, 3, 2, '2024-12-16', '09:30:00', 'confirmed'),
(4, 4, 3, '2024-12-16', '14:00:00', 'confirmed'),
(2, 5, 1, '2024-12-17', '09:15:00', 'confirmed'),
(2, 6, 1, '2024-12-17', '10:45:00', 'confirmed'),
(3, 7, 2, '2024-12-17', '11:00:00', 'confirmed'),
(5, 1, 3, '2024-12-17', '14:30:00', 'confirmed');

INSERT INTO admission_record (clinic_id, patient_id, admission_date, discharge_date, reason) VALUES
(3, 1, '2024-12-13', '2024-12-16', '肺炎觀察'),
(4, 2, '2024-12-12', '2024-12-15', '骨折手術後康復'),
(5, 4, '2024-12-16', NULL, '心臟病觀察'),
(6, 5, '2024-12-18', NULL, '腦震盪觀察'),
(3, 6, '2024-12-19', '2024-12-22', '腸胃炎治療');

INSERT INTO prescription (doctor_id, patient_id, prescription_date, cost, dosage) VALUES
(1, 1, '2024-12-13', 150.00, '每日三次'),
(2, 2, '2024-12-12', 200.00, '每日兩次'),
(3, 4, '2024-12-16', 180.00, '每日三次'),
(4, 5, '2024-12-18', 220.00, '每日三次'),
(5, 6, '2024-12-19', 160.00, '每日兩次');


INSERT INTO prescription_medicines (prescription_id, medication_id, dosage, instructions) VALUES
(1, 1, '每次一顆', '飯後服用'),
(1, 2, '每次一顆', '飯後服用'),
(2, 3, '每次一包', '飯前服用'),
(3, 4, '每次一顆', '飯後服用'),
(4, 5, '每次一顆', '飯後服用'),
(4, 1, '每次一顆', '飯後服用'),
(5, 2, '每次一顆', '飯後服用');


INSERT INTO medical_records (appointment_id, patient_id, doctor_id, cases_id, prescription_id) VALUES
(1, 1, 1, 'CASE001', 1),
(2, 2, 2, 'CASE002', 2),
(3, 3, 1, 'CASE003', NULL),
(4, 4, 3, 'CASE004', 3),
(5, 5, 4, 'CASE005', 4),
(6, 6, 5, 'CASE006', 5);


INSERT INTO medical_costs (patient_id, payment_deadline, prescription_id, amount, payment_status, created_date) VALUES
(1, '2024-12-20', 1, 500.00, 'paid', '2024-12-13'),
(2, '2024-12-19', 2, 1500.00, 'partial', '2024-12-12'),
(4, '2024-12-23', 2, 2000.00, 'pending', '2024-12-16'),
(5, '2024-12-25', 2, 1800.00, 'pending', '2024-12-18'),
(6, '2024-12-26', 2, 1200.00, 'paid', '2024-12-19');



INSERT INTO examination (examination_name, examination_date, patient_id, result) VALUES
('體重檢測', '2024-12-13', 1, '體重50公斤'),
('體重檢測', '2024-12-14', 2, '體重47公斤');

INSERT INTO date (date, clinic_id, hospital_stay_date, examination_date, payment_deadline) VALUES
('2024-12-13', 1, '2024-12-13', '2024-12-13', '2024-12-20'),
('2024-12-12', 2, '2024-12-12', '2024-12-12', '2024-12-19'),
('2024-12-16', 3, '2024-12-16', '2024-12-16', '2024-12-23'),
('2024-12-18', 4, '2024-12-18', '2024-12-18', '2024-12-25'),
('2024-12-19', 5, '2024-12-19', '2024-12-19', '2024-12-26');

COMMIT;