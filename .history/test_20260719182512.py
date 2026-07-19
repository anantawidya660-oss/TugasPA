# test_env.py
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

print("=" * 50)
print("📋 CEK .ENV")
print("=" * 50)
print(f"TIDB_HOST      : {os.getenv('TIDB_HOST')}")
print(f"TIDB_USER      : {os.getenv('TIDB_USER')}")
print(f"TIDB_DATABASE  : {os.getenv('TIDB_DATABASE')}")
print(f"TIDB_PASSWORD  : {os.getenv('TIDB_PASSWORD')[:5]}... (hidden)")
print("=" * 50)