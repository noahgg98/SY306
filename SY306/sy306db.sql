
CREATE TABLE Users (
    Username VARCHAR(255) NOT NULL,
    NameReal VARCHAR(255) NOT NULL,
    Pass VARCHAR(255) NOT NULL,
    Permission VARCHAR(255) NOT NULL DEFAULT 'Regular',
    PRIMARY KEY (Username)
); 

CREATE TABLE Messages (
    MesgID int NOT NULL AUTO_INCREMENT,
    Mesg VARCHAR(255) NOT NULL,
    Username VARCHAR(255) NOT NULL,
    TmStamp DateTime NOT NULL DEFAULT NOW(),
    PRIMARY KEY (MesgID),
    FOREIGN KEY (Username) REFERENCES Users(Username)
); 


INSERT INTO Users (Username, NameReal, Pass, Permission) VALUES ("Admin", "Admin", SHA2("Admin",256), "admin");
INSERT INTO Users (Username, NameReal, Pass) VALUES ("test1", "test1", SHA2("test1",256));
INSERT INTO Users (Username, NameReal, Pass) VALUES ("test2", "test2", SHA2("test2",256));
INSERT INTO Users (Username, NameReal, Pass) VALUES ("4test", "4test", SHA2("4test",256));
INSERT INTO Messages (Mesg, Username) VALUES ("This is a test Message","test1");
INSERT INTO Messages (Mesg, Username) VALUES ("This is another test","test2");
INSERT INTO Messages (Mesg, Username) VALUES ("This is again another test Message","test1");
INSERT INTO Messages (Mesg, Username) VALUES ("This is a final test","test2");

COMMIT;