-- Add missing fields to users table for Django compatibility
ALTER TABLE users ADD COLUMN IF NOT EXISTS last_login TIMESTAMP NULL;
ALTER TABLE users ADD COLUMN IF NOT EXISTS is_superuser BOOLEAN NOT NULL DEFAULT FALSE;
ALTER TABLE users ADD COLUMN IF NOT EXISTS is_staff BOOLEAN NOT NULL DEFAULT FALSE;
ALTER TABLE users ADD COLUMN IF NOT EXISTS is_active BOOLEAN NOT NULL DEFAULT TRUE;
ALTER TABLE users ADD COLUMN IF NOT EXISTS date_joined TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP;

-- Update admin user to have superuser privileges
UPDATE users SET is_superuser = TRUE, is_staff = TRUE WHERE role = 'admin';

-- Create indexes
CREATE INDEX IF NOT EXISTS users_is_active_idx ON users(is_active);
CREATE INDEX IF NOT EXISTS users_is_staff_idx ON users(is_staff);
