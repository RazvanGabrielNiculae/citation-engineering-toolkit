import subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; TOOL=ROOT/'tools'/'check_claim_matrix.py'
class CLI(unittest.TestCase):
 def run_case(self,rel): return subprocess.run([sys.executable,str(TOOL),str(ROOT/rel)],capture_output=True,text=True)
 def test_valid(self): self.assertEqual(self.run_case('examples/claims.csv').returncode,0)
 def test_primary_fact_requires_source(self): self.assertNotEqual(self.run_case('tests/fixtures/primary-without-source.csv').returncode,0)
if __name__=='__main__': unittest.main()
