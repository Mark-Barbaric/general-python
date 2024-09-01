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

COMMIT;