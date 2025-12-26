-- PostgreSQL Database: sima_agp
-- Converted from MySQL
-- Generation Time: Dec 25, 2025

-- Drop tables if exist
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS mahasiswa CASCADE;
DROP TABLE IF EXISTS prodi CASCADE;
DROP TABLE IF EXISTS migrations CASCADE;

-- --------------------------------------------------------
-- Table structure for table prodi
-- --------------------------------------------------------

CREATE TABLE prodi (
    id_prodi BIGSERIAL PRIMARY KEY,
    prodi VARCHAR(100) NOT NULL,
    jenjang VARCHAR(2) NOT NULL CHECK (jenjang IN ('D3', 'S1')),
    created_at TIMESTAMP NULL DEFAULT NULL,
    updated_at TIMESTAMP NULL DEFAULT NULL
);

-- Dumping data for table prodi
INSERT INTO prodi (id_prodi, prodi, jenjang, created_at, updated_at) VALUES
(1, 'Teknik Informatika', 'S1', '2025-12-24 13:34:52', '2025-12-24 13:34:52'),
(2, 'Sistem Informasi', 'S1', '2025-12-24 13:34:52', '2025-12-24 13:34:52'),
(3, 'Teknik Komputer', 'D3', '2025-12-24 13:34:52', '2025-12-24 13:34:52'),
(4, 'Manajemen Informatika', 'D3', '2025-12-24 13:34:52', '2025-12-24 13:34:52'),
(5, 'Teknik Pertambangan', 'D3', '2025-12-24 13:43:14', '2025-12-24 13:43:14'),
(6, 'Teknik Geologi', 'D3', '2025-12-24 13:54:29', '2025-12-24 13:54:29');

-- Set sequence for prodi
SELECT setval('prodi_id_prodi_seq', (SELECT MAX(id_prodi) FROM prodi));

-- --------------------------------------------------------
-- Table structure for table mahasiswa
-- --------------------------------------------------------

CREATE TABLE mahasiswa (
    nim VARCHAR(20) PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    alamat TEXT NOT NULL,
    jenis_kelamin VARCHAR(1) NOT NULL CHECK (jenis_kelamin IN ('L', 'P')),
    tempat VARCHAR(50) NOT NULL,
    tgl_lahir DATE NOT NULL,
    id_prodi BIGINT NOT NULL,
    tahun_masuk INTEGER NOT NULL,
    email VARCHAR(255) DEFAULT NULL,
    no_telepon VARCHAR(20) DEFAULT NULL,
    created_at TIMESTAMP NULL DEFAULT NULL,
    updated_at TIMESTAMP NULL DEFAULT NULL,
    CONSTRAINT mahasiswa_id_prodi_foreign FOREIGN KEY (id_prodi) 
        REFERENCES prodi(id_prodi) ON DELETE CASCADE
);

-- Create index for foreign key
CREATE INDEX mahasiswa_id_prodi_idx ON mahasiswa(id_prodi);

-- Dumping data for table mahasiswa
INSERT INTO mahasiswa (nim, nama, alamat, jenis_kelamin, tempat, tgl_lahir, id_prodi, tahun_masuk, email, no_telepon, created_at, updated_at) VALUES
('09888', 'Firli Batubara Ankara', 'Jl Kancana 2 Bandung', 'L', 'Bandung', '2006-05-18', 4, 2025, NULL, NULL, '2025-12-24 13:41:02', '2025-12-24 13:42:46'),
('89000', 'Neni Irwati', 'Jl Sancang 65 Garut', 'P', 'Garut', '2006-12-12', 6, 2025, 'neninkmt@gmail.com', '082121635987', '2025-12-24 13:59:13', '2025-12-24 14:23:06');

-- --------------------------------------------------------
-- Table structure for table users
-- --------------------------------------------------------

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) DEFAULT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'mahasiswa' CHECK (role IN ('admin', 'mahasiswa')),
    nim VARCHAR(20) DEFAULT NULL UNIQUE,
    remember_token VARCHAR(100) DEFAULT NULL,
    created_at TIMESTAMP NULL DEFAULT NULL,
    updated_at TIMESTAMP NULL DEFAULT NULL,
    last_login TIMESTAMP NULL DEFAULT NULL,
    is_superuser BOOLEAN NOT NULL DEFAULT FALSE,
    is_staff BOOLEAN NOT NULL DEFAULT FALSE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    date_joined TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT users_nim_foreign FOREIGN KEY (nim) 
        REFERENCES mahasiswa(nim) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX users_nim_idx ON users(nim);
CREATE INDEX users_is_active_idx ON users(is_active);
CREATE INDEX users_is_staff_idx ON users(is_staff);

-- Dumping data for table users
INSERT INTO users (id, name, username, email, password, role, nim, is_superuser, is_staff, is_active, created_at, updated_at) VALUES
(1, 'Administrator', 'admin', 'admin@sima-agp.ac.id', '$2y$10$zH.k.XsDJR.RNWytmobCquq6tlQD2SDLMCtFzMtt1xMda/bWMVkNW', 'admin', NULL, TRUE, TRUE, TRUE, '2025-12-24 14:12:08', '2025-12-24 14:12:08'),
(2, 'Neni Irwati', '89000', 'neninkmt@gmail.com', '$2y$10$lTZkW3vQbRhltsLtU/vB7Oeo0CAU7DDYE.70guWBJoQGenHEz5qXG', 'mahasiswa', '89000', FALSE, FALSE, TRUE, '2025-12-24 14:21:10', '2025-12-24 14:23:41');

-- Set sequence for users
SELECT setval('users_id_seq', (SELECT MAX(id) FROM users));

-- --------------------------------------------------------
-- Table structure for table migrations
-- --------------------------------------------------------

CREATE TABLE migrations (
    id SERIAL PRIMARY KEY,
    migration VARCHAR(255) NOT NULL,
    batch INTEGER NOT NULL
);

-- Dumping data for table migrations
INSERT INTO migrations (id, migration, batch) VALUES
(1, '2024_01_01_000001_create_prodi_table', 1),
(2, '2024_01_01_000002_create_mahasiswa_table', 1),
(3, '2024_01_02_000001_create_users_table', 2),
(4, '2024_01_02_000002_add_auth_fields_to_mahasiswa_table', 2);

-- Set sequence for migrations
SELECT setval('migrations_id_seq', (SELECT MAX(id) FROM migrations));
