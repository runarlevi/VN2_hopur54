INSERT INTO products_productcategory (name) VALUES('Consoles');
INSERT INTO products_productcategory (name) VALUES('Games');
INSERT INTO products_productcategory (name) VALUES('Accessories');

INSERT INTO products_product (name, description, price, released, stock, category_id) VALUES('PS4: Call of Duty: Black Ops III', 'Call of Duty: Black Ops III takes place in 2065, 40 years after the events of Black Ops II, in a world facing upheaval from conflicts, climate change and new technologies. A Third Cold War is ongoing between two global alliances, known as Winslow Accord and Common Defense Pact.', 39.99, true, 20, 2);
INSERT INTO products_product (name, description, price, released, stock, category_id) VALUES('PS4: Call of Duty: Modern Warfare', 'Call of Duty: Modern Warfare is a 2019 first-person shooter video game developed by Infinity Ward and published by Activision. ... They introduced an entirely new engine for the game, which allows for new performance enhancements such as more detailed environments and ray-tracing capabilities.', 39.99, true, 20, 2);
INSERT INTO products_product (name, description, price, released, stock, category_id) VALUES('PS4: Red Dead Redemption 2', 'Red Dead Redemption 2 is a 2018 action-adventure game developed and published by Rockstar Games. The game is the third entry in the Red Dead series and is a prequel to the 2010 game Red Dead Redemption.', 39.99, true, 20, 2);
INSERT INTO products_product (name, description, price, released, stock, category_id) VALUES('PS4: Marvels Spider-Man', 'Marvels Spider-Man is a 2018 action-adventure game developed by Insomniac Games and published by Sony Interactive Entertainment. Based on the Marvel Comics superhero Spider-Man, it is inspired by the long-running comic book mythology and adaptations in other media.', 39.99, true, 20, 2);


INSERT INTO products_productimage (image, product_id) VALUES('https://upload.wikimedia.org/wikipedia/en/b/b1/Black_Ops_3.jpg', 1);
INSERT INTO products_productimage (image, product_id) VALUES('https://upload.wikimedia.org/wikipedia/en/thumb/e/e9/CallofDutyModernWarfare%282019%29.jpg/220px-CallofDutyModernWarfare%282019%29.jpg', 2);
INSERT INTO products_productimage (image, product_id) VALUES('https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg', 3);
INSERT INTO products_productimage (image, product_id) VALUES('https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Spider-Man_PS4_cover.jpg/220px-Spider-Man_PS4_cover.jpg', 4);