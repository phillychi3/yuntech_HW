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

