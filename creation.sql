.open store.db

PRAGMA foreign_keys = 1;

CREATE TABLE `addr` (
  `aid` int NOT NULL,/*  */   
  `type` varchar(12) NOT NULL, -- the ac
  primary key(`aid`)
);

CREATE TABLE `customer` (
  `cid` int NOT NULL,
  `name` varchar(25) NOT NULL,
  `age` int NOT NULL,
  `card_number` varchar(25) NOT NULL,
  PRIMARY  KEY(`cid`)
);
CREATE TABLE `customer_item` (
  -- confluence
  `cid` int NOT NULL, 
  `item_id` int NOT NULL,
  `item_count` int NOT NULL,
  `time_stamp` varchar(30) NOT NULL,
  FOREIGN KEY(`time_stamp`) REFERENCES corder(`time_stamp`) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY(`cid`) REFERENCES customer(`cid`) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY(`item_id`) REFERENCES item(`item_id`) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE `corder` (
  -- like customer_customer_item confluence
  -- collection of customer_items
  `cid` int NOT NULL,
  `time_stamp` varchar(30) NOT NULL,
  `total_price` float NOT NULL,
  PRIMARY KEY(`time_stamp`),
  FOREIGN KEY(`cid`) REFERENCES customer(`cid`) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE `phone_number` (
  `pid` int NOT NULL,   
  `type` varchar(10) NOT NULL, -- home, work, cell, etc.
  primary key(`pid`)
);

CREATE TABLE `item` (
  -- generic item
  `item_id` int NOT NULL,
  `item_name` varchar(25) NOT NULL,
  `item_price` float NOT NULL,
  PRIMARY KEY(`item_id`)
);

CREATE TABLE c_address(
  `cid` int NOT NULL,
  `aid` int NOT NULL,
  `address_name` varchar(50) NOT NULL,
  PRIMARY KEY (`cid`, `aid`),
  FOREIGN KEY (`cid`) REFERENCES customer(`cid`) ON DELETE CASCADE ON UPDATE CASCADE
  FOREIGN KEY (`aid`) REFERENCES addr(`aid`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `c_number` (
  `cid` int NOT NULL,
  `pid` int NOT NULL,
  `number` varchar(50) NOT NULL, -- the actual phone number
  PRIMARY KEY (`cid`, `pid`),
  FOREIGN KEY (`cid`) REFERENCES customer(`cid`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`pid`)REFERENCES phone_number(`pid`) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE `cart` (
  `cid` int NOT NULL,
  `item_id` int NOT NULL,
  `amount` int NOT NULL,
  FOREIGN KEY(`cid`) REFERENCES customer(`cid`) ON DELETE CASCADE ON UPDATE CASCADE
  FOREIGN KEY (`item_id`) REFERENCES item(`item_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

