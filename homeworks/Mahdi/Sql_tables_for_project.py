# DATABASE: hospital_management


# 1. TABLE: patients

# patient_id       INT              PRIMARY KEY, AUTO_INCREMENT
# name             VARCHAR(100)     NOT NULL
# age              INT
# gender           ENUM('Male', 'Female')  Enumeration
# phone_number     VARCHAR(20)
# address          VARCHAR(255)


# 2. TABLE: doctors

# doctor_id        INT              PRIMARY KEY, AUTO_INCREMENT
# name             VARCHAR(100)     NOT NULL
# specialization   VARCHAR(100)
# phone_number     VARCHAR(20)


# 3. TABLE: doctor_schedules

# schedule_id      INT              PRIMARY KEY, AUTO_INCREMENT
# doctor_id        INT              FOREIGN KEY REFERENCES doctors(doctor_id)
# working_day      VARCHAR(15)
# start_time       TIME
# end_time         TIME


# 4. TABLE: appointments

# appointment_id   INT              PRIMARY KEY, AUTO_INCREMENT
# patient_id       INT              FOREIGN KEY REFERENCES patients(patient_id)
# doctor_id        INT              FOREIGN KEY REFERENCES doctors(doctor_id)
# appointment_date DATE             NOT NULL
# appointment_time TIME             NOT NULL
# status           ENUM('Booked', 'Completed', 'Cancelled')


# 5. TABLE: medical_records

# record_id        INT              PRIMARY KEY, AUTO_INCREMENT
# patient_id       INT              FOREIGN KEY REFERENCES patients(patient_id)
# doctor_id        INT              FOREIGN KEY REFERENCES doctors(doctor_id)
# diagnosis        TEXT
# treatment_notes  TEXT
# record_date      DATE


# 6. TABLE: bills

# bill_id          INT              PRIMARY KEY, AUTO_INCREMENT
# patient_id       INT              FOREIGN KEY REFERENCES patients(patient_id)
# consultation_fee DECIMAL(10,2)    DEFAULT 0
# service_charge   DECIMAL(10,2)    DEFAULT 0
# total_amount     DECIMAL(10,2)    GENERATED
# payment_status   ENUM('Paid', 'Unpaid', 'Partial')
# bill_date        DATE


# 7. TABLE: medicines

# medicine_id      INT              PRIMARY KEY, AUTO_INCREMENT
# medicine_name    VARCHAR(100)     NOT NULL
# category         VARCHAR(100)
# quantity         INT              DEFAULT 0
# price            DECIMAL(10,2)    NOT NULL
# expiration_date  DATE


# 8. TABLE: medicine_sales

# sale_id          INT              PRIMARY KEY, AUTO_INCREMENT
# patient_id       INT              FOREIGN KEY REFERENCES patients(patient_id)
# sale_date        DATETIME         DEFAULT CURRENT_TIMESTAMP
# total_amount     DECIMAL(10,2)    DEFAULT 0


# 9. TABLE: medicine_sale_items

# item_id          INT              PRIMARY KEY, AUTO_INCREMENT
# sale_id          INT              FOREIGN KEY REFERENCES medicine_sales(sale_id)
# medicine_id      INT              FOREIGN KEY REFERENCES medicines(medicine_id)
# quantity         INT              NOT NULL
# unit_price       DECIMAL(10,2)    NOT NULL


# wamp zamp : php , aphachi , mysqli posgress 