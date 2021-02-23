#  Copyright (c) 2021. Guilherme Penedo (@guipenedo)
import discourse_api as disc

if __name__ == '__main__':
    lista_cats = disc.get_category_names()
    print("List of categories:", lista_cats)
    while True:
        cat_name = input("Choose one of the categories from the list above (origin) to duplicate: ")
        if cat_name in lista_cats:
            break
        print("There is no category with that name.")
    while True:
        new_cat_name = input("Choose the name of the new category (destination): ")
        if new_cat_name not in lista_cats:
            break
        print("A category with this name already exists.")
    origin = disc.get_category_by_name(cat_name)
    slug = input(f"The original category slug is {origin['slug']}. Choose slug for new category: ")
    replace_groups = input("Would you like to replace groups from the previous category with different ones, already created? (yes/no) ") == 'yes'
    group_mapping = {}
    if replace_groups:
        n_groups = int(input("How many groups? "))
        for i in range(n_groups):
            g_name = input("Old group " + str(i + 1) + "/" + str(n_groups) + ": ")
            group_mapping[g_name] = input("New group " + str(i + 1) + "/" + str(n_groups) + ": ")
    disc.duplicate_category(origin, new_cat_name, slug, group_mapping=group_mapping)
