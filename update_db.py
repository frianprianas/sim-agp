import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname='sima_agp',
    user='postgres',
    password='buhun666',
    host='localhost',
    port='5432'
)

cur = conn.cursor()

print('=' * 50)
print('UPDATING POSTGRESQL DATABASE')
print('=' * 50)

# SQL statements
sqls = [
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS last_login TIMESTAMP NULL",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS is_superuser BOOLEAN NOT NULL DEFAULT FALSE",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS is_staff BOOLEAN NOT NULL DEFAULT FALSE",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS is_active BOOLEAN NOT NULL DEFAULT TRUE",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS date_joined TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP",
    "UPDATE users SET is_superuser = TRUE, is_staff = TRUE, is_active = TRUE WHERE role = 'admin'",
    "UPDATE users SET is_active = TRUE WHERE is_active IS FALSE OR is_active IS NULL",
    "CREATE INDEX IF NOT EXISTS users_is_active_idx ON users(is_active)",
    "CREATE INDEX IF NOT EXISTS users_is_staff_idx ON users(is_staff)",
]

for sql in sqls:
    try:
        cur.execute(sql)
        print(f'✓ {sql[:60]}...')
    except Exception as e:
        print(f'✗ Error: {e}')

conn.commit()
cur.close()
conn.close()

print('\n' + '=' * 50)
print('✅ DATABASE UPDATE COMPLETE!')
print('=' * 50)
