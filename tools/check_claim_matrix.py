#!/usr/bin/env python3
import csv,sys
from pathlib import Path
p=Path(sys.argv[1]) if len(sys.argv)>1 else Path("examples/claims.csv")
rows=list(csv.DictReader(p.open(encoding="utf-8"))); errors=[]
for i,r in enumerate(rows,2):
 if not r.get("claim","").strip(): errors.append(f"row {i}: empty claim")
 if not r.get("evidence_type","").strip(): errors.append(f"row {i}: missing evidence_type")
 if r.get("evidence_type","").lower() in {"primary fact","vendor claim"} and not r.get("source_url","").strip(): errors.append(f"row {i}: sourced claim lacks source_url")
print(f"claims={len(rows)} errors={len(errors)}")
for e in errors: print("ERROR",e)
sys.exit(bool(errors))
