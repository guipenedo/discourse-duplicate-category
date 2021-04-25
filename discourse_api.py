#  Copyright (c) 2021. Guilherme Penedo (@guipenedo)
from config import forum_api_key, forum_api_user, forum_url

from pydiscourse import DiscourseClient

client = DiscourseClient(forum_url,
                         api_username=forum_api_user,
                         api_key=forum_api_key)


def get_category_names():
    return [x["name"] for x in client.categories()]


def get_category_by_name(name):
    for cat in client.categories():
        if cat["name"] == name:
            return cat
    return None


def get_about_post(category):
    if "topic_url" in category:
        comps = category["topic_url"].split("/")
        if len(comps) == 4:
            return client.post(comps[2], comps[3])


def duplicate_category(old, name, slug, parent=None, sub_slug="", group_mapping=None):
    if group_mapping is None:
        group_mapping = {}
    old = client._get(u"/c/{0}{1}/find_by_slug.json".format(sub_slug, old["slug"]))["category"]  # more info
    data = {}
    for x in old:
        if x not in ["name", "slug", "position", "color", "text_color"]:
            data[x] = old[x]
            if data[x] == False:
                data[x] = 'false'
    # description_excerpt, description, uploaded_logo, description_text, navigate_to_first_post_after_read, permission
    # use the new slug
    data["slug"] = slug
    # images
    if "uploaded_logo" in old and old["uploaded_logo"]:
        data["uploaded_logo_id"] = old["uploaded_logo"]["id"]
    if "uploaded_background" in old and old["uploaded_background"]:
        data["uploaded_background_id"] = old["uploaded_background"]["id"]
    # permissions are cleared initially
    data["permissions"] = {}
    # reviewer group also has to be replaced
    if 'reviewable_by_group_name' in old and old['reviewable_by_group_name'] in group_mapping:
        data['reviewable_by_group_name'] = group_mapping[old['reviewable_by_group_name']]
    # all access permissions, possibly with group mapping
    if 'group_permissions' in old:
        for g in old['group_permissions']:
            gname = g["group_name"]
            if gname in group_mapping:
                gname = group_mapping[gname]
            data["permissions"][gname] = g["permission_type"]
    cat = client.create_category(name, old["color"], old["text_color"], parent=parent, **data)["category"]
    # description
    about_post = get_about_post(old)
    if about_post:
        new_about_post = get_about_post(cat)
        if new_about_post:
            client.update_post(new_about_post["post_stream"]["posts"][0]["id"],
                               about_post["post_stream"]["posts"][0]["cooked"])
    print("Created category", name)
    for sub_cat in client.categories(parent_category_id=old["id"]):
        print("Creating sub-category", sub_cat["name"])
        duplicate_category(sub_cat, sub_cat["name"], sub_cat["slug"], name, sub_slug=old["slug"] + "/", group_mapping=group_mapping)
