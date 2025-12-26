@echo off
echo ========================================
echo Update PostgreSQL Database for Django
echo ========================================
echo.
echo Menambahkan kolom Django ke tabel users...
echo.

psql -U postgres -d sima_agp -f database\update_users_table.sql

echo.
echo ========================================
echo Update selesai!
echo ========================================
pause
