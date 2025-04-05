CREATE TABLE tbl (
    table_id INT(11),
    location VARCHAR(255),
    PRIMARY KEY (table_id)
);
CREATE TABLE customer (
    customer_id INT(11),
    name VARCHAR(100),
    NIC_no VARCHAR(12),
    contact_no VARCHAR(10),
    PRIMARY KEY (customer_id)
);

CREATE TABLE waiter (
    waiter_id INT(11),
    name VARCHAR(150),
    contact_no VARCHAR(10),
    shift VARCHAR(10),
    PRIMARY KEY (waiter_id)
);

CREATE TABLE table_order (
    order_id INT(11),
    date_time DATETIME,
    table_id INT(11),
    waiter_id INT(11),
    PRIMARY KEY (order_id),
    FOREIGN KEY (table_id) REFERENCES tbl(table_id),
    FOREIGN KEY (waiter_id) REFERENCES waiter(waiter_id)
);

CREATE TABLE reservation (
    reservation_id INT(11),
    date_time DATETIME,
    no_of_pax INT(11),
    order_id INT(11),
    table_id INT(11),
    customer_id INT(11),
    PRIMARY KEY (reservation_id),
    FOREIGN KEY (order_id) REFERENCES table_order(order_id),
    FOREIGN KEY (table_id) REFERENCES tbl(table_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE menu (
    menu_id INT(11),
    description VARCHAR(255),
    availability INT(11),
    PRIMARY KEY (menu_id)
);

CREATE TABLE menu_item (
    menu_item_id INT(11),
    description VARCHAR(255),
    price FLOAT,
    availability INT(11),
    menu_id INT(11),
    PRIMARY KEY (menu_item_id),
    FOREIGN KEY (menu_id) REFERENCES menu(menu_id)
);

CREATE TABLE order_menu_item (
    order_id INT(11),
    menu_item_id INT(11),
    quantity INT(11),
    FOREIGN KEY (order_id) REFERENCES table_order(order_id),
    FOREIGN KEY (menu_item_id) REFERENCES menu_item(menu_item_id)
);
