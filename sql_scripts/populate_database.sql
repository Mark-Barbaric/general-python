START TRANSACTION;

SET @uuid1 = uuid();
SET @uuid2 = uuid();

INSERT INTO users(user_id, user_name)
VALUES (@uuid1, 'mark'),
(@uuid2, 'john');

INSERT INTO blog_posts(blog_post_id, blog_post_name, user_id)
VALUES(uuid(), 'Post 1', @uuid1),
(uuid(), 'Post 2', @uuid1);

COMMIT;