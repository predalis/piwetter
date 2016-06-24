import MySQLdb
import geheim

# creates a new database in  MySQL and returns the new db
def myConnectAndCreate(dbName): 
	db = MySQLdb.connect(geheim.host, geheim.username, geheim.password, dbName)
	cursor = db.cursor()
	createAdb(cursor)
	return db
	

####### CAUTION THIS DESTROYS ANY EXISTING DATA IN YOUR CURRENT DATABASE JUST FOR RESET OR INSTALL
def createAdb(cursor):
	cursor.execute('DROP DATABASE '+geheim.dbName)
	sql = 'CREATE DATABASE IF NOT EXISTS ' + geheim.dbName + """ DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"""
	print (sql)
	cursor.execute(sql)

def getConnected():
	db = MySQLdb.connect(geheim.host, geheim.username, geheim.password, geheim.dbName)
	return db
#myDB = myConnectAndCreate('')

def createNewTable(cursor):
	#cursor.execute("DROP TABLE IF EXISTS LOCATION")
	sql ="""CREATE TABLE IF NOT EXISTS LOCATION(
	locID INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	locName VARCHAR(30),
	country VARCHAR(30),
	province VARCHAR(30),
	Latitude VARCHAR(30),
	Longitude VARCHAR(30),
	elevation VARCHAR(30),
	street VARCHAR(30),
	postalCode VARCHAR(30),
	city VARCHAR(30),
	INDEX (locName),
	INDEX (country))"""
	cursor.execute(sql)
	
	#cursor.execute("DROP TABLE IF EXISTS DATETIME")
	sql = """CREATE TABLE IF NOT EXISTS DATETIME(
	dateID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	date DATE, 
	time TIME)"""
	cursor.execute(sql)

	#cursor.execute("DROP TABLE IF EXISTS WETTERDATEN")
	sql = """CREATE TABLE IF NOT EXISTS WETTERDATEN(
	weID INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	rainIntensity INT (6), 
	lightIntensity INT (6), 
	barometer DOUBLE, 
	temperature1 DOUBLE, 
	temperature2 DOUBLE, 
	altitude DOUBLE,
	time TIME NOT NULL,
	windDirection DOUBLE, 
	humidity DOUBLE,
	dateID INT(6) UNSIGNED,
	locID INT(6) UNSIGNED,
	FOREIGN KEY (dateID) REFERENCES DATETIME(dateID),
	FOREIGN KEY (locID) REFERENCES LOCATION(locID))"""
	cursor.execute(sql)
	
	#cursor.execute("DROP TABLE IF EXISTS USER")
	sql="""CREATE TABLE IF NOT EXISTS USER(
	user_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	mail VARCHAR(30) NOT NULL UNIQUE,
	city VARCHAR(30),
	country VARCHAR(30),
	firstname VARCHAR(30),
	lastname VARCHAR (30),
	pwd_hash VARCHAR(120) NOT NULL,
	INDEX (mail))"""
	cursor.execute(sql)


#def createDateEntry():
#db = myConnectAndCreate(geheim.dbName)
#db.close()

myDB = getConnected()
cursor = myDB.cursor()

createNewTable(cursor)
myDB.close()


