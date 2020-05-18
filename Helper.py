class Helper:

    def filter_blog_post_by_user(self, user_id, blog_posts):
        blog_post_for_user = []
        for post_id in blog_posts:
            if blog_posts[post_id].userId == user_id:
                blog_post_for_user.append(blog_posts[post_id].to_json())

        return blog_post_for_user
