CREATE DATABASE VetSurgery;
USE VetSurgery;

CREATE TABLE IF NOT EXISTS Owners 
(
OwnerID INT AUTO_INCREMENT,
FirstName VARCHAR(255),
LastName VARCHAR(255),
Email VARCHAR(255),
Phone VARCHAR(20),
Address VARCHAR(255),
PRIMARY KEY(OwnerID)
);

CREATE TABLE IF NOT EXISTS Pets 
(
PetID INT AUTO_INCREMENT,
OwnerID INT NOT NULL,
PetName VARCHAR(255) NOT NULL,
Species VARCHAR(255) NOT NULL,
Age INT,
PRIMARY KEY(PetID),
FOREIGN KEY(OwnerID) REFERENCES Owners(OwnerID)
);

CREATE TABLE IF NOT EXISTS Appointments
(
AppointmentID INT AUTO_INCREMENT,
Date DATE NOT NULL,
Time TIME NOT NULL,
PetID INT,
Appointment_status ENUM('Available', 'Booked') NOT NULL,
Notes VARCHAR(1000),
PRIMARY KEY(AppointmentID),
FOREIGN KEY(PetID) REFERENCES Pets(PetID)
);

INSERT INTO Owners (FirstName, LastName, Email, Phone, Address) 
VALUES 
('Olivia', 'Smith', 'olivia.smith@example.co.uk', '+44 7700 900001', '123 High Street, London'),
('Liam', 'Jones', 'liam.jones@example.co.uk', '+44 7700 900002', '456 Elm Road, Birmingham'),
('Amelia', 'Taylor', 'amelia.taylor@example.co.uk', '+44 7700 900003', '789 Pine Drive, Glasgow'),
('Ethan', 'Brown', 'ethan.brown@example.co.uk', '+44 7700 900004', '101 Oak Lane, Manchester'),
('Isabella', 'Evans', 'isabella.evans@example.co.uk', '+44 7700 900005', '234 Maple Avenue, Bristol'),
('Mason', 'Wilson', 'mason.wilson@example.co.uk', '+44 7700 900006', '567 Birch Street, Newcastle'),
('Sophia', 'Davies', 'sophia.davies@example.co.uk', '+44 7700 900007', '890 Cedar Place, Liverpool'),
('Logan', 'Roberts', 'logan.roberts@example.co.uk', '+44 7700 900008', '123 Spruce Way, Sheffield'),
('Ava', 'Johnson', 'ava.johnson@example.co.uk', '+44 7700 900009', '456 Redwood Close, Leeds'),
('Jacob', 'Walker', 'jacob.walker@example.co.uk', '+44 7700 900010', '789 Sycamore Road, Edinburgh');


INSERT INTO Pets (OwnerID, PetName, Species, Age) 
VALUES 
(1, 'Bella', 'Dog', 3),
(2, 'Charlie', 'Cat', 2),
(3, 'Luna', 'Rabbit', 1),
(4, 'Max', 'Dog', 4),
(5, 'Lucy', 'Cat', 5),
(6, 'Bailey', 'Dog', 2),
(7, 'Daisy', 'Rabbit', 3),
(8, 'Oliver', 'Cat', 4),
(9, 'Molly', 'Dog', 1),
(10, 'Oscar', 'Rabbit', 2);

ALTER TABLE Appointments
MODIFY COLUMN Appointment_status ENUM('Available', 'Booked', 'Complete') NOT NULL;

-- Monday, April 15, 2024
INSERT INTO Appointments (Date, Time, Appointment_status) VALUES 
('2024-04-15', '10:00:00', 'Available'),
('2024-04-15', '10:30:00', 'Available'),
('2024-04-15', '11:00:00', 'Available'),
('2024-04-15', '11:30:00', 'Available'),
('2024-04-15', '12:00:00', 'Available'),
('2024-04-15', '14:00:00', 'Available'),
('2024-04-15', '14:30:00', 'Available'),
('2024-04-15', '15:00:00', 'Available'),
('2024-04-15', '15:30:00', 'Available');

-- Tuesday, April 16, 2024
INSERT INTO Appointments (Date, Time, Appointment_status) VALUES 
('2024-04-16', '10:00:00', 'Available'),
('2024-04-16', '10:30:00', 'Available'),
('2024-04-16', '11:00:00', 'Available'),
('2024-04-16', '11:30:00', 'Available'),
('2024-04-16', '12:00:00', 'Available'),
('2024-04-16', '14:00:00', 'Available'),
('2024-04-16', '14:30:00', 'Available'),
('2024-04-16', '15:00:00', 'Available'),
('2024-04-16', '15:30:00', 'Available');

-- Wednesday, April 17, 2024
INSERT INTO Appointments (Date, Time, Appointment_status) VALUES 
('2024-04-17', '10:00:00', 'Available'),
('2024-04-17', '10:30:00', 'Available'),
('2024-04-17', '11:00:00', 'Available'),
('2024-04-17', '11:30:00', 'Available'),
('2024-04-17', '12:00:00', 'Available'),
('2024-04-17', '14:00:00', 'Available'),
('2024-04-17', '14:30:00', 'Available'),
('2024-04-17', '15:00:00', 'Available'),
('2024-04-17', '15:30:00', 'Available');

