import psycopg2

# Connect to database
conn = psycopg2.connect(
    dbname="sima_agp",
    user="postgres",
    password="buhun666",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Get column info for mahasiswa table
cur.execute("""
    SELECT column_name, data_type, is_nullable, column_default
    FROM information_schema.columns
    WHERE table_name = 'mahasiswa'
    ORDER BY ordinal_position;
""")

print("\n" + "="*80)
print("STRUKTUR TABEL MAHASISWA")
print("="*80)
print(f"{'Column Name':<20} {'Data Type':<20} {'Nullable':<10} {'Default'}")
print("-"*80)

for row in cur.fetchall():
    print(f"{row[0]:<20} {row[1]:<20} {row[2]:<10} {row[3] or ''}")

print("="*80)

cur.close()
conn.close()
