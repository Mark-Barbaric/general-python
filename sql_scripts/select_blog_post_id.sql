SELECT * FROM blog_posts.blog_post_id, blog_posts.blog_post_name, users.user_name
INNER JOIN users ON users.user_id = blog_posts.user_id