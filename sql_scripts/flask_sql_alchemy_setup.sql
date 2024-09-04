START TRANSACTION;

CREATE TABLE users(
	user_id VARCHAR(36) UNIQUE NOT NULL,
    user_name VARCHAR(12) NOT NULL
);

CREATE TABLE blog_posts(
	blog_post_id VARCHAR(36) NOT NULL,
    blog_post_name VARCHAR(12),
    user_id VARCHAR(36) NOT NULL,
    PRIMARY KEY (blog_post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE user_reviews(
    review_id VARCHAR(36) NOT NULL,
    rating FLOAT NOT NULL,
    blog_post_id VARCHAR(36) NOT NULL,
    user_id VARCHAR(36) NOT NULL,
    PRIMARY KEY (review_id),
    FOREIGN KEY (blog_post_id) REFERENCES blog_posts(blog_post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

COMMIT;

START TRANSACTION;

SET @user_uuid1 = uuid();
SET @user_uuid2 = uuid();
SET @user_uuid3 = uuid();
SET @blog_post_id1 = uuid();
SET @blog_post_id2 = uuid();
SET @review_uuid1 = uuid();
SET @review_uuid2 = uuid();

INSERT INTO users(user_id, user_name)
VALUES (@user_uuid1, 'mark'),
(@user_uuid2, 'john'),
(@user_uuid3, 'peter');

INSERT INTO blog_posts(blog_post_id, blog_post_name, user_id)
VALUES(@blog_post_id1, 'Post 1', @user_uuid1),
(@blog_post_id2, 'Post 2', @user_uuid1);

INSERT INTO user_reviews(review_id, rating, user_id, blog_post_id)
VALUES(uuid(), 4, @user_uuid2, @blog_post_id1),
(uuid(), 3.5, @user_uuid3, @blog_post_id1);

COMMIT;