-- Thursday, April 18, 2024
INSERT INTO Appointments (Date, Time, Appointment_status) VALUES 
('2024-04-18', '10:00:00', 'Available'),
('2024-04-18', '10:30:00', 'Available'),
('2024-04-18', '11:00:00', 'Available'),
('2024-04-18', '11:30:00', 'Available'),
('2024-04-18', '12:00:00', 'Available'),
('2024-04-18', '14:00:00', 'Available'),
('2024-04-18', '14:30:00', 'Available'),
('2024-04-18', '15:00:00', 'Available'),
('2024-04-18', '15:30:00', 'Available');

-- Friday, April 19, 2024
INSERT INTO Appointments (Date, Time, Appointment_status) VALUES 
('2024-04-19', '10:00:00', 'Available'),
('2024-04-19', '10:30:00', 'Available'),
('2024-04-19', '11:00:00', 'Available'),
('2024-04-19', '11:30:00', 'Available'),
('2024-04-19', '12:00:00', 'Available'),
('2024-04-19', '14:00:00', 'Available'),
('2024-04-19', '14:30:00', 'Available'),
('2024-04-19', '15:00:00', 'Available'),
('2024-04-19', '15:30:00', 'Available');

-- Monday, April 22, 2024
INSERT INTO Appointments (Date, Time, Appointment_status) VALUES 
('2024-04-22', '10:00:00', 'Available'),
('2024-04-22', '10:30:00', 'Available'),
('2024-04-22', '11:00:00', 'Available'),
('2024-04-22', '11:30:00', 'Available'),
('2024-04-22', '12:00:00', 'Available'),
('2024-04-22', '14:00:00', 'Available'),
('2024-04-22', '14:30:00', 'Available'),
('2024-04-22', '15:00:00', 'Available'),
('2024-04-22', '15:30:00', 'Available');

-- Tuesday, April 23, 2024
INSERT INTO Appointments (Date, Time, Appointment_status) VALUES 
('2024-04-23', '10:00:00', 'Available'),
('2024-04-23', '10:30:00', 'Available'),
('2024-04-23', '11:00:00', 'Available'),
('2024-04-23', '11:30:00', 'Available'),
('2024-04-23', '12:00:00', 'Available'),
('2024-04-23', '14:00:00', 'Available'),
('2024-04-23', '14:30:00', 'Available'),
('2024-04-23', '15:00:00', 'Available'),
('2024-04-23', '15:30:00', 'Available');

SET SQL_SAFE_UPDATES = 0;

UPDATE Appointments SET Appointment_status = 'Booked', PetID = 1 WHERE Date = '2024-04-18' AND Time = '11:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 4 WHERE Date = '2024-04-19' AND Time = '10:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 4 WHERE Date = '2024-04-17' AND Time = '10:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 9 WHERE Date = '2024-04-23' AND Time = '11:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 7 WHERE Date = '2024-04-18' AND Time = '14:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 3 WHERE Date = '2024-04-18' AND Time = '11:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 7 WHERE Date = '2024-04-17' AND Time = '14:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 2 WHERE Date = '2024-04-15' AND Time = '10:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 1 WHERE Date = '2024-04-18' AND Time = '14:00:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 9 WHERE Date = '2024-04-18' AND Time = '15:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 8 WHERE Date = '2024-04-15' AND Time = '15:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 4 WHERE Date = '2024-04-16' AND Time = '15:00:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 1 WHERE Date = '2024-04-19' AND Time = '15:00:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 3 WHERE Date = '2024-04-22' AND Time = '15:00:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 8 WHERE Date = '2024-04-17' AND Time = '11:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 2 WHERE Date = '2024-04-18' AND Time = '11:00:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 10 WHERE Date = '2024-04-17' AND Time = '15:00:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 9 WHERE Date = '2024-04-15' AND Time = '15:00:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 1 WHERE Date = '2024-04-16' AND Time = '10:30:00';
UPDATE Appointments SET Appointment_status = 'Booked', PetID = 5 WHERE Date = '2024-04-17' AND Time = '11:00:00';

-- Update appointment for PetID 4 on 2024-04-16 at 15:00 to 'Complete'
UPDATE Appointments 
SET Appointment_status = 'Complete', Notes = 'Completed annual vaccination.' 
WHERE Date = '2024-04-16' AND Time = '15:00:00';

-- Update appointment for PetID 1 on 2024-04-19 at 15:00 to 'Complete'
UPDATE Appointments 
SET Appointment_status = 'Complete', Notes = 'Allergy consultation and treatment.' 
WHERE Date = '2024-04-19' AND Time = '15:00:00';

-- Update appointment for PetID 9 on 2024-04-15 at 15:00 to 'Complete'
UPDATE Appointments 
SET Appointment_status = 'Complete', Notes = 'Nail trimming and ear cleaning.' 
WHERE Date = '2024-04-15' AND Time = '15:00:00';

-- Update appointment for PetID 8 on 2024-04-17 at 11:30 to 'Complete'
UPDATE Appointments 
SET Appointment_status = 'Complete', Notes = 'General wellness check-up completed.' 
WHERE Date = '2024-04-17' AND Time = '11:30:00';

-- Update appointment for PetID 10 on 2024-04-17 at 15:00 to 'Complete'
UPDATE Appointments 
SET Appointment_status = 'Complete', Notes = 'Emergency treatment for ingestion of foreign object. Follow-up required.' 
WHERE Date = '2024-04-17' AND Time = '15:00:00';

-- Update appointment for PetID 7 on 2024-04-17 at 14:30 to 'Complete'
UPDATE Appointments 
SET Appointment_status = 'Complete', Notes = 'Behavioral consultation for anxiety. Medication prescribed.' 
WHERE Date = '2024-04-17' AND Time = '14:30:00';
