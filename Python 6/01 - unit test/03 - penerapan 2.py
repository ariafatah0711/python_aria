import unittest

def koneksi_ke_db():
    print("[terhubung ke db]")

def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))

class User:
    username = ""
    aktif = False
    
    def __init__(self, db, username):
        self.username = username
        pass
    
    def set_aktif(self):
        self.aktif = True

class TestUser(unittest.TestCase):
    # Test Fixture
    def setUp(self):
        self.db = koneksi_ke_db()
        self.dicoding = User(self.db, "dicoding")
 
    def tearDown(self):
        putus_koneksi_db(self.db)
 
    # Test Case 1
    def test_user_default_not_active(self):
        self.assertFalse(self.dicoding.aktif)  # tidak aktif secara default
        
    # Test Case 2
    def test_user_is_active(self):
        self.dicoding.set_aktif()  # aktifkan user baru
        self.assertTrue(self.dicoding.aktif)

if __name__ == "__main__":
    # Test Runner
    unittest.main()
    