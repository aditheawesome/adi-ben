.open store.db
PRAGMA foreign_keys = 1;

insert into item values(0, "apple", 0.5);
insert into item values(1, "orange", 0.75);
insert into item values(2, "bananas", 3);
insert into item values(3, "watermelon", 2.5);
insert into item values(4, "strawberries", 5);
 
insert into phone_number values(0, "home");
insert into phone_number values(1, "work");
insert into phone_number values(2, "cell");

insert into addr values(0, "home");
insert into addr values(1, "work");
insert into addr values(2, "grandmas");


insert into customer values (12345, "Adi", 13, "1111-1111-1111-1111");
insert into customer values (23456, "Ben", 15, "2222-2222-2222-2222");

insert into c_number values (12345, 0, "111-111-1111");
insert into c_number values (12345, 1, "222-222-2222");
insert into c_number values (23456, 1, "333-333-3333");
insert into c_number values (23456, 0, "444-444-4444");
insert into c_number values (12345, 2, "555-555-5555");

insert into c_address values (12345, 0, "111 A Road");
insert into c_address values (23456, 0, "222 B Street");
insert into c_address values (23456, 1, "333 C Drive");

-- select * from corder;
-- select * from customer_item;
-- DELETE FROM customer_item WHERE cid = 19295;

select * from item;
select * from phone_number;
select * from addr;
select * from customer;
select * from c_number;
select * from c_address;

-- select * from customer_item;
select "end selections";
--customer id, time stamp, name print out for all specific purchased frname;
--customer id, time stamp, name print out for all specific purchased fruits

-- select customer.cid, customer_item.time_stamp, customer_item.item_count, item.item_name
-- from customer, customer_item, item
-- where customer.cid = customer_item.cid and customer_item.item_id = item.item_id;


-- SELECT COUNT(item_id) FROM cart;

