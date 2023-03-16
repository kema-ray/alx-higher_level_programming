--  script that creates the database hbtn_0d_usa and the table cities

CREATE DATAASE IF NOT EXISTS 'hbtn_0d_usa';
CREATE TABLE IF NOT ES=XISTS 'hbtn_0d_usa'.'cities'; (
		PRIMARY KEY('id'),
		'id'	INT	NOT NULL AUTO_INCREMENT,
		'state_id'	INT	NOT NULL,
		'name'	VARCHER(256)	NOT NULL,
		FOREIGN KEY('state_id')
		REFERENCE 'hbtn_0d_usa'.'states'('id')
);
