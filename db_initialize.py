import sqlite3
con = sqlite3.connect('database.db')
con.execute("DROP TABLE IF EXISTS Users;")
con.execute("CREATE TABLE Users (username VARCHAR(200) PRIMARY KEY, password VARCHAR(200), admin CHAR(1), salt VARCHAR(200), publickey VARCHAR(5000), privatekey VARCHAR(5000), mute CHAR(1))")
con.execute("INSERT INTO Users (username, password, admin, salt, publickey, privatekey, mute) VALUES ('WentaoGao', '3c7a71e1b859a94a35be988b0e7a633c', '1', 'xyz', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArnpU4Z8R4UqZ9o9lbrH1\nCRzJ866A+3C21CT279lFe1eZaeRcWIFgpudONz8EomxqFarF98Vov9vzKd9yTY4H\nhtADJEo4TPJaUBX0rqBUQnnTxsKHuyRISA35WimRd51LIO98JTokOxeBopF8JCfG\nV158jiqFEnKTskqBMTgFFU55YSr38VgQnv2z9ApSRlhdcJGdlhMGYNQ6/EJLyi7i\nAE5LeIAgRd50M315udoYnDiGLaK5Is7TI1XqSDVow9hzHXrWDaMfWuwhx+Ls3RW7\ndyfUfanvO8ztEFbV58fqUP3fMDBj/CUDOU+O6ntGi8NO0A6YO1UTuDRHmcz0C5sZ\nDwIDAQAB\n-----END PUBLIC KEY-----', '-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEArnpU4Z8R4UqZ9o9lbrH1CRzJ866A+3C21CT279lFe1eZaeRc\nWIFgpudONz8EomxqFarF98Vov9vzKd9yTY4HhtADJEo4TPJaUBX0rqBUQnnTxsKH\nuyRISA35WimRd51LIO98JTokOxeBopF8JCfGV158jiqFEnKTskqBMTgFFU55YSr3\n8VgQnv2z9ApSRlhdcJGdlhMGYNQ6/EJLyi7iAE5LeIAgRd50M315udoYnDiGLaK5\nIs7TI1XqSDVow9hzHXrWDaMfWuwhx+Ls3RW7dyfUfanvO8ztEFbV58fqUP3fMDBj\n/CUDOU+O6ntGi8NO0A6YO1UTuDRHmcz0C5sZDwIDAQABAoIBAADBIHRcnovOMiM5\n4Uyg/vO798P5EOK0XgaKEGB4gw9/XfdYvu0SX7yCm/0ibg27u6uxLedZ/Nxkkyt7\nreIkj+crSa4OdMOpvcwoyGkF0S3ZmmaUPXreCLobkEslAd4LO+XTdWS5i+6fvkuV\nSPzTsxEC6L4YOKMknZ2aXkQrDCPpmnpsJJOUgUZFk0Q2esCY3DuCdy7148RECcVU\nUZJrHJBowjT68jNFriDEzlci/9qrx0umUv1Z/7x2ppBf4dwPTAe0Pyk5SSJznc+3\nVRcpDhl4eJzdCSEovDar6lVp0bRdyXnS7dk9YQFTDspwz9Dr7lpFpQ/7m8oTyvJH\ne2mJW7ECgYEAvQHfq4obVZsd8T3Q6lireq/ms2NLM+pN4DOyCN2YFjWt+EYz6eTF\n075783q5f5TcbFg7lk7y7DRy8+44A9xzKPA8p/g5rbY4BB2AmjNbWSQhrdBfqxJ9\nUQusSFZxGKyuEYSIIebprrem9c7rdAFYPL8yljJpvlY9cfyql/QwpP8CgYEA7FIV\nyWLbeQ5eee/SNNDYQOLovs99DesXl42MpYOvt1r5Bsq/YubKVHcNl4YKSpuz0syP\nyN5ZVqFTFRr6vk4Im5L9QWIhayKYO8fEGPDYtxKEGnMQ4AlkStrID2TQGjMmif6G\n2zYPtuLeyio5nVvwjz9T69iNV6dsaJiPrn83O/ECgYAvtaxfIbJ6rnglcCQvM4i9\npG9IsvTFuwxDXuk+4ajFWnF6rUXncY8aPwgM0trGQK5PTwpji7Q4OZkWx/gtyVTs\nbY/yGm980PVc3JGc2v/hBYTW2jV7+mPVtGudquxLfTNHSrwOSrqMFuG3RK8cjkZW\ntzCuxzT4Dc7e2he52bL5wwKBgQCcM21/HT6f92VvB5tTma82xES+ynqIFpoTbFZI\nmJAui40KdjymbJHT3pU3UDvBMMVdUiS/ymgWoK8/xgNygjWiTzfiXbBlFgq1iMcP\nDTLRXwW+TcwbqVmHOLD/q8z5ZFHW6EvO3R7p7W8BBYPrhPeuV1drDknuZBV91Ukz\nN5cUoQKBgHhf9l0TkHkSqJ4nG3/UVNLRzauzv+L7mf6y0+xs7kXWv4cqM4IIOPx9\nCv9+KHT20wvo6BWAAksYgwLxJCt9pL6zoCmU1XIwOK6y0BHN+gTTO1yKO76kfTFV\nfsRivuaINEB2fvTfYHEqh3HUrmQp6IK3mXJlaohP4zJBpSJE1OM5\n-----END RSA PRIVATE KEY-----','0')")
con.execute("INSERT INTO Users (username, password, admin, salt, publickey, privatekey, mute) VALUES ('LangyiChen', '3c7a71e1b859a94a35be988b0e7a633c', '1', 'xyz', '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqVEqU5Z0084xeXyqUgGo\nLMIebbb2FgJF9JiOsgAl5XFMJisL5GlT+c5Pc98cCpyjwyHmSh5n8nKkl5MLDpX1\npphaJzCIAkkLnDgkgaxpdvq6T6IlO0f8AMzIGJvpbpJnDZkEXoOgquz02KGK3/8i\nXTmfzzRLBLaHsTYUJJ37ZlRV7+gx/LCcXlp3xnxDpiMKeR8vE4ZEVWXk8LJwaDJV\nBlveMuy7QJaskxzHeRyJUvuA8xvm0h+PMAzPYlWlTOFNVYUcauGl4FcO03424WKc\nq0J9xI6FnTfQsjjdMaPItbl9beR/ZK5Qi8JGXbs7TcjG0LzxxKDJfQcR8nvkEC0W\nBQIDAQAB\n-----END PUBLIC KEY-----', '-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAqVEqU5Z0084xeXyqUgGoLMIebbb2FgJF9JiOsgAl5XFMJisL\n5GlT+c5Pc98cCpyjwyHmSh5n8nKkl5MLDpX1pphaJzCIAkkLnDgkgaxpdvq6T6Il\nO0f8AMzIGJvpbpJnDZkEXoOgquz02KGK3/8iXTmfzzRLBLaHsTYUJJ37ZlRV7+gx\n/LCcXlp3xnxDpiMKeR8vE4ZEVWXk8LJwaDJVBlveMuy7QJaskxzHeRyJUvuA8xvm\n0h+PMAzPYlWlTOFNVYUcauGl4FcO03424WKcq0J9xI6FnTfQsjjdMaPItbl9beR/\nZK5Qi8JGXbs7TcjG0LzxxKDJfQcR8nvkEC0WBQIDAQABAoIBAAnuMn0SDTqR9Jlj\nPCsQoVA0t2uoaDD8w6UXoIDknNRi63wumKU2H0B+vu61FnQx4THz5kmRFHgmDKy+\nKU8a8PwrIdh8EnIN3jI0ocGAPvRFOtGqWSQrseZLHG5DELMVP5mO0LCJaE42FRsy\niE5gbJ/KniqdLswxN26nlRFbua+z6KTEbdvuKxbcMqLyjNj5uiPZ4cimDFzEuXNv\n3AScSFbUmhQ7UW5FcNgFW4LtGBDlj1Fyjs1hVJHHpojLTiHcvAprITKKK2g9HtGS\nqqo1I1S2dp9L8hfEsKJ+ih7+Wpv18Bt0MBMy909GBFPOxTrbGbOK2dPdQgxyQ4Is\nqhuOigECgYEAzSAGzKAgqsnxDmk+c7S+VGf/p9X0rZXERyf0Q344NfkpPTOX6t4j\nhrWZ2NQ4g/gNRlz7RIh8MECzmQiAK8ICR45oJfj/NtinDMGWw5l7+TdXhoj7fY6N\n73ErJvs9Db3to9rMJoJJg+pIT2XJuU+UE6I3+crhrIdI5A66gZj51gECgYEA00+V\nj8NLIFDGfNGhy4MhItr9wJUcb5UVcEjUlwMqbW8jrs/I20SaqxZ1hsbRNNwDRv2R\nbH6LWQAEfaKOkMq7/x/D5FWnfqu9/ZhB2J+lIhsRfTfGBbqG4x+TG22ZW31+9Cwo\nx3vf3KYu8qryBX1PSWzr8YR9GZ3CC4+GsJdb6AUCgYB0U4tHlC+ya19nGswt9fxS\nBcB4P9/IaTysVb4yYGwkP67hZFbs/RkMlgQvcPqz7IIquyRL01MKUkcHrEhziEye\no+XwUur5AZiKpWaIeoxR4s6iHyDwLV3UwksEikovdtxDphtMY2qpgr2LOWBS1QxW\nrhIseJ/OpdHyc1/Vixl0AQKBgD8BitHL5FmlXBmZlAmPdtDixSioDUuEA1lwjdrd\nOchZjCUylWwzv35l+vMN0xFUzLFdKABWlwwZgj1HvASWPonqmck6dO/DG6pCvNdv\neph5w7Q3bhcFL/UG1CEog8KQ38rEZABfAjfTYUpACFv0qjB1hsCDxZ1euZ4i1IFR\nEDlVAoGAHE14n7F3NtPK4ZDfK55kd8hrVT2LRuD/4y42nqdpkGKNWKV4WDax+P3C\nz5gCi2Lrs81/wjDGel+hVWtJTBjw4/ug6Z6l9K7wrzSYW155QlT0UxLIeRWy/kx5\n3nnhsGs67/tjJp9F5RelTGTqbYQGzWjLyowI2KQhGkUOc9nggtU=\n-----END RSA PRIVATE KEY-----','1')")
con.commit()

con.execute("DROP TABLE IF EXISTS Friends;")
con.execute("CREATE TABLE Friends (friend_r VARCHAR(200), friend_a VARCHAR(200))")
con.execute("INSERT INTO Friends (friend_r, friend_a) VALUES ('WentaoGao', 'LangyiChen')")
con.execute("INSERT INTO Friends (friend_r, friend_a) VALUES ('LangyiChen', 'WentaoGao')")
con.commit()

con.execute("DROP TABLE IF EXISTS Messages;")
con.execute("CREATE TABLE Messages (sender VARCHAR(200), receiver VARCHAR(200), message VARCHAR(1000), signature VARCHAR(5000))")
con.commit()
