import collections
import mongomock
from community import *


class TestCommunity:

    def test_create_community(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        result = create_community(username, community, collection)
        assert result == True

    def test_create_community2(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        create_community(username, community, collection)
        result = create_community(username, community, collection)
        assert result == False

    def test_join_community(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        result = join_community(username, community, collection)
        assert result == False

    def test_join_community2(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        create_community("User", community, collection)
        result = join_community(username, community, collection)
        assert result == ['User', 'TestName']

    def test_leave_community(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        result = leave_community(username, community, collection)
        assert result == False

    def test_leave_community2(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        create_community("User", community, collection)
        join_community(username, community, collection)
        result = leave_community(username, community, collection)
        assert result == True

    def test_make_post_in_community(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        content = "TestContent"
        community = "CommunityTest"
        post_title = "testTitle"
        result = make_post_in_community(
            username, post_title, content, community, collection)
        assert result == True

    def test_make_post_in_community2(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        content = "TestContent"
        post_title = "testTitle"
        create_community("User", community, collection)
        result = make_post_in_community(
            username, post_title, content, community, collection)
        assert result != False

    def test_show_community_with_posts(self):
        collection = mongomock.MongoClient().db.collection
        community = "CommunityTest"
        result = show_community_with_posts(community, collection)
        assert result == False

    def test_show_community_with_posts2(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        post_title = "testTitle"
        content = "TestContent"
        create_community("User", community, collection)
        make_post_in_community(
            username, post_title, content, community, collection)
        result = show_community_with_posts(community, collection)
        creator = result["posts"][0]["creator"]
        assert creator == "TestName"

    def test_set_community_rules(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        rules = ["No Running", "No Diving"]
        create_community("User", community, collection)
        result = set_community_rules(username, community, rules, collection)
        assert result == False

    def test_set_community_rules2(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        rules = ["No Running", "No Diving"]
        create_community(username, community, collection)
        result = set_community_rules(username, community, rules, collection)
        assert result == True

    def test_ban_in_community(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        target = "TestTarget"
        reason = "Breaking community rules"
        create_community(username, community, collection)
        result = ban_in_community(
            username, target, community, reason, collection)
        assert result == False

    def test_ban_in_community2(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        target = "TestTarget"
        reason = "Breaking community rules"
        create_community(username, community, collection)
        join_community(target, community, collection)
        result = ban_in_community(
            username, target, community, reason, collection)
        assert result == True

    def test_delete_post(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        post_title = "testTitle"
        content = "TestContent"
        create_community(username, community, collection)
        make_post_in_community(username, post_title,
                               content, community, collection)
        community_posts = show_community_with_posts(community, collection)
        post_id = community_posts["posts"][0]["_id"]
        result = delete_post(post_id, collection)
        assert result == True

# Fix make post
    def test_like_post(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        post_title = "testTitle"
        content = "TestContent"
        create_community(username, community, collection)
        post_id = make_post_in_community(
            "Testname2", post_title, content, community, collection)
        result = like_post(post_id, community, username, collection)
        assert result == False

# Fix make post
    def test_comment_on_post(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        post_title = "testTitle"
        content = "This is a comment"
        content1 = "This is text"
        create_community(username, community, collection)
        post_id = make_post_in_community(
            "Testname2", post_title, content1, community, collection)
        result = comment_on_post(
            post_id, community, username, content, collection)
        assert result == False

    def test_show_community_memebrs(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        create_community(username, community, collection)
        result = show_community_memebrs(community, collection)
        assert result[0] == "TestName"

# Fix make post
    def test_delete_comment(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        post_title = "testTitle"
        content = "This is a comment"
        content1 = "This is text"
        create_community(username, community, collection)
        post_id = make_post_in_community(
            username, post_title, content1, community, collection)
        comment_id = comment_on_post(
            post_id, community, username, content, collection)
        result = delete_comment(username, community,
                                post_id, comment_id, collection)
        assert result == False

    def test_upgrade_to_mod(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        create_community("User", community, collection)
        join_community(username, community, collection)
        result = upgrade_to_mod(username, community, collection)
        assert result == True

    def test_downgrade_to_user(self):
        collection = mongomock.MongoClient().db.collection
        username = "TestName"
        community = "CommunityTest"
        create_community("User", community, collection)
        join_community(username, community, collection)
        upgrade_to_mod(username, community, collection)
        result = downgrade_to_user(username, community, collection)
        assert result == True